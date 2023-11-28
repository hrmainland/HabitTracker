import urllib.parse
import http.client

USER_KEY = "yourKeyHere"
API_TOKEN = "yourTokenHere"

def send_push(title, message):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": API_TOKEN,
                     "user": USER_KEY,
                     "message": message,
                     "title": title,
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    response = conn.getresponse()
    if response.code == 200:
        print("Push Sent")
