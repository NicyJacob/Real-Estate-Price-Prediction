# Real-Estate-Price-Prediction
To create a Machine Learning model to make price predictions on real estate sales in Belgium.

# Description
The project is divided into 4 major phases namely, Data Collection, Data Analysis, Training & Evaluation and lastly API Deployment.

  Data Acquisition - This phase includes data scraping from the website of a real estate company in Belgium. The data is converted to a csv file using pandas dataframe. This csv file is used as input for the Data Analysis phase.The performance of this code can be improved by using sitemaps.
  
  Data Analysis - This phase includes the pre-processing of data. The data is cleaned for duplicates, blank spaces and empty values. The data scraped consisted of mainly categorical data. This data is label encoded to convert it to discrete datavalues. The correlation between the price and categorical data is calculated. Also the median value of the price was compared to the different categories.The plots and analysis is saved in graphs.ipynb in the data folder.
  
  Training & Evaluation - Data pre_processing is done in the analysis phase. Data is again checked to ensure no duplicates, no NaNs, no text data. The features with a strong correlation with price is selected. The continuous variables is normalised. The dataset is split into training and test set. Regression algorithms is used to train machine learning models. The models used are Polynomial Regresion, Random Forest Regression and Gradient Boost Regression. The error values considered for model evaluation are root-mean-square error (RMSE), Root Mean Squared Log Error(RLMSE) and r square. Based on the metrics, Gradient Boosting Regression is finally used to train the machine learning model.
  
  Deployment - The final model is deployed locally using API and Docker. Render is used to deploy the prediction on web service. The final files is stored in House_Price_API folder. The model is available on https://house-price.onrender.com/


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
  7. Docker
  
