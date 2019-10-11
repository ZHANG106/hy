# 介绍

一个关于天气数据的数据清洗和分析作业

## Aim 
The aim of this assignment is to investigate and visualise data using Python as a data science tool. It will test your ability to: 
1. read a data file in Python and extract related data from it; 
2. use various graphical and non-graphical tools to perform data exploration, data wrangling and data analysis; 
3. use basic tools for managing and processing data; and 
4. communicate your findings in your report. 

## Data 
The dataset we will use comes from the TAO (Tropical Atmosphere Ocean) project, by the Pacific Marine Environmental Lab of the U.S. National Oceanic and Atmospheric Administration. This monitors the atmosphere in the tropical Pacific Ocean. 
> The Tropical Atmosphere Ocean dataset we chose (TAO_2006.csv file) contains atmosphere data from a specific monitoring site: (2◦N,165◦E). 
> We chose to investigate environment data from January until September 2006, where the measurements were taken every 10 minutes. 
> The dataset contains information about Timestamp, date (YYYYMMDD) and time (HHMMSS) of measurements, Precipitation (PREC), Air Temperature (AIRT), Sea Surface Temperature (SST), Relative Humidity (RH), and the Quality (Q) of measurements. 
> The file is available on Moodle and is publicly available from pmel.noaa.gov. 


## Supportive Material/Code: 
• Material: In order to complete your assignment, you may want to use regressiondemo.py code used in week 5 tutorial. If you use this code, you do not need to upload the regressiondemo.py file it in your final submission. 

• Code: If "YYYYMMDD" is in datetime format, you can extract year, month and day from it using method .dt and create a new column for year, month and day as follows: 

~~~python
>>> your_dataframe['Month']=your_dataframe['YYYYMMDD'].dt.year
>>> your_dataframe['Month']=your_dataframe['YYYYMMDD'].dt.month 
>>> your_dataframe['Month']=your_dataframe['YYYYMMDD'].dt.day 
~~~

## Task A: Data Wrangling and Analysis on TAO dataset 
In this task, you are required to explore the dataset and do some data analysis on the Tropical Atmosphere Ocean dataset. Have a look at the csv file (TAO_2006.csv) and then answer a series of questions about the data using Python. 
### A1. Dataset size 
How many rows and columns exist in this dataset? 
### A2. Min/Max values in each column 
Find maximum and minimum values for Precipitation (PREC), Air temperature (AT), Sea surface temperature (SST) and Relative humidity (RH) in this dataset. 
### A3. Number of records in each month 
List the number of records in each month. In which two months are the number of records at their lowest? Why? 
### A4. Missing values 
There are some missing values: -9.990000 and -99.900000 represent missing values. 
1. How many rows contain missing values (-9.990000 or -99.900000) in this dataset? 
2. List the months with no missing values in them. 
3. Remove the records with missing values. 

> Note: Use the dataset with missing values removed from here onwards. 
### A5. Investigating Sea surface temperature (SST) in different months 
Now look at the sea surface temperature (SST) column and answer the following questions 
1. Using a boxplot, visualize the distribution of SST over different months. 
2. Describe the trend of median SST over different months. 
3. Which month has the highest median SST? Which month has the lowest? 

### A6. Exploring precipitation measurements (PREC) 
Now look at the Precipitation column and answer the following questions 
1. Precipitation values in this dataset show rain rates. Plot Precipitation values over different timestamps. 
2. Due to measurement error, there are some counter-intuitive values in Precipitation column. Identify those values and replace them with zero. 

> Note: Use the dataset from previous task (Task A6) and complete Tasks, A7-A9. 
### A7. Relationship between variables 
1. Compute pairwise correlation of columns, precipitation, air temperature and surface temperature. Which two features have the least linear association? 
2. Now let's look at the relationship between air temperature and relative humidity. Plot the values of these features against each other. Is there any relationship between these two features? Describe it. 

### A8. Predicting quality of measurements (Q) 
We now want to build a predictive model to predict the quality of measurements (Q) in the dataset based on four features: Precipitation (PREC), Air temperature (AIRT), Sea surface temperature (SST) and Relative humidity (RH). 
1. Divide the dataset into a 75% training set and a 25% testing set and train a decision tree model. 
2. Using test set, compute the confusion matrix and accuracy. 
3. Considering accuracy only, do you think that this is a good model? What other metric(s) should we consider as well? Why? Elaborate your answer. 

### A9. Investigating daily relative humidity (RH) 
We will now investigate the trend in the daily relative humidity over time. For this, you will need to aggregate the median relative humidity by day. 
1. Fit a linear regression using Python to this data (i.e., relative humidity over different days) and plot the linear fit. 
2. Use the linear fit to predict median relative humidity on 2nd September 2006. 
3. Can you think of a better model that fits all of the aggregated data to capture the trend in relative humidity over time? Describe the model you suggested and explain why it is better suited for this task. 
4. Use your new model to predict median relative humidity on 2nd September 2006 and compare with the prediction of your previous linear fit. 

### A10. Filling in missing values 
Rather than removing the missing values in task A4, fill in the missing values (for column, RH only) using an appropriate regression model. 