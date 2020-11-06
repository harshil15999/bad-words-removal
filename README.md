# <Library Name>  <br>
https://questgen.ai/  


Questgen AI is an opensource NLP library focused on developing easy to use Question generation algorithms.<br>
It is on a quest build the world's most advanced question generation AI leveraging on state-of-the-art transformer models like T5, BERT and OpenAI GPT-2 etc.


<img src= './quest.gif' >

### Current Features :
<pre>
1. Multiple Choice Questions (MCQs)
2. Boolean Questions (Yes/No)
3. General FAQs
4. Paraphrasing any Question  
5. Question Answering.
</pre>

## Simple and Complete Google Colab Demo
[![Open In Colab]()


## 1. Installation

### 1.1 Libraries
```
pip install git+https://github.com/ramsrigouthamg/Questgen.ai
pip install sense2vec==1.0.2
pip install git+https://github.com/boudinfl/pke.git

python -m nltk.downloader universal_tagset
python -m spacy download en 
```
### 1.2 Download and extract zip of Sense2vec wordvectors that are used for generation of multiple choices.
```
wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
tar -xvf  s2v_reddit_2015_md.tar.gz
```

## 2. Running the code

### 2.1 Generate boolean (Yes/No) Questions
```
from pprint import pprint
from Questgen import main
qe= main.BoolQGen()
payload = {
            "input_text": "Sachin Ramesh Tendulkar is a former international cricketer from India and a former captain of the Indian national team. He is widely regarded as one of the greatest batsmen in the history of cricket. He is the highest run scorer of all time in International cricket."
        }
output = qe.predict_boolq(payload)
pprint (output)
```

<details>
<summary>Show Output</summary>

```
'Boolean Questions': ['Is sachin ramesh tendulkar the highest run scorer in '
                       'cricket?',
                       'Is sachin ramesh tendulkar the highest run scorer in '
                       'cricket?',
                       'Is sachin tendulkar the highest run scorer in '
                       'cricket?']

```
</details>


### NLP models used

For maintaining meaningfulness in Questions, Questgen uses Three T5 models. One for Boolean Question generation, one for MCQs, FAQs, Paraphrasing and one for answer generation.

### Online Demo website


### License


### Contribution guidelines


### Contributors Profile




[![Linkedin Link](linkedin.png)](#link to your linkedin)
