# Real-Estate-Price-Prediction
To create a Machine Learning model to make price predictions on real estate sales in Belgium.

# Description
The project is divided into 4 major phases namely, Data Collection, Data Analysis, Training & Evaluation and lastly API Deployment.

  Data Collection - This phase includes data scraping from the website of a real estate company in Belgium. The data is converted to a csv file using pandas dataframe. This csv file is used as input for the Data Analysis phase.
  
  Data Analysis - This phase includes the pre-processing of data. The data is cleaned for duplicates, blank spaces and empty values. The data scraped consisted of mainly categorical data. This data is encoded to convert it to discrete datavalues. The correlation between the price and categorical data is calculated. Also the median value of the price was compared to the different categories.
  
  Training & Evaluation - Data pre_processing is done in the analysis phase. Data is again checked to ensure no duplicates, no NaNs, no text data. The features with strong correlation with price were selected. The continuous variables were normalised and the categorical data was encoded using One Hot Encoder. The dataset was split into training and test set. Polynomial Regression and Random Forest Regression were considered as the models for training. The model was trained and evaluated on the performance metrics. The metric selected for the evaluation is r2 square. Mean absolute error(MAE) is calculated to know the error margin.
  

# Installation


# Usage
This project performs web scraping using selenium. You would need to install selenium and the geckodriver to execute the program.
https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium/bin
NB: On Linux, put your geckodriver (the downloaded extension) in the equivalent path on your machine into /home/<YOUR_NAME>/.local/bin/

Data visualisations is done using [plotly](https://plotly.com/python/)

Model training and evaluation is done using Sklearn library.


# Requirements
The following python libraries are used in this program
  1. Requests
  2. BeautifulSoup
  3. Pandas
  4. Plotly
  5. Dython
  6. Sklearn
  
  
# Note
The performance of this code can be improved by using sitemaps.
