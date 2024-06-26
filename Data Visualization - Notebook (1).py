#!/usr/bin/env python
# coding: utf-8

# 1. **[Plots using Matplotlib ](#matplotlib)**
# 2. **[Plots using Seaborn ](#seaborn)**
# 

# #### Import the required libraries  

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# to suppress warnings
import warnings
warnings.filterwarnings('ignore')


# Seaborn library provides a variety of datasets. Plot different visualization plots using various libraries for the 'tips' dataset. 

# In[2]:


# load the 'tips' dataset from seaborn
tips_data = sns.load_dataset('tips')

# display head() of the dataset
tips_data.head()


# <a name="matplotlib"> </a>
# ## 1. Plots using Matplotlib
# <table align="left">
#     <tr>
#         <td>    <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b> 
#                     </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# <a id="list"> </a>
# ### 1.1 Line Plot
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>
#                     </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[3]:


# data
import numpy as np
X = np.linspace(1,20,100)
Y = np.exp(X)

# line plot
plt.plot(X,Y)

# display the plot
plt.show()


# From the plot, it can be observed that as 'X' is increasing there is an exponential increase in Y.

# **The above plot can be represented not only by a solid line, but also a dotted line with varied thickness. The points can be marked explicitly using any symbol.**

# In[4]:


# data
X = np.linspace(1,20,100)
Y = np.exp(X)

# line plot
# the argument 'r*' plots each point as a red '*' 
plt.plot(X,Y, 'r*')

# display the plot
plt.show()


# We can change the colors or shapes of the data points.
# 
# There can be multiple line plots in one plot. Let's plot three plots together in a single graph. Also, add a plot title.

# In[5]:


# data
X = np.linspace(1,20,100)
Y1 = X
Y2 = np.square(X)
Y3 = np.sqrt(X)

# line plot
plt.plot(X,Y1,'r', X,Y2,'b', X,Y3,'g')

# add title to the plot
plt.title('Line Plot')

# display the plot
plt.show()


# <a id="list"> </a>
# ### 1.2 Scatter Plot
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>
#                     </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[6]:


# check the head() of the tips dataset
tips_data.head()


# Plot the scatter plot for the variables 'total_bill' and 'tip'.

# In[7]:


# data
X = tips_data['total_bill']
Y = tips_data['tip']

# plot the scatter plot
plt.scatter(X,Y)

# add the axes labels to the plot
plt.xlabel('total_bill')
plt.ylabel('tip')

# display the plot
plt.show()


# We can add different colors, opacity, and shapes to data points. Let's add these customizations to the above plot.

# In[8]:


# plot the scatter plot for the variables 'total_bill' and 'tip'

X = tips_data['total_bill']
Y = tips_data['tip']

# plot the scatter plot
# s is for shape, c is for colour, alpha is for opacity (0 < alpha < 1)
plt.scatter(X, Y, s = np.array(Y)**2, c= 'green', alpha= 0.8)

# add title 
plt.title('Scatter Plot')

# add the axes labels to the plot
plt.xlabel('total_bill')
plt.ylabel('tip')

# display the plot
plt.show()


# The bubbles with greater radius display that the tip amount is more as compared to the bubbles with less radius.

# <a id="list"> </a>
# ### 1.3 Bar Plot
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>
#                     </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[9]:


# check the head() of the tips dataset
tips_data.head()


# In[10]:


# the variable 'smoker' is categorical
# check categories in the variable
set(tips_data['smoker'])


# In[11]:


# bar plot to get the count of smokers and non-smokers in the data

# kind='bar' plots a bar plot
# 'rot = 0' returns the categoric labels horizontally
tips_data.smoker.value_counts().plot(kind='bar', rot = 0)

# display the plot
plt.show()


# In[12]:


tips_data.smoker.value_counts()[1]+1


# Let's add the count of smokers and non-smokers, axes labels and title to the above plot.

# In[13]:


# bar plot to get the count of smokers and non-smokers in the data

# kind='bar' plots a bar plot
# 'rot = 0' returns the categoric labels horizontally
# 'color' can be used to add a specific colour
tips_data.smoker.value_counts().plot(kind='bar', rot = 0, color = 'green')

# plt.text() adds the text to the plot
# x and y are positions on the axes
# s is the text to be added
plt.text(x = -0.05, y = tips_data.smoker.value_counts()[0]+1, s = tips_data.smoker.value_counts()[0])
plt.text(x = 0.98, y = tips_data.smoker.value_counts()[1]+1, s = tips_data.smoker.value_counts()[1])

# add title and axes labels
plt.title('Bar Plot')
plt.xlabel('Smoker')
plt.ylabel('Count')

# display the plot
plt.show()


# From the bar plot, it can be interpreted that the proportion of non-smokers is more in the data.

# <a id="list"> </a>
# ### 1.4 Pie Plot
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>
# </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[14]:


# check the head() of the tips dataset
tips_data.head()


# In[15]:


# categories in the 'day' variable
tips_data.day.value_counts()


# In[16]:


# plot the occurrence of different days in the dataset

# 'autopct' displays the percentage upto 1 decimal place
# 'radius' sets the radius of the pie plot
plt.pie(tips_data.day.value_counts(), autopct = '%.1f%%', radius = 1.2, labels = ['Sat', 'Sun','Thur','Fri'])

# display the plot
plt.show()


# From the above pie plot, it can be seen that the data has a high proportion for Saturday followed by Sunday.

# **Exploded pie plot** is a plot in which one or more sectors are separated from the disc.

# In[17]:


# plot the occurrence of different days in the dataset

# exploded pie plot
plt.pie(tips_data.day.value_counts(), autopct = '%.1f%%', radius = 1.2, labels = ['Sat', 'Sun','Thur','Fri'],
        explode = [0,0,0,0.5])

# display the plot
plt.show()


# **Donut pie plot** is a type of pie plot in which there is a hollow center representing a doughnut.

# In[18]:


# plot the occurrence of different days in the dataset

# pie plot
plt.pie(tips_data.day.value_counts(), autopct = '%.1f%%', radius = 1.2, labels = ['Sat', 'Sun','Thur','Fri'])

# add a circle at the center
circle =  plt.Circle( (0,0), 0.5, color='white')
plot = plt.gcf()
plot.gca().add_artist(circle)
 
# display the plot
plt.show()


# <a id="list"> </a>
# ### 1.5 Histogram
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b></b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[19]:


# check the head() of the tips dataset
tips_data.head()


# In tips dataset, 'tip' is the continuous variable. Let's plot the histogram to understand the distribution of the variable.

# In[20]:


# plot the histogram
# specify the number of bins, using 'bins' parameter
plt.hist(tips_data['tip'], bins= 5)

# add the graph title and axes labels
plt.title('Distribution of tip amount')
plt.xlabel('tip')
plt.ylabel('Frequency')

# display the plot
plt.show()


# From the above plot, we can see that the tip amount is positively skewed. 

# <a id="list"> </a>
# ### 1.6 Box Plot
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b></b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[21]:


# check the head() of the tips dataset
tips_data.head()


# Plot the boxplot of 'total_bill' to check the distribution and presence of outliers in the variable.

# In[22]:


# plot a distribution of total bill
plt.boxplot(tips_data['total_bill'])

# add labels for five number summary
plt.text(x = 1.1, y = tips_data['total_bill'].min(), s ='min')
plt.text(x = 1.1, y = tips_data.total_bill.quantile(0.25), s ='Q1')
plt.text(x = 1.1, y = tips_data['total_bill'].median(), s ='meadian (Q2)')
plt.text(x = 1.1, y = tips_data.total_bill.quantile(0.75), s ='Q3')
plt.text(x = 1.1, y = tips_data['total_bill'].max(), s ='max')


# add the graph title and axes labels
plt.title('Boxplot of Total Bill Amount')
plt.ylabel('Total bill')

# display the plot
plt.show()


# The above boxplot clearly shows the presence of outliers above the horizontal line. We can add an arrow to showcase the outliers. Also, the median (Q2) is represented by the orange line, which is near to Q1 rather than Q3. This shows that the total bill is positively skewed.

# In[23]:


# plot a distribution of total bill
plt.boxplot(tips_data['total_bill'])

# add labels for five number summary
plt.text(x = 1.1, y = tips_data['total_bill'].min(), s ='min')
plt.text(x = 1.1, y = tips_data.total_bill.quantile(0.25), s ='Q1')
plt.text(x = 1.1, y = tips_data['total_bill'].median(), s ='meadian (Q2)')
plt.text(x = 1.1, y = tips_data.total_bill.quantile(0.75), s ='Q3')
plt.text(x = 1.1, y = tips_data['total_bill'].max(), s ='max')

# add an arrow (annonate) to show the outliers
plt.annotate('Outliers', xy = (0.97,45),xytext=(0.7, 44), arrowprops = dict(facecolor='black', arrowstyle = 'simple'))

# add the graph title and axes labels
plt.title('Boxplot of Total Bill Amount')
plt.ylabel('Total bill')

# display the plot
plt.show()


# <a name="seaborn"> </a>
# ## 2. Plots using Seaborn
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>
#                     </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>

# <a id="list"> </a>
# ### 2.1 Strip Plot
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b> </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[24]:


# check the head() of the tips dataset
tips_data.head()


# Plot a strip plot to check the relationship between the variables 'tip' and 'time'

# In[25]:


# strip plot
sns.stripplot(y = 'tip', x = 'time', data = tips_data)

# display the plot
plt.show()


# It can be seen that the tip amount is more at dinner time than at lunchtime. But the above plot is unable to display the spread of the data. We can plot the points with spread using the 'jitter' parameter in the stripplot function.

# In[26]:


# strip plot with jitter to spread the points
sns.stripplot(y = 'tip', x = 'time', data = tips_data, jitter = True)

# display the plot
plt.show()


# The plot shows that for most of the observations the tip amount is in the range 1 to 3 irrespective of the time. 

# <a id="list"> </a>
# ### 2.2 Swarm Plot
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>  </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[27]:


# check the head() of the tips dataset
tips_data.head()


# Plot the swarm plot for the variables 'tip' and 'time'. 

# In[28]:


# swarm plot
sns.swarmplot(y = 'tip', x = 'time', data = tips_data)

# display the plot
plt.show()


# The above plot gives a good representation of the tip amount for the time. It can be seen that the tip amount is 2 for most of the observations. We can see that the swarm plot gives a better understanding of the variables than the strip plot.  
# 
# 
# We can add another categorical variable in the above plot by using the parameter 'hue'. 

# In[29]:


# swarm plot with one more categorical variable 'day'
sns.swarmplot(y = 'tip', x = 'time', data = tips_data, hue = 'day')

# display the plot
plt.show()


# The plot shows that the tip was collected at lunchtime only on Thursday and Friday. The amount of tips collected at dinner time on Saturday is the highest.

# <a id="list"> </a>
# ### 2.3 Violin Plot
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b></b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[30]:


# check the head() of the tips dataset
tips_data.head()


# Let's draw a violin plot for the numerical variable 'total_bill' and a categorical variable 'day'.

# In[31]:


# violin plot
sns.violinplot(y = 'total_bill', x = 'day', data = tips_data)

# display the plot
plt.show()


# The above violin plot shows that the total bill distribution is nearly the same for different days. We can add another categorical variable 'sex' to the above plot to get an insight into the bill amount distribution based on days as well as gender.

# In[32]:


# set the figure size
plt.figure(figsize = (8,5))

# violin plot with addition of the variable 'sex'  
# 'split = True' draws half plot for each of the category of 'sex' 
sns.violinplot(y = 'total_bill', x = 'day', data = tips_data, hue = 'sex', split = True)

# display the plot
plt.show()


# There is no significant difference in the distribution of bill amount and sex.

# <a id="list"> </a>
# ### 2.4 Pair Plot
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[33]:


# check the head() of the tips dataset
tips_data.head()


# Plot a pair plot for the tips dataset.

# In[34]:


# set the figure size
plt.figure(figsize = (8,8))

# plot a pair plot
sns.pairplot(tips_data)

# display the plot
plt.show()


# The above plot shows the relationship between all the numerical variables. 'total_bill' and 'tip' has a positive linear relationship with each other. Also, 'total_bill' and 'tip' are positively skewed. 'size' has a significant impact on the 'total_bill', as the minimum bill amount is increasing with an increasing number of customers (size).

# <a id="list"> </a>
# ### 2.5 Distribution Plot
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>
#  </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[35]:


# check the head() of the tips dataset
tips_data.head()


# Lets plot a distribution plot of 'total_bill'.

# In[36]:


# plot a distribution plot
sns.displot(tips_data['total_bill'], kind='kde')

# display the plot
plt.show()


# We can interpret from the above plot that the total bill amount is between the range 10 to 20 for a large number of observations. The distribution plot can be used to visualize the total bill for different times of the day. We can use the hue parameter to visualize the total bill with respect to time.

# In[37]:


# # iterate the distplot() function over the time

# # list of time
time = ['Lunch', 'Dinner']

# # iterate through time
for i in time:
    subset = tips_data[tips_data['time'] == i]
    
# # Draw the density plot`
# # 'hist = False' will not plot a histogram
# # 'kde = True' plots density curve
    sns.distplot(subset['total_bill'], hist = False, kde = True,
                  kde_kws = {'shade':True},
                  label = i)


# It can be seen that the distribution plot for lunch is more right-skewed than a plot for dinner. This implies that the customers are spending more on dinner rather than lunch. 

# <a id="list"> </a>
# ### 2.6 Count Plot
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[38]:


# check the head() of the tips dataset
tips_data.head()


# Let us plot the count of observations for each day based on time.

# In[39]:


# count of observations for each day based on time
# set 'time' as hue parameter
sns.countplot(data = tips_data, x = 'day', hue = 'time')

# display the plot
plt.show()


# All the observations recorded on Saturday and Sunday are for dinner. Observations for lunch on Thursday is highest among lunchtime.

# <a id="list"> </a>
# ### 2.7 Heatmap
# <table align="left">
#     <tr>
#         <td>
#             <div align="left", style="font-size:120%">
#                 <font color="#21618C">
#                     <b>  </b>
#                 </font>
#             </div>
#         </td>
#     </tr>
# </table>
# 
# 

# In[40]:


# check the head() of the tips dataset
tips_data.head()


# Compute correlation between the variables using .corr() function. Plot a heatmap of the correlation matrix.

# In[41]:


# compute correlation
corr_matrix = tips_data.corr()

corr_matrix


# In[42]:


# plot heatmap
# 'annot=True' returns the correlation values 
sns.heatmap(corr_matrix, annot = True)

# display the plot
plt.show()


# The above plot shows that there is a moderate correlation between 'total_bill' and 'tip' (0.68). The diagonal values are '1' as it is the correlation of the variable with itself.

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# to suppress warnings
import warnings
warnings.filterwarnings('ignore')


# In[5]:


data = pd.read_csv('C:\\Users\\anthony\\Downloads\\prog_book.csv')


# In[6]:


data


# In[8]:


plt.hist(data['Price'], bins= 10)


# In[9]:


sns.countplot(data = data, x = 'Type')

# display the plot
plt.show()


# In[10]:


# strip plot
sns.stripplot(y = 'Rating', x = 'Type', data = data)

# display the plot
plt.show()


# In[11]:


# plot a distribution of total bill
plt.boxplot(data['Rating'])


# display the plot
plt.show()


# In[12]:


# plot a distribution plot
sns.displot(data['Reviews'], kind='kde')

# display the plot
plt.show()


# In[13]:


# plot heatmap
# 'annot=True' returns the correlation values 
sns.heatmap(data.corr(), annot = True)

# display the plot
plt.show()


# In[14]:


data.Type.value_counts()


# In[15]:


plt.pie(data.Type.value_counts(), autopct = '%.1f%%', radius = 1.2, labels = ['Paperback', 'Hardcover','Kindle Edition','ebook','Unknown Binding','Boxed Set - Hardcover'])

# display the plot
plt.show()


# In[ ]:




