#!/usr/bin/env python
# coding: utf-8

# In[11]:


from datetime import datetime
datetimenow = datetime.now();
current_datetime = datetimenow.strftime("%d/%m/%Y %H:%M:%S")
print("Current date & time is:=", current_datetime)

