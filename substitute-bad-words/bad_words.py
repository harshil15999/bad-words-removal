path="data/bad-words.csv"
import pandas as pd
data=pd.read_csv(path)

class create_dictionary:
    def __init__(self):
        self.store=dict()
        
    class words:
        def __init__(self,word,firstword,lastword):
            self.firstword=firstword
            self.lastword=lastword
            
    def pass_words(self,word):
        h=self.words(word,word[0],word[-1])
        self.store[word]=h
        

bad_words=create_dictionary()
data['fucking'].apply(bad_words.pass_words)   



