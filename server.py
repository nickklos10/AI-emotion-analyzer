"""
Emotion Detection Server

This script defines a Flask-based server for performing emotion detection on user-provided text.

Author(Learner): [Nicholas Klos]
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor
import os

port = int(os.environ.get("PORT", 4000))

app = Flask("Emotion Detection")

def run_emotion_detection():
    """
    Main function to run the Emotion Detection application.
    """
    print(f"🚀 Server starting on port {port}...")
    app.run(host="0.0.0.0", port=port)

@app.route("/emotionDetector", methods=["GET", "POST"])
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    if request.method == 'POST':
        data = request.json
        text_to_detect = data.get('textToAnalyze', '')
    else:
        text_to_detect = request.args.get('textToAnalyze', '')

    if not text_to_detect:
        return "No text provided", 400

    response = emotion_detector(text_to_detect)
    formatted_response = emotion_predictor(response)
    
    if formatted_response['dominant_emotion'] is None:
        return "Invalid text! Please try again.", 500
    
    # Prepare a cleaner formatted response
    readable_response = (
        f"For the given statement, the system response is as follows:<br><br>"
        f"Anger: {formatted_response['anger']*100:.1f}%<br>"
        f"Disgust: {formatted_response['disgust']*100:.1f}%<br>"
        f"Fear: {formatted_response['fear']*100:.1f}%<br>"
        f"Joy: {formatted_response['joy']*100:.1f}%<br>"
        f"Sadness: {formatted_response['sadness']*100:.1f}%<br><br>"
        f"The dominant emotion is: {formatted_response['dominant_emotion'].capitalize()}."
    )
    
    return readable_response


@app.route("/")
def render_index_page():
    """
    Render the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    run_emotion_detection()

