

# # **TikTok Project**
# **Course 3 mock role as a Data Analyst at the company Tiktok
# # **Course 3 End-of-course project: Exploratory data analysis**
# 
# 
# **The purpose** of this project is to conduct exploratory data analysis on a provided data set. Your mission is to continue the investigation you began in C2 and perform further EDA on this data with the aim of learning more about the variables. Of particular interest is information related to what distinguishes claim videos from opinion videos.
# 
# **The goal** is to explore the dataset and create visualizations.

# *This activity has 4 parts:*
# 
# **Part 1:** Imports, links, and loading
# 
# **Part 2:** Data Exploration
# *   Data cleaning

# **Part 3:** Build visualizations
# 
# **Part 4:** Evaluate and share results


# <img src="images/Pace.png" width="100" height="100" align=left>
# 
# # **PACE stages**



# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## **PACE: Plan**
# 

# 

# 1.) Identify any outliers:
# What methods are best for identifying outliers?
# ###the best methods for identifying outliers are creating a visual with seaborn, matplotlib or plotly express in python##
# 
# How do you make the decision to keep or exclude outliers from any future models?
# ##you can remove fliers as one of the variables when coding.##

# ### **Task 1. Imports, links, and loading**


# For EDA of the data, import the packages that would be most helpful, such as `pandas`, `numpy`, `matplotlib.pyplot`, and `seaborn`.
# 

# In[1]:


# Import packages for data manipulation

import pandas as pd
import numpy as np

# Import packages for data visualization

from matplotlib import pyplot as plt
import seaborn as sns


# Then, load the dataset into a dataframe. Read in the data and store it as a dataframe object.
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.
# 

# In[2]:


# Load dataset into dataframe
data = pd.read_csv("tiktok_dataset.csv")


# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## **PACE: Analyze**
# 
# Consider the questions in your PACE Strategy Document and those below where applicable to complete your code.

# ### **Task 2a: Data exploration and cleaning**
# 
# The first step is to assess your data. Check the Data Source page on Tableau Public to get a sense of the size, shape and makeup of the data set.
# 



# Display and examine the first few rows of the dataframe

data.head()


# In[4]:


# Get the size of the data

data.size


# In[5]:


# Get the shape of the data

data.shape


# Get basic information about the data, using `.info()`.

# In[6]:


# Get basic information about the data

data.info()


# Generate a table of descriptive statistics, using `.describe()`.

# In[7]:


# Generate a table of descriptive statistics

data.describe()


# In[10]:


data.drop_duplicates(inplace = True)
data.info()


# ### **Task 2b. Assess data types**

# In Tableau, staying on the data source page, double check the data types of the columns in the dataset. Refer to the dimensions and measures in Tableau.
# 

# Review the instructions linked in the previous Activity document to create the required Tableau visualization.

# ### **Task 2c. Select visualization type(s)**

# Select data visualization types that will help you understand and explain the data.
# 
# Now that you know which data columns you’ll use, it is time to decide which data visualization makes the most sense for EDA of the TikTok dataset. What type of data visualization(s) would be most helpful? Consider the distribution of the data.
# 
# * Line graph
# * Bar chart
# * Box plot
# * Histogram
# * Heat map
# * Scatter plot
# * A geographic map
# 

# Bar charts, box plots and histograms make the most sense to understand the data.

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## **PACE: Construct**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Construct stage.

# ### **Task 3. Build visualizations**
# 
# Now that you have assessed your data, it’s time to plot your visualization(s).

# #### **video_duration_sec**
# 
# Create a box plot to examine the spread of values in the `video_duration_sec` column.

# In[4]:


# Create a boxplot to visualize distribution of `video_duration_sec`


data.boxplot(figsize = (5,1) ,
             column = ['video_duration_sec'],
             vert = False)


# Create a histogram of the values in the `video_duration_sec` column to further explore the distribution of this variable.

# In[13]:


# Create a histogram

sns.histplot(data, x = "video_duration_sec")


# **Question:** What do you notice about the duration and distribution of the videos?
# 
# I have noticed that the videos are between about five seconds long and are no longer than 60 seconds, while most of the videos are either the full 60 seconds, 45 seconds, 25 seconds or about three seconds long.

# #### **video_view_count**
# 
# Create a box plot to examine the spread of values in the `video_view_count` column.

# In[14]:


# Create a boxplot to visualize distribution of `video_view_count`

plt.figure(figsize=(5, 1))

box = sns.boxplot(x = data['video_view_count'])

plt.title('Tiktok video duration Boxplot')


# Create a histogram of the values in the `video_view_count` column to further explore the distribution of this variable.

# In[7]:


# Create a histogram

plt.hist(data['video_duration_sec'], bins = range(0,71, 5))
plt.xticks(range(0, 71, 5))
plt.yticks(range(0, 2001, 200))
plt.xlabel('video duration')
plt.ylabel('count')
plt.title('Histogram of Tiktok videos duration')
plt.show();


# **Question:** What do you notice about the distribution of this variable?
# The distributon of variables are pretty level across the board.

# #### **video_like_count**
# 
# Create a box plot to examine the spread of values in the `video_like_count` column.

# In[3]:


#Create a box plot for the 'video like count' column

sns.boxplot(x = 'video_like_count', data = data, showfliers = True)


# Create a histogram of the values in the `video_like_count` column to further explore the distribution of this variable.

# In[16]:


# Create a histogram

plt.hist(data['video_like_count'], bins = range(0,325001, 20000))
plt.xticks(range(0, 325001, 20000), rotation=45)
plt.yticks(range(0, 11001, 500))
plt.xlabel('Amount of likes')
plt.ylabel('count')
plt.title('Histogram of Tiktok videos likes')
plt.show();


# **Question:** What do you notice about the distribution of this variable?
# 
# I noticed that there are an overwhelming amount of videos that have anywhere between zero and 20,000 likes.

# #### **video_comment_count**
# 
# Create a box plot to examine the spread of values in the `video_comment_count` column.

# In[4]:


# Create a boxplot to visualize distribution of `video_comment_count`


sns.boxplot(x = 'video_comment_count', data = data, showfliers = True)


# Create a histogram of the values in the `video_comment_count` column to further explore the distribution of this variable.

# In[15]:


# Create a histogram

plt.hist(data['video_comment_count'], bins = range(0,8001, 500))
plt.xticks(range(0, 8001, 500), rotation=45)
plt.yticks(range(0, 17001, 1000))
plt.xlabel('Amount of comments')
plt.ylabel('count')
plt.title('Histogram of Tiktok videos comments')
plt.show();


# **Question:** What do you notice about the distribution of this variable?

# #### **video_share_count**
# 
# Create a box plot to examine the spread of values in the `video_share_count` column.

# In[18]:


# Create a boxplot to visualize distribution of `video_share_count`

sns.boxplot(x = 'video_share_count', data = data, showfliers = False)


# *Create* a histogram of the values in the `video_share_count` column to further explore the distribution of this variable.

# In[35]:


# Create a histogram

plt.hist(data['video_share_count'], bins = range(0,50001, 2500))
plt.xticks(range(0, 50001, 2500), rotation=45)
plt.yticks(range(0, 11001, 1000))
plt.xlabel('Amount of times a video was shared')
plt.ylabel('count')
plt.title('Histogram of Tiktok videos share amount')
plt.show();


# **Question:** What do you notice about the distribution of this variable?
# 
# There is a vast majority of the amount of shares between the numbers of 0 and 5000.

# #### **video_download_count**
# 
# Create a box plot to examine the spread of values in the `video_download_count` column.

# In[6]:


# Create a boxplot to visualize distribution of `video_download_count`

sns.boxplot(x = 'video_download_count', data = data, showfliers = False)


# Create a histogram of the values in the `video_download_count` column to further explore the distribution of this variable.

# In[13]:


# Create a histogram

plt.hist(data['video_download_count'], bins = range(0,9501, 500))
plt.xticks(range(0, 9501, 500), rotation=45)
plt.yticks(range(0, 15001, 2500))
plt.xlabel('How many times a video was downloaded')
plt.ylabel('count')
plt.title('Histogram of Tiktok videos download count')
plt.show();


# **Question:** What do you notice about the distribution of this variable?

# #### **Claim status by verification status**
# 
# Now, create a histogram with four bars: one for each combination of claim status and verification status.

# In[8]:


# Create a histogram

print(data['verified_status'].unique())
print(data['claim_status'].unique())
plt.figure(figsize=(7,4))
sns.histplot(data=data,
             x='claim_status',
             hue='verified_status',
             multiple='dodge',
             shrink=0.4)
plt.title('Claims by verification status histogram');


# **Question:** What do you notice about the number of verified users compared to unverified? And how does that affect their likelihood to post opinions?
# 
# Most of the the tiktok videos were claims by unverified accounts. From this specific graph it you could draw an insight that if you are unverified you will be flagged.

# #### **Claim status by author ban status**
# 
# The previous course used a `groupby()` statement to examine the count of each claim status for each author ban status. Now, use a histogram to communicate the same information.

# In[3]:


# Create a histogram

fig = plt.figure(figsize=(7,4))
sns.histplot(data, x='claim_status', hue='author_ban_status',
             multiple='dodge',
             hue_order=['active', 'under review', 'banned'],
             shrink=0.9,
             palette={'active':'green', 'under review':'orange', 'banned':'red'},
             alpha=0.5)
plt.title('Amount of Claim status videos by author ban status');


# **Question:** What do you notice about the number of active authors compared to banned authors for both claims and opinions?

# #### **Median view counts by ban status**
# 
# Create a bar plot with three bars: one for each author ban status. The height of each bar should correspond with the median number of views for all videos with that author ban status.

# In[4]:


# Create a bar plot


ban_status_counts = data.groupby(['author_ban_status']).median(
    numeric_only=True).reset_index()

fig = plt.figure(figsize=(5,3))
sns.barplot(data=ban_status_counts,
            x='author_ban_status',
            y='video_view_count',
            order=['active', 'under review', 'banned'],
            palette={'active':'green', 'under review':'orange', 'banned':'red'},
            alpha=0.5)
plt.title('Median view count by ban status');


# **Question:** What do you notice about the median view counts for non-active authors compared to that of active authors? Based on that insight, what variable might be a good indicator of claim status?
# 
# I noticed that the median view count for banned acounts is a bit higher than accounts that are under review. Videos that have accounts that are under review are significantly higher than accounts that are active.

# In[14]:


# Calculate the median view count for claim status.

data.groupby('claim_status')['video_view_count'].median()


# #### **Total views by claim status**
# 
# Create a pie graph that depicts the proportions of total views for claim videos and total views for opinion videos.

# In[5]:


# Create a pie graph

fig = plt.figure(figsize=(3,3))
plt.pie(data.groupby('claim_status')['video_view_count'].sum(), labels=['claim', 'opinion'])
plt.title('Total views by video claim status');


# **Question:** What do you notice about the overall view count for claim status?

# ### **Task 4. Determine outliers**
# 
# When building predictive models, the presence of outliers can be problematic. For example, if you were trying to predict the view count of a particular video, videos with extremely high view counts might introduce bias to a model. Also, some outliers might indicate problems with how data was captured or recorded.
# 
# The ultimate objective of the TikTok project is to build a model that predicts whether a video is a claim or opinion. The analysis you've performed indicates that a video's engagement level is strongly correlated with its claim status. There's no reason to believe that any of the values in the TikTok data are erroneously captured, and they align with expectation of how social media works: a very small proportion of videos get super high engagement levels. That's the nature of viral content.
# 
# Nonetheless, it's good practice to get a sense of just how many of your data points could be considered outliers. The definition of an outlier can change based on the details of your project, and it helps to have domain expertise to decide a threshold. You've learned that a common way to determine outliers in a normal distribution is to calculate the interquartile range (IQR) and set a threshold that is 1.5 * IQR above the 3rd quartile.
# 
# In this TikTok dataset, the values for the count variables are not normally distributed. They are heavily skewed to the right. One way of modifying the outlier threshold is by calculating the **median** value for each variable and then adding 1.5 * IQR. This results in a threshold that is, in this case, much lower than it would be if you used the 3rd quartile.
# 
# Write a for loop that iterates over the column names of each count variable. For each iteration:
# 1. Calculate the IQR of the column
# 2. Calculate the median of the column
# 3. Calculate the outlier threshold (median + 1.5 * IQR)
# 4. Calculate the numer of videos with a count in that column that exceeds the outlier threshold
# 5. Print "Number of outliers, {column name}: {outlier count}"
# 
# ```
# Example:
# Number of outliers, video_view_count: ___
# Number of outliers, video_like_count: ___
# Number of outliers, video_share_count: ___
# Number of outliers, video_download_count: ___
# Number of outliers, video_comment_count: ___
# ```

# In[6]:


### YOUR CODE HERE ###

column_names = ['video_view_count',
              'video_like_count',
              'video_share_count',
              'video_download_count',
              'video_comment_count',
               ]
##outlier_thresh is the threshold for outliers right side of q3 iqr
for column in column_names:
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3 - q1
    median = data[column].median()
    outlier_thresh = median + 1.5*iqr

## formula for outliers for tiktok videos
    outlier_count = (data[column] > outlier_thresh).sum()
    print(f'Number of outliers, {column}:', outlier_count)


# #### **Scatterplot**

# In[7]:


# Create a scatterplot of `video_view_count` versus `video_like_count` according to 'claim_status'
### YOUR CODE HERE ###
sns.scatterplot(x=data["video_view_count"], y=data["video_like_count"],
                hue=data["claim_status"], s=10, alpha=0.8)
plt.show()


# In[19]:


# Create a scatterplot of ``video_view_count` versus `video_like_count` for opinions only
### YOUR CODE HERE ###

claim_status_opinion = data[data['claim_status']=='opinion']
sns.scatterplot(x=claim_status_opinion["video_view_count"], y=claim_status_opinion["video_like_count"],
                 s=10, alpha=.3)
plt.show()


# You can do a scatterplot in Tableau Public as well, which can be easier to manipulate and present. If you'd like step by step instructions, you can review the instructions linked in the previous Activity page.

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## **PACE: Execute**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Execute stage.

# ### **Task 5a. Results and evaluation**
# 
# Having built visualizations in Tableau and in Python, what have you learned about the dataset? What other questions have your visualizations uncovered that you should pursue?
# 
# ***Pro tip:*** Put yourself in your client's perspective, what would they want to know?
# 
# Use the following code cells to pursue any additional EDA. Also use the space to make sure your visualizations are clean, easily understandable, and accessible.
# 
# ***Ask yourself:*** Did you consider color, contrast, emphasis, and labeling?
# 

# 
# I have learned that there are two main types of videos. There is the type of video that has gone viral that either has the ban status of the author as 'banned' or 'under review' whilst the video has gone viral and the video is striked as a 'claim'. There also is a flip side to that coin that where the video is flagged as an 'opinion' and the author ban status is 'Active', the video is also very low numerically for the like count, download count, view count, so on and so forth.
# 
# My other questions are what type of content is going viral? Is it mostly funny content? Violence related? Or does it have a political view point that is contriversal? Who is the intended audience? Does the creator have a small following or are they an influencer?
# 
# My client would likely want to know a few more details and or analytics of the videos/authors.
# 
# 

# ### **Task 5b. Conclusion**
# *Make it professional and presentable*
# 
# You have visualized the data you need to share with the director now. Remember, the goal of a data visualization is for an audience member to glean the information on the chart in mere seconds.
# 
# *Questions to ask yourself for reflection:*
# Why is it important to conduct Exploratory Data Analysis? What other visuals could you create?
# 

# EDA is important because you need to make sure the data is squeeky clean without errors, nulls, Nans, duplicates. Also it is important becuase you can draw insights that you might not have yet actualized until you see the data visually.
# 
# 
# 
# Visualizations helped me understand outliers and how they play a role in the scope of data. They also help me see the 'whole' picture and give me a different perspective on how to interpret it.
# 

# You’ve now completed a professional data visualization according to a business need. Well done! Be sure to save your work as a reference for later work in Tableau.

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
