from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][0]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__": 
    #makes sure the server only runs if the script is executed directly from the 
    #Python interpreter and not used as an imported module.
    app.run(debug=True, host='0.0.0.0', port=80) 
    #so that our flask app will run on the servers IP address and not on 
    #localhost that way we can access it remotely.

    #debug=True : don't need to rerun server every change