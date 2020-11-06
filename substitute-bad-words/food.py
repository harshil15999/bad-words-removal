

path="data/generic-food.csv"

import pandas as pd
food=pd.read_csv(path)
#%%

food['firstword']=''
food['lastword']=''
#%%
food['firstword']=food['FOOD_NAME'].apply(lambda x: x[0].lower())
food['lastword']=food['FOOD_NAME'].apply(lambda x: x[-1].lower())

#%%

