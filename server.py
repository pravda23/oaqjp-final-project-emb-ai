from flask import Flask, request, render_template
# from "EmotionDetection" import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def render_index_page():
    return render_template('index.html')

def analyze_sentiment():
    text_to_analyze = request.args.get('textToAnalyze')
    # response = emotion_detector(text_to_analyze)
    # label = response['label']
    # score = response['score']
    
    return "server running on port 4000"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)