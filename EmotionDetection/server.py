''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''give the correct response depending on the output of watson
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is 'anger': {response['anger']},"
        + f" 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}"
        + f" and 'sadness': {response['sadness']}."
        + f" The dominant emotion is {response['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    '''direction to homepage
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
