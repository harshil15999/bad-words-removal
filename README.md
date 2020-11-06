# bad-words-removal<br>
https://questgen.ai/  


## Aim

This projec


<img src= './quest.gif' >

## Aim
This project aims to provide an api for removing bad words and improve the overall experience of the online communications.


## Current Features
1. Detecting Bad words and substituting it with food names
2. Detecting the toxicity of the comment/text

## Pipeline Explanation
### **1**. Detecting bad words and susbtituing food names

a. Cleaning the text by using text hero-Tokenization,Punctuation removal
b. POS tagging 
c. RULE based removal of bad words based on POS Tags

### ** 2 ** Detection of toxicity [threat,insult,obscene,toxic,severe_toxic]
a. Pre processing of text for BERT model[tokenization using BERT tokenizer]
b. Adding layers on top of BERT
c. Fine tuning on dataset
d. Validation 
e. Predicting for single query    
    

## Simple and Complete Google Colab Demo
[![Open In Colab]()


## 1. Installation

### 1.1 Libraries
```
python -m nltk.downloader universal_tagset
python -m spacy download en 
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
