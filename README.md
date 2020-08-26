The files record.py, post.py and mqtt_publisher.py need to be present on the Raspberry Pi (which is connected to a Raspberry Camera and Mic).

Python packages required on the Pi: 
pyaudio

The file keras_server.py and the folder ml (which contains the trained model) needs to be in another system that can run the model remotely.
Python packages required for running a successful prediction on the system:
keras
tensorflow
librosa
numPy
matplotlib

The Raspberry Pi and the system running the model should be connected to the same network. The keras server will run on port 9787 by default which can be changed in keras_server.py


Results:
The machine learning model was evaluated on a test set and resulted in an accuracy of around 81%. 

A major roadblock which we tried handling throughout the project is to handle if computation is feasible on the Raspberry Pi. A better results can be achieved if higher computation ability is available.  
