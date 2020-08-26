# importing the requests library 
import requests
import sys

def flaskReq(path):
    URL = "http://169.234.30.191:9787/predict"
    with open(path, 'rb') as fobj:
        payload = {"audio": fobj} 
        request = requests.post(URL, files = payload)
        request = request.json()
        if request["success"]: 
            return request["predictions"]
        else:
            return "Request failed"

if __name__ == '__main__':
    flaskReq('demo.wav')
