from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import detect_emotion

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET','POST'])
def emotion_detector():
    # try query params, then form data, then JSON body
    text = request.args.get('textToAnalyze')
    if not text:
        text = request.form.get('textToAnalyze')
    if not text:
        data = request.get_json(silent=True)
        if data:
            text = data.get('textToAnalyze') or data.get('text')

    print("Received text:", repr(text))

    if not text or str(text).strip() == "":
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    emotion_result = detect_emotion(text)

    response = (
        f"For the given statement, the system response is "
        f"'anger': {emotion_result['anger']}, "
        f"'disgust': {emotion_result['disgust']}, "
        f"'fear': {emotion_result['fear']}, "
        f"'joy': {emotion_result['joy']} and "
        f"'sadness': {emotion_result['sadness']}. "
        f"The dominant emotion is {emotion_result['dominant_emotion']}."
    )

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)