from flask import Flask,jsonify
from flask import request
from flask import render_template
from flask import abort

app = Flask(__name__,
    static_folder='assets',
)
from substitute_bad_words.main import check

@app.route("/")
def index():
    return render_template("index.html",
    prediction_text="put the words here")


@app.route('/', methods=['POST'])
def create_task():
    
    data = request.form
    print(data)
    x=data['comment']
    answer=check(x)
    temp=''
    for i in answer:
        temp=temp+" "+i

    return render_template("index.html",prediction_text=temp)
    
    


if __name__ == '__main__':
    
    app.run(debug=True,port=8080)