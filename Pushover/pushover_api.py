import urllib.parse
import http.client

USER_KEY = "u7mcripqenb5rwr6bz8qsz399orq6u"
PUSH_EMAIL = "1p4su4ww4x@pomail.net"
API_TOKEN = "aoic76g69zsem4e8jbbg2r8q3dh8p9"


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


if __name__ == "__main__":
    send_push("Test", "You've been neglecting your future! Step up, research, and uncover your dream job's path to success! 🔍🚀")
    pass
