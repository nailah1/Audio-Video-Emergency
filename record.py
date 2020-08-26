from sys import byteorder
from array import array
from struct import pack
from picamera import PiCamera
from time import sleep

import pyaudio
import wave
import post
import mqtt_publisher

THRESHOLD = 200
CHUNK_SIZE = 512
FORMAT = pyaudio.paInt16
RATE = 44100
CHANNELS = 1
DEVICE_INDEX= 1

def is_silent(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    print(max(snd_data))
    return max(snd_data) < THRESHOLD

def check():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdev = info.get('deviceCount')
    for i in range (0, numdev):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("ID = ", i, "-", p.get_device_info_by_host_api_device_index(0,i).get('name'))
    
def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    "Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in xrange(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in xrange(int(seconds*RATE))])
    return r

def record():
    """
    Record a word or words from the microphone and 
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the 
    start and end, and pads with 0.5 seconds of 
    blank sound to make sure VLC et al can play 
    it without getting chopped off.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
        input_device_index = DEVICE_INDEX,
        input=True, output=False,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        # little endian, signed short
        try:
            snd_data = array('h', stream.read(CHUNK_SIZE))
            if byteorder == 'big':
                snd_data.byteswap()
            r.extend(snd_data)

            silent = is_silent(snd_data)

            if silent and snd_started:
                num_silent += 1
            elif not silent and not snd_started:
                snd_started = True

            if snd_started and num_silent > 100:
                break
        except IOError as ex:
            if ex[1] != pyaudio.paInputOverflowed:
                raise
            data = '\x00' * CHUNK_SIZE  # or however you choose to handle it, e.g. return None

        

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.4)
    return sample_width, r

def record_to_file(path):
    print("Records from the microphone and outputs the resulting data to 'path'")

    
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()


if __name__ == '__main__':
    file_count=0
    camera = PiCamera()
    check()
    while(True):
        file_count  += 1
        print("please speak a word into the microphone")
        # checkFun()
#        file_name = 'demo_'+str(file_count)+'.wav'
        file_name = 'test.wav'
        record_to_file(file_name)
        #print("Sending file: ",file_name)
        result = post.flaskReq(file_name)
        result = float(result)
        if(result > 50.0):
            camera.start_preview()
            sleep(5)
            camera.capture('image.jpg')
            camera.stop_preview()
            mqtt_publisher.publish(result)
        print("done - result written to demo.wav")
    
