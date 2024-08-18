# Import the requests library to handle HTTP requests
import requests
import json

# Define a function name emotion_detector that takes a string input (text_to_analyze)
def emotion_detector(text_to_analyze):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detection API with the text and headers
    response = requests.post(url, json=myobj, headers=header)
    
    # Parse the response from the API
    formatted_response = json.loads(response.text)

    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    # Determine the dominant emotion
    dominant_emotion = max({'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness},
    key=lambda k: {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}[k])

    # Return results including the dominant emotion
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}