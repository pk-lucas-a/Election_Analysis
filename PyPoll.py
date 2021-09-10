#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pseudocode
#1. Open csv
#2. Get candidate names
#3. Run vote count for each
#4. Get total votes 
#5. Return percentage won
#6. Return winner


# In[2]:


# Add our dependencies.
import os
dir(os.path)
import csv


# In[3]:


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# In[4]:


# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    
    # Read and print the header row.
    headers = next(file_reader) #causes first row to be skipped in future
    print(headers)
    
    #for row in file_reader:
        #print(row)
    


# In[ ]:


#Alternate file open
# Assign a variable for the file to load and the path.
##file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
#with open(file_to_load) as election_data:
    # Print the file object.
     #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
##file_to_save = os.path.join("analysis", "election_analysis.txt") 
        
# write data to the file.
##open(file_to_save, "w")


# In[ ]:




