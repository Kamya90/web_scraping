#!/usr/bin/env python
# coding: utf-8

# In[1]:


# IMPORT ALL THE REQUIRED PACKAGES AND LIBRARIES
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
URL='https://www.marketsandmarkets.com/telecom-and-IT-market-research-113.html'


# In[2]:


# INITIALIZATION OF LISTS 
report_title = []
date_published=[]
link=[]
report_description=[]


# In[3]:


#RAW HTML CODE EXTRACTION
page=requests.get(URL)
soup=BeautifulSoup(page.content,'html.parser')#PARSED VERSION
print (soup.prettify())#PUTS LINE INTO HTML LIST ELEMENT


# In[4]:


#EXTRACTION OF REPORT TITLES AND APPENDING IT IN THE LIST CREATED PREVIOUSLY
for heading in soup.find_all('h3', align='justify'):
     report_title.append(heading.text.strip())
print( report_title)   
    


# In[8]:


#EXTRACTION OF DATES AND APPENDING IT IN THE LIST CREATED PREVIOUSLY
for dates in soup.find_all('td',class_='displaynone'):
    trimmed_text=dates.renderContents()
    date_published.append(trimmed_text.strip())
print(date_published)   


# In[6]:


#EXTRACTION OF REPORT CONTENT  AND APPENDING IT IN THE LIST CREATED PREVIOUSLY
for content in soup.find_all('p', align='justify'):
    report_description.append(content.text.strip())
print(report_description)   
    


# In[18]:


#EXTRACTION OF REPORT LINKS AND APPENDING IT IN THE LIST CREATED PREVIOUSLYtable = soup.find('table', 'reportTbl')
links = soup.find_all('a',href=True)
link.append(links)
print(link)


# In[ ]:





# In[19]:


#OPENING OF A FILE
 
file = open('ReportTitle.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(report_title) 
    


# In[20]:


dict = {'report_title': report_title}   
df = pd.DataFrame(dict)  #CONVERSION INTO A DATAFRAME  
df.to_csv('ReportTitle.csv')  #CONVERSION INTO .CSV FILE TYPE


# In[21]:


df = pd.read_csv('ReportTitle.csv')
print(df)


# In[22]:


file1 = open('Date_Published.csv', 'w+', newline ='') 
with file1:     
    write = csv.writer(file1) 
    write.writerows(date_published) 
    


# In[23]:


dict1 = {'date_published': date_published}          
df = pd.DataFrame(dict1)   
df.to_csv('Publishing_Date.csv') 
df = pd.read_csv('Publishing_Date.csv')
print(df)


# In[24]:


file2 = open('Links.csv', 'w+', newline ='') 
with file2:     
    write = csv.writer(file2) 
    write.writerows(links) 
dict2 = {'links':links }          
df = pd.DataFrame(dict2)   
df.to_csv('Links.csv') 
df = pd.read_csv('Links.csv')
print(df)            


# In[25]:


file3 = open('Report_Description.csv', 'w+', newline ='',encoding='utf-8') 
with file3:     
    write = csv.writer(file3) 
    write.writerows(report_description) 
dict3 = {'report_description': report_description}          
df = pd.DataFrame(dict3)   
df.to_csv('Report_Description.csv') 
df = pd.read_csv('Report_Description.csv')
print(df)      


# In[ ]:





# In[ ]:




