
# coding: utf-8

# ## We have the min and max temperatures in a city In India for each months of the year.
# We would like to find a function to describe this and show it graphically, the dataset
# given below.
# Task:
# 1. fitting it to the periodic function
# 2. plot the fit
# Data
# Max = 39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25
# Min = 21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy import interpolate
import pandas as pd


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[65]:


Max =np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
Min =np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])
Min


# In[113]:


month=np.arange(12)
month


# In[5]:


plt.plot(month, Max, 'ro')
plt.plot(month, Min, 'bo')
plt.xlabel('Month')
plt.ylabel('Min and max temperature')


# In[116]:


from scipy import optimize
def yearly_temps(times, avg, ampl, time_offset):
   
    return (avg+ ampl * np.cos((times + time_offset) * 2 * np.pi / times.max()))
res_max, cov_max = optimize.curve_fit(yearly_temps, month,Max)
res_min, cov_min =optimize.curve_fit(yearly_temps, month,Min)


# In[117]:


days = np.linspace(0, 12, num=365)

plt.figure()
plt.plot(month, Max, 'ro')
plt.plot(days, yearly_temps(days, *res_max), 'r-')
plt.plot(month, Min, 'bo')
plt.plot(days, yearly_temps(days, *res_min), 'b-')


# ## This assignment is for visualization using matplotlib:
# data to use:
# url=
# https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.cs
# v
# titanic = pd.read_csv(url)
# Charts to plot:
# 1. Create a pie chart presenting the male/female proportion
# 2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender

# In[3]:


titanic = pd.read_csv('https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv')


# In[4]:


titanic.head()


# In[56]:


sums = titanic.sex.groupby(titanic.sex).count()
explode = (0.1, 0)
plt.pie(sums, explode=explode,labels=sums.index,autopct='%1.1f%%', shadow=True, startangle=90);
plt.legend(sums.index, loc="best")
plt.title('Pie Chart - Male/Female')


# ## 2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender

# In[60]:


gender_color=[]
for elem in titanic.sex:
    if elem=="male":
        gender_color.append("green")
    else:
        gender_color.append("blue")

plt.scatter(x='age',y='fare',c=gender_color,data=titanic,label=gender_color)

