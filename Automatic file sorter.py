#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os,shutil


# In[12]:


path=r"C:/Users/sneha/OneDrive/Desktop/Documents/Sneha documents/"


# In[17]:


file_name =os.listdir(path)
file_name


# In[23]:


folder_name=['Pdf file','Img file']
for folder in range(0,len(folder_name)):
            if not os.path.exists(path + folder_name[folder]):
                #print(path+ folder_name[folder])
                os.makedirs(path + folder_name[folder])
                
for file in file_name:
        if ".pdf" in file and not os.path.exists(path + "Pdf file/"+ file):
            shutil.move(path+file, path +"Pdf file/"+ file)
        elif ".jpg" in file and not os.path.exists(path + "Img file/"+ file):
            shutil.move(path+file, path +"Img file/"+ file)                  


# In[20]:





# In[ ]:




