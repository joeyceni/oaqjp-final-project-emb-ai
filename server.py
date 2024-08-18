''' Executing this function initiates the Emotion Detection app to be deployed on localhost:5000 '''

# Import Flask, render_template, request from the flask framework package:
# Import the emotion_detector function from the package created:
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    '''
    The function obtains the returned response from the emotion_detector function
    and parses the emotions into their respective variables for further processing
    as either emotion scores or None.
    Args:
        anger (Optional[float]): Score for the anger emotion, or None
        disgust (Optional[float]):  Score for the disgust emotion, or None
        fear (Optional[float]):  Score for the fear emotion, or None
        joy (Optional[float]):  Score for the joy emotion, or None
        sadness (Optional[float]):  Score for the sadness emotion, or None
        dominant_emotion (Optional[float]): Score for the dominant_emotion emotion, or None 
    Returns:
        Numeric score or None resulting in an informative statement or "Invalid" msg, respectively
    '''
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
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
