import requests
import private

rtBaseUrl = 'https://www.rescuetime.com/anapi/data'
rtApiKey = 'key='
rtApiFormat = 'format=json'
# minute&rb=2016-11-24&re=2016-11-25

r = requests.get(rtBaseUrl+'?'+rtApiKey+private.rtEyApiKey+'&'+rtApiFormat)

print(r.json())
