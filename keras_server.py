# Python program to expose a ML model as flask REST API 
  
# import the necessary modules 
import tensorflow as tf 
import numpy as np 
import flask 
import io 

import librosa
import soundfile as sf
import os
from keras.utils import to_categorical
from keras.optimizers import SGD
from keras.models import load_model
  
# Create Flask application and initialize Keras model 
app = flask.Flask(__name__) 
  
# Now, we can predict the results. 
@app.route("/predict", methods =["POST"]) 
def predict(): 
    data = {} # dictionary to store result 
    data["success"] = False
  
    # Check if image was properly sent to our endpoint 
    if flask.request.method == "POST": 
        if flask.request.files.get("audio"): 
            audio = flask.request.files["audio"]
            print(audio)
            model = tf.keras.models.load_model('model.h5')
            pred = predict(model, audio)

            r = os.listdir('data/')
            r.sort()
            sorted = np.argsort(pred)
            count = 0
            data["predictions"] = False
            predictions = {}
            for index in (-pred).argsort()[0]:
                key = r[index + 1]
                predictions[key] = str(round(pred[0][index]*100))
                print(key, predictions[key])
                count += 1

            for key, value in predictions.items():
                if key == 'Scream':
                    data["predictions"] = value

            data["success"] = True
  
    return flask.jsonify(data) 
  
def predict(model, data_path):
    x_data = parse_audio_file(data_path)
    X_train = np.expand_dims(x_data, axis=2)
    pred = model.predict(X_train)
    return pred

def parse_audio_file(fn):
    features = np.empty((0,193))
    ext_features = get_ext_features(fn)
    features = np.vstack([features,ext_features])
    return np.array(features)

def get_ext_features(fn):
    try:
        mfccs, chroma, mel, contrast, tonnetz = extract_feature(fn)
        ext_features = np.hstack([mfccs, chroma, mel, contrast, tonnetz])
        return ext_features
    except Exception as e:
        print("[Error] extract feature error. %s" % (e))
        return None

def extract_feature(file_name):
    X, sample_rate = sf.read(file_name, dtype='float32')
    if X.ndim > 1:
        X = X[:,0]
    X = X.T

    stft = np.abs(librosa.stft(X))
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
    mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,axis=0)
    return mfccs, chroma, mel, contrast, tonnetz
  
if __name__ == "__main__": 
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started")) 
    # load_model() 
    app.run(host="0.0.0.0", port="9787")