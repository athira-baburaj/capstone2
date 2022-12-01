#!/usr/bin/env python
# coding: utf-8

# # Creating Database for NS faculty's Salaries using Python

# #### Phase 1: Merging the pdf files

# In[1]:


import os
from PyPDF2 import PdfFileMerger
# use dict to sort by filepath or filename
file_dict = {}
for subdir, dirs, files in os.walk("C:/Users/athi0/OneDrive/Desktop/Capstone Project/New folder/2022"):
    for file in files:
        filepath = subdir + os.sep + file
        # you can have multiple endswith
        if filepath.endswith((".pdf", ".PDF")):
            file_dict[file] = filepath
            print(file)
# use strict = False to ignore PdfReadError: Illegal character error
merger = PdfFileMerger(strict=False)



for k, v in file_dict.items():
    print(k, v)
    merger.append(v)



merger.write("C:/Users/athi0/OneDrive/Desktop/Capstone Project/New folder/pdf/single_file_2022.pdf")


# #### Phase 2: Reading Tabular data from the merged pdf file yearwise

# In[2]:


import tabula as tb
import pandas as pd
df = tb.read_pdf("C:/Users/athi0/OneDrive/Desktop/Capstone Project/New folder/pdf/single_file_2022.pdf",pages="all")
print(len(df))


# In[3]:


with open('C:/Users/athi0/OneDrive/Desktop/Capstone Project/New folder/csv/all_dfs_2022.csv','a',encoding='utf-8') as f:
     for x in df:
        x.to_csv(f)
        f.write("\n")


# #### Phase 3: Creating database and extracting the data we need

# In[4]:


import sqlite3
conn = sqlite3.connect('my_data.db')
c = conn.cursor()


# In[9]:


c.execute('''CREATE TABLE universities (Year integer, University text, Name text, Salary integer)''')


# In[10]:


import pandas as pd
# load the data into a Pandas DataFrame
universities = pd.read_csv('C:/Users/athi0/OneDrive/Desktop/Capstone Project/New folder/csv/csv-All Year.csv')
# write the data to a sqlite table
universities.to_sql('universities', conn, if_exists='append', index = False) 


# In[11]:


c.execute('''SELECT * FROM universities''').fetchall()


# In[12]:


c.execute('''SELECT year, university, name, salary FROM universities where name Like "%Patricia%" and university = "Acadia University"''').fetchall()


# In[13]:


c.execute('''SELECT year, university, name, salary FROM universities where salary > 350000''').fetchall() 


# In[14]:


c.execute('''SELECT Year, University, name, salary FROM universities where name Like "%macleod%" and Year = 2019''').fetchall()

