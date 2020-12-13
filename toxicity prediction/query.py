
from flask import request
from flask import Flask
app = Flask(__name__)
import numpy as np
import pandas as pd
from sklearn import metrics
import transformers
import torch
from torch.utils.data import Dataset, DataLoader, RandomSampler, SequentialSampler
from transformers import BertTokenizer, BertModel, BertConfig
import pickle

from torch import cuda
device = 'cuda' if cuda.is_available() else 'cpu'

def query(text):
    from transformers import BertTokenizer

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    
    #comment_text='COCKSUCKER BEFORE YOU PISS AROUND ON MY WORK'
    comment_text = " ".join(text.split())

    inputs = tokenizer.encode_plus(
        comment_text,
        None,
        add_special_tokens=True,
        max_length=200,
        pad_to_max_length=True,
        return_token_type_ids=True
    )
    ids = inputs['input_ids']
    mask = inputs['attention_mask']
    token_type_ids = inputs["token_type_ids"]

    ids=torch.tensor(ids, dtype=torch.long)
    mask=torch.tensor(mask, dtype=torch.long)
    token_type_ids=torch.tensor(token_type_ids, dtype=torch.long)

    ids=ids.resize_(1,200)
    mask=mask.resize_(1,200)
    token_type_ids=token_type_ids.resize_((1,200))  
    class BERTClass(torch.nn.Module):
        def __init__(self):
            super(BERTClass, self).__init__()
            self.l1 = transformers.BertModel.from_pretrained('bert-base-uncased')
            self.l2 = torch.nn.Dropout(0.3)
            self.l3 = torch.nn.Linear(768, 6)
        
        def forward(self, ids, mask, token_type_ids):
            _, output_1= self.l1(ids, attention_mask = mask, token_type_ids = token_type_ids)
            output_2 = self.l2(output_1)
            output = self.l3(output_2)
            return output

    model = BERTClass()
    model.to(device)
        
    
    outputs = model(ids.to(device, dtype = torch.long),mask.to(device, dtype = torch.long),token_type_ids.to(device, dtype = torch.long))
    x=torch.sigmoid(outputs).cpu().detach().numpy().tolist()  
    y = np.array(x) >= 0.5
    y=y[0]

    l=['toxic','severe_tocix','obscene','threat','insult','identity_hate']
    ans=[]
    for i in range(len(y)):
        if(y[i]==True):
            #print(l[i])
            ans.append(l[i])
    #x is the original predicted proba
    
    store=dict()
    store['probablity']=x
    store['predicted']=ans
    return store




