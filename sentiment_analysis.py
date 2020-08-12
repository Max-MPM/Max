from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/', methods =['POST','GET'])
def result():
    if request.method == 'POST':
        message = request.form.get('message')
        
        sid_obj = SentimentIntensityAnalyzer() 
        sentiment_dict = sid_obj.polarity_scores(message)
        score = sentiment_dict['compound']
        if score >=0.5:
            sentiment =['positive']
        elif score<=-0.05:
            sentiment =['Negative']
        else:
            sentiment =['Netural'] 

        return '<h1>The sentiment of this message is {}.'.format(sentiment)

    return '''<form method='POST'>
    Message <input type='text' name='message'>
    <input type='submit'>
    </form>'''

if  __name__ == '__main__':
    app.run(debug=True, port=5000)