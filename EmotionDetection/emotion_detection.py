import requests

def emotion_detector(text_to_analyze):
  """
  This function detects emotions in the provided text using the Watson NLP Emotion Prediction function.

  Args:
      text_to_analyze: The text string to be analyzed for emotions.

  Returns:
      A dictionary containing emotion scores, or None if an error occurs.
  """

  # Define the URL, headers, and input JSON format
  url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
  headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  input_json = {"raw_document": {"text": text_to_analyze}}
  
  # Send POST request with JSON data
  response = requests.post(url, headers=headers, json=input_json)

  if response.status_code == 400:
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }
  
  # Formating the content
  emotion_predictions = response.json()['emotionPredictions'][0]['emotion']
  
  # Loop to define the Maximum score and pick the dominant emotion
  max_score = 0

  for emotion, score in emotion_predictions.items():
    if score > max_score:
        max_score = score
        dominant_emotion = emotion
    
  emotion_predictions['dominant_emotion'] = dominant_emotion

  return emotion_predictions
