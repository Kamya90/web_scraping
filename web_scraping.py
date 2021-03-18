#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import csv
URL='https://www.marketsandmarkets.com/telecom-and-IT-market-research-113.html'


# In[2]:


report_title = []
date_published=[]
link=[]
report_description=[]
USD_value=[]


# In[3]:


page=requests.get(URL)
soup=BeautifulSoup(page.content,'html.parser')
print (soup.prettify())


# In[4]:



for heading in soup.find_all('h3', align='justify'):
    report_title.append(heading.text.strip())
print( report_title)   
   


# In[20]:


for dates in soup.find_all('td',class_='displaynone'):
    trimmed_text=dates.renderContents()
    date_published.append(trimmed_text.strip())
print(date_published)   


# In[6]:


for content in soup.find_all('p', align='justify'):
    report_description.append(content.text.strip())
print(report_description)   
    


# In[7]:


table = soup.find('table', 'reportTbl')
links = table.find_all('a',href=True)
link.append(links)
print(link)


# In[22]:





# In[9]:



 
file = open('ReportTitle.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(report_title) 
    


# In[10]:


dict = {'title': report_title}   
       
df = pd.DataFrame(dict)  
    
# saving the dataframe  
df.to_csv('ReportTitle.csv')  


# In[11]:


df = pd.read_csv('ReportTitle.csv')
print(df)


# In[12]:


file1 = open('ReportTitle.csv', 'w+', newline ='') 
with file1:     
    write = csv.writer(file1) 
    write.writerows(date_published) 
    


# In[16]:


dict1 = {'title': date_published}          
df = pd.DataFrame(dict1)   
df.to_csv('Publishing_Date.csv') 
df = pd.read_csv('Publishing_Date.csv')
print(df)


# In[14]:


file2 = open('Links.csv', 'w+', newline ='') 
with file2:     
    write = csv.writer(file2) 
    write.writerows(link) 
dict2 = {'title':links }          
df = pd.DataFrame(dict2)   
df.to_csv('Links.csv') 
df = pd.read_csv('Links.csv')
print(df)            


# In[15]:


file3 = open('Report_Description.csv', 'w+', newline ='',encoding='utf-8') 
with file3:     
    write = csv.writer(file3) 
    write.writerows(report_description) 
dict3 = {'title': report_description}          
df = pd.DataFrame(dict3)   
df.to_csv('Report_Description.csv') 
df = pd.read_csv('Report_Description.csv')
print(df)      


# In[ ]:





# In[ ]:




