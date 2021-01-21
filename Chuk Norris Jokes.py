#!/usr/bin/env python
# coding: utf-8

# #  Jokes Scrappper 

# In[1]:


import requests
import json

jokes_dict = {}

n = int(input('Enter the number of jokes you want to Scrape'))

#scrapping all the jokes and adding to the dictionary with their indexes 
for i in range(1, n):
    # url can be any 
    jokes_url = f"http://api.icndb.com/jokes/{i}"
    if json.loads(requests.get(jokes_url).content)['type'] == 'success':
        jokes_dict[i] = (json.loads(requests.get(jokes_url).content)['value']['joke'])
        
joke_nu = int(input("Enter the joke Number"))

print(jokes_dict[joke_nu])


# In[ ]:




