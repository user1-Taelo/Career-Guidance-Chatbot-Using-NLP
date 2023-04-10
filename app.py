from flask import Flask, render_template, jsonify, request
import processor

app = Flask(__name__)

app.config['SECRET_KEY'] = '901011915BSSMY4S204212262168130420076'

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/Chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

        return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
