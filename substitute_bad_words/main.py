#importing require helping data
from .bad_words import bad_words
from .food import food
print("STARTING")


import spacy
import en_core_web_sm
from spacy import displacy
import nltk
import numpy as np
import random 
nlp = en_core_web_sm.load()

from flask import request
#need to write the functions to clean up the input 

def subsitute(word,data,first_word_label,last_word_label,default='falooda'):
    word=word.lower()
    x=data.loc[(data['%s'%(first_word_label)]==word[0])&
               (data['%s'%(last_word_label)]==word[-1])]
    x=x.sample(random_state=43,frac=1)
    
    if(x.shape[0]>=1):
        return x.reset_index(drop=True)['FOOD_NAME'].to_numpy()
    
    x=data.loc[(data['%s'%(first_word_label)]==word[0])]
    x=x.sample(random_state=43,frac=1)
    
    if(x.shape[0]>=1):
        return x.reset_index(drop=True)['FOOD_NAME'].to_numpy()
    
    x=data.loc[(data['%s'%(last_word_label)]==word[-1])].head(1)
    x=x.sample(random_state=43,frac=1)
    
    if(x.shape[0]>=1):
        return x.reset_index(drop=True)['FOOD_NAME'].to_numpy()
    else:
        return np.array(default)


def check(text):
    doc = nlp(text)  
    l=[]
    words=[]
    tags=[]
    mask=[]
    original_words=[]
    for token in doc:
        #print(token.text,  token.pos_, token.tag_, token.dep_,token.is_alpha)
        original_words.append(token.text)
        if(token.pos_!="VERB"):
            if(bad_words.store.get(token.text)!=None):
                mask.append(1)
                x=subsitute(token.text,food,'firstword','lastword')
                np.random.shuffle(x)
                
                y=x[0]
                l.append(y)
                tags.append(token.pos_)
            else:
                tags.append(token.pos_)
                l.append(token.text)
                mask.append(0)
    print(l)
    return l



from flask import Flask,jsonify
from flask import request
app = Flask(__name__)

@app.route('/check', methods=['POST'])
def create_task():
    if not request.json or not 'text' in request.json :
        abort(400)
    data = request.json
    x=data['text']
    answer=check(x)
    temp=''
    for i in answer:
        temp=temp+" "+i
    return jsonify({'text': temp}), 200


if __name__ == '__main__':
    app.run(debug=True,port=8080)


