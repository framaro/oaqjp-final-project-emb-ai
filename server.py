# import the function emotion_detector
from EmotionDetection.emotion_detection import emotion_detector

#import flask and render_template
from flask import Flask, render_template, request

# creates a flask app
app = Flask("Emotion Detector") 

@app.route("/")
def index():
    """Renders the initial HTML template."""
    return render_template("index.html")

@app.route("/emotionDetector")
def analyze_text():
    """Processes user input and displays emotion detection results."""
    user_text = request.args.get('textToAnalyze')
    
    # Process the text using emotion_detector
    emotion = emotion_detector(user_text)
    
    # Format the output as requested by the customer
    output_text = f"For the given statement, the system response is \n"
    # Iterate through emotions and format the output
    emotions_list = []
    for emotion_name, score in emotion.items():
        if emotion_name != "dominant_emotion":
            emotions_list.append(f"'{emotion_name}': {score}") 

    # Join emotions with appropriate separators
    output_text += ", ".join(emotions_list[:-1]) 
    output_text += " and " + emotions_list[-1] if len(emotions_list) > 1 else "" 

    output_text += f".\nThe dominant emotion is {emotion['dominant_emotion']}." 
    return output_text

if __name__ == "__main__":
    app.run(debug=True)