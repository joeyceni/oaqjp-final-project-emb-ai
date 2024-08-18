''' Executing this function initiates the Emotion Detection application, which 
    is to be executed over the Flask channel and deployed on localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package: 
# Import the emotion_detector function from the package created:
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotions from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the label is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the emotions
        # Return a formatted string with the emotions using f-strings
        return (f"For the given statement, the system response is "
                f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
                f"'joy': {joy} and 'sadness': {sadness}. The dominant emotion "
                f"is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)