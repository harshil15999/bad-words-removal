# bad-words-removal<br>

## Aim
This project aims to provide an api for removing bad words and improve the overall experience of the online communications.


## Current Features
1. Detecting Bad words and substituting it with food names
2. Detecting the toxicity of the comment/text

## Pipeline Explanation
### **1**. Detecting bad words and susbtituing food names : Substitution

a. Cleaning the text by using text hero-Tokenization,Punctuation removal
b. POS tagging 
c. RULE based removal of bad words based on POS Tags


###  2. Detection of toxicity [threat,insult,obscene,toxic,severe_toxic] : Classification
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

### 2.1 Removing Bad Words
```

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

### 2.2 Predicting toxicity
```

```

<details>
<summary>Show Output</summary>

```


```
</details>



### NLP models used
a. Spacy Encore Sm\
b. BERT

### Online Demo website


### License
MIT


### Contribution guidelines


### Contributors Profile




[![Linkedin Link](linkedin.png)](#link to your linkedin)
