#Call http server with encoded string
string = '''
from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "10.40.41.227", 9559)
tts.say("Hello, world!")'''
import urllib.parse
import urllib.request
import json
url = "http://10.100.27.192:8080/run_string/" + urllib.parse.quote(string)
print(url)
response = urllib.request.urlopen(url)
print(response.read())
