#!/usr/bin/env python
# coding: utf-8

# In[19]:


import os, shutil


# In[27]:


path = "C:/Users/CassiuS/Desktop/PyFileSorter/"


# In[28]:


file_name = os.listdir(path)


# In[31]:


folder_names = ['csv files', 'image files', 'text files']

for loop in range(0,3):
 if not os.path.exists(path + folder_names[loop]):
    os.makedirs(path + folder_names[loop])


# In[34]:


for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "text files/" + file):
        shutil.move(path + file, path + "text files/" + file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




