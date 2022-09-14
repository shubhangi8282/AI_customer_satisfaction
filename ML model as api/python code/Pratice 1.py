#!/usr/bin/env python
# coding: utf-8

# In[1]:


# String variable
x = "hello"
print (x)
print (type(x))


# In[2]:


# int variable
x = 5
print (x, type(x))


# In[3]:


# float variable
x = 5.0
print (x, type(x))


# In[4]:


# text variable
x = "5"
print (x, type(x))


# In[5]:


a = 1
b = 2
c = a + b
print (c)


# In[6]:


# Creating a list
x = [3, "hello", 1.2]
print (x)


# In[7]:



# Adding to a list
x.append(7)
print (x)
print (len(x))


# In[8]:


# Replacing items in a list
x[1] = "bye"
print (x)


# In[9]:


# Operations
y = [2.4, "world"]
z = x + y
print (z)


# In[10]:


# Creating a tuple
x = (3.0, "hello") # tuples start and end with ()
print (x)


# In[11]:


# Adding values to a tuple
x = x + (5.6, 4)
print (x)


# In[12]:


# Sets
text = "Learn ML with Made With ML"
print (set(text))
print (set(text.split(" ")))


# In[13]:


# Indexing
x = [3, "hello", 1.2]
print ("x[0]: ", x[0])
print ("x[1]: ", x[1])
print ("x[-1]: ", x[-1]) # the last item
print ("x[-2]: ", x[-2]) # the second to last item


# In[14]:


# Slicing
print ("x[:]: ", x[:]) # all indices
print ("x[1:]: ", x[1:]) # index 1 to the end of the list
print ("x[1:2]: ", x[1:2]) # index 1 to index 2 (not including index 2)
print ("x[:-1]: ", x[:-1]) # index 0 to last index (not including last index)


# In[15]:


# Creating a dictionary
person = {"name": "Goku",
          "eye_color": "brown"}
print (person)
print (person["name"])
print (person["eye_color"])


# In[16]:


# Changing the value for a key
person["eye_color"] = "green"
print (person)


# In[17]:


# Adding new key-value pairs
person["age"] = 24
print (person)


# In[18]:


from collections import OrderedDict


# In[19]:


# Native dict
d = {}
d["a"] = 2
d["c"] = 3
d["b"] = 1
print (d)


# In[20]:


# Dictionary items
print (d.items())


# In[21]:


# Order by keys
print (OrderedDict(sorted(d.items())))


# In[22]:


# Order by values
print (OrderedDict(sorted(d.items(), key=lambda x: x[1])))


# In[23]:


# If statement
x = 4
if x < 1:
    score = "low"
elif x <= 4: # elif = else if
    score = "medium"
else:
    score = "high"
print (score)


# In[24]:


# If statement with a boolean
x = True
if x:
    print ("it worked")


# In[25]:


# For loop
veggies = ["carrots", "broccoli", "beans"]
for veggie in veggies:
    print (veggie)


# In[26]:


# `break` from a for loop
veggies = ["carrots", "broccoli", "beans"]
for veggie in veggies:
    if veggie == "broccoli":
        break
    print (veggie)


# In[27]:


# `continue` to the next iteration
veggies = ["carrots", "broccoli", "beans"]
for veggie in veggies:
    if veggie == "broccoli":
        continue
    print (veggie)


# In[28]:


# While loop
x = 3
while x > 0:
    x -= 1 # same as x = x - 1
    print (x)


# In[29]:


# For loop
x = [1, 2, 3, 4, 5]
y = []
for item in x:
    if item > 2:
        y.append(item)
print (y)


# In[30]:


# List comprehension
y = [item for item in x if item > 2]
print (y)


# In[31]:


# Function with multiple inputs
def join_name(first_name, last_name):
    """Combine first name and last name."""
    joined_name = first_name + " " + last_name
    return joined_name


# In[33]:


# Use the function
first_name = "shubhangi"
last_name = "lohitkumar"
joined_name = join_name(
    first_name=first_name, last_name=last_name)
print (joined_name)


# In[34]:


def f(*args, **kwargs):
    x = args[0]
    y = kwargs.get("y")
    print (f"x: {x}, y: {y}")


# In[35]:


f(5, y=2)


# In[36]:


# Creating the class
class Pet(object):
    """Class object for a pet."""

    def __init__(self, species, name):
        """Initialize a Pet."""
        self.species = species
        self.name = name


# In[37]:


# Creating an instance of a class
my_dog = Pet(species="dog",
             name="Scooby")
print (my_dog)
print (my_dog.name)


# In[38]:


# Creating the class
# Creating the class
class Pet(object):
    """Class object for a pet."""

    def __init__(self, species, name):
        """Initialize a Pet."""
        self.species = species
        self.name = name

    def __str__(self):
        """Output when printing an instance of a Pet."""
        return f"{self.species} named {self.name}"


# In[39]:


# Creating an instance of a class
my_dog = Pet(species="dog",
             name="Scooby")
print (my_dog)
print (my_dog.name)


# In[40]:


import numpy as np


# In[41]:


# Set seed for reproducibility
np.random.seed(seed=1234)


# In[42]:


# Scalar
x = np.array(6)
print ("x: ", x)
print ("x ndim: ", x.ndim) # number of dimensions
print ("x shape:", x.shape) # dimensions
print ("x size: ", x.size) # size of elements
print ("x dtype: ", x.dtype) # data type


# In[43]:


# Vector
x = np.array([1.3 , 2.2 , 1.7])
print ("x: ", x)
print ("x ndim: ", x.ndim)
print ("x shape:", x.shape)
print ("x size: ", x.size)
print ("x dtype: ", x.dtype) # notice the float datatype


# In[44]:


# Matrix
x = np.array([[1,2], [3,4]])
print ("x:\n", x)
print ("x ndim: ", x.ndim)
print ("x shape:", x.shape)
print ("x size: ", x.size)
print ("x dtype: ", x.dtype)


# In[45]:


# 3-D Tensor
x = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print ("x:\n", x)
print ("x ndim: ", x.ndim)
print ("x shape:", x.shape)
print ("x size: ", x.size)
print ("x dtype: ", x.dtype)


# In[ ]:




