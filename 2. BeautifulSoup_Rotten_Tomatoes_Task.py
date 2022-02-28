#!/usr/bin/env python
# coding: utf-8

# #  Esther Web scraping a Rotten Tomatoes page

# ## Import the relevant libraries

# This exercise is going to use web scraping techniques to extract data and store in a data frame using Pandas. The data that will needed to be included in the data frame will be as follows:
# - Title
# - Year
# - Score
# - Adjusted score
# - Director
# - Cast
# 
# As an exension task, then the following can be added also:
# 
#  - consensus
#  - synopsis
#  
# There will be placeholder headers and some notes to assist you but feel free to delete any of that and work in your own way on this. The completed data frame should be exported as a CSV at the end of the activity. You will need to use the pandas documentation to help with this.
# https://pandas.pydata.org/docs/
# 

# In[51]:


# load packages


# In[2]:


# Define the URL of the site
base_site = 


# ## Check to see if the request was successful

# In[3]:


# sending a request to the webpage


# In[4]:


# get the HTML from the webpage


# ## Choosing a parser

# In[8]:


# convert the HTML to a BeatifulSoup object


# In[9]:


# Exporting the HTML to a file


# ### Re: Parser choice

# In[11]:


# Beautiful Soup ranks the lxml parser as the best one.

# If a parser is not explicitly stated in the Beautiful Soup constructor,
# the best one available on the current machine is chosen.

# This means that the same piece of code can give different results on different computers.


# ## Finding an element containing all the data

# In[7]:


# Right click on the webpage and choose INSPECT to find out the divs of the part of the page that you would like to scrape.
# 
#Find all div tags on the webpage containing the information we want to scrape


# # Extracting the title, year and score of each movie

# In[13]:


# The title, year and score of each movie are contained in the 'h2' tags


# In[8]:


# choose the first film to get a better idea of how the data is structured - use list indexing to achieve this.


# In[9]:


# Extracting all 'h2' tags


# In[18]:



# The movie title is in the 'a' tag
# The year is in a 'span' with class 'start-year'
# The score is in a 'span' with class 'tMeterScore'


# ## Title

# In[ ]:





# In[10]:


# Obtaining the movie titles from the links


# ## Year

# In[11]:


# Filtering only the spans containing the year


# In[12]:


# Extracting the year string


# ### Removing the brackets

# In[26]:


# Use the strip method to remove the parantheses


# In[13]:


# code for removing parantheses - use the strip method 


# In[14]:


# Updating years with stripped values
# Create a list of all the years 


# In[15]:


# Converting all the strings to integers - use list comprehension to achieve this


# ## Score

# In[17]:


# Extracting the score string


# In[18]:


# Converting each score to an integer


# # Extracting the rest of the information

# ## Critics Consensus

# In[1]:


# The critics consensus is located inside a 'div' tag with the class 'info critics-consensus'
# This can be found inside the original 'div's we scraped

critics_consensus=html_soup.find_all('div',class='info critics-consensus')
print (type()critics_consensus)
print (len()critics_consensus)


# In[3]:





# ### Way #2: Inspecting the HTML

# In[50]:


# When inspecting the HTML we see that the common phrase ("Critics Consensus: ")
# is located inside a span element
# The string we want to obtain follows that


# In[19]:


# We can use .contents to obtain a list of all children of the tag


# In[20]:


# The second element of that list is the text we want


# In[21]:


# We can remove the extra whitespace (space at the beginning) with the .strip() method


# ## Directors

# In[22]:


# Extracting all director divs
directors= [div.find("div", {"class": "descriptors"}) for div in divs]
directors

directors_text = [d.contents[1].strip() for d in directors]
directors_text


# ## Cast info

# In[64]:


# Each cast member's name is the string of a link
# There are multiple cast members for a movie


# In[4]:


cast= [div.find("div", {"class": "info cast"}) for div in divs]

cast[0]

directors_text = [d.contents[1].strip() for d in directors]
directors_text

# Obtain all the links to different cast members


# In[23]:


# Extract the names from the links


# In[24]:


# OPTIONALLY: We can stitch all names together as one string

# This can be done using the join method
# To use join, pick a string to use as a separator (in our case a comma, followed with a space) and
# pass the list of strings you want to merge to the join method

#cast = ", ".join(cast_names)
#cast


# In[68]:


# Now we need to do the above operations for every movie


# ### Using a for loop

# In[5]:


# Initialize the list of all cast memners
#cast = []

# Just put all previous operations inside a for loop



# ## Synopsis

# In[ ]:





# # Representing the data in structured form

# ## Creating a Data Frame

# In[ ]:





# ## Populating the dataframe

# In[6]:


# Populating the dataframe




# ## Exporting the data to CSV (comma-separated values) and excel files

# In[85]:


# Write data to excel file


# In[86]:


# or write data to CSV file


# In[87]:


# Index is set to False so that the index (0,1,2...) of each movie is not saved to the file (the index is purely internal)
# The header is set to True, so that the names of the columns are saved

