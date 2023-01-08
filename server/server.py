import os
import openai
from flask import Flask, request
from flask_cors import cross_origin
from dotenv import load_dotenv
load_dotenv()

OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')

if not OPEN_AI_KEY:
    print("Please add your OPEN AI KEY in .env")
    quit(0)

app = Flask(__name__)


@app.route("/ask", methods=["GET"])
@cross_origin()
def ask():
    openai.api_key = OPEN_AI_KEY

    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=request.args['q'],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    message = completions.choices[0].text
    return {"answers": message}


if __name__ == "__main__":
    app.run(debug=True)
