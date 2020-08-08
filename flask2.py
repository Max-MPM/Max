from flask import Flask, request

app = Flask(__name__)

#This is a query example
@app.route('/query_example')
def query_example():
    language = request.args.get('language')
    framework = request.args['framework']
    website = request.args.get('website')


    return '''<h1>The lanuage is {}<h1>
              <h1>The framework is {}<h1>
              <h1>The website is {}<h1>'''.format(language, framework, website)

#This is a form example
@app.route('/form_example', methods=['POST','GET'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form['framework']
        return '<h1>The language is {}. The framework is {}.<h1>'.format(language, framework)

    return '''<form method='POST'>
    Language <input type='text' name='language'>
    Framework <input type='text' name='framework'>
    <input type='submit'>
    </form>'''



#This is a JSON example
@app.route('/json_example', methods=['POST'])
def json_example():
    return '....'


if __name__ == '__main__':
    app.run(debug=True, port=5000)