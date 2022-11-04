FROM python:3.7
EXPOSE 5000

WORKDIR /home/becode/Desktop/becode_projects/Real-Estate-Price-Prediction/Deployment

RUN pip3 install joblib
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install Flask
RUN pip3 install scikit-learn

COPY prediction.py ./prediction.py
COPY app_price.py ./app_price.py

COPY avg_sal_zipcodes.csv ./avg_sal_zipcodes.csv
COPY finalized_scaler.sav ./finalized_scaler.sav
COPY finalized_model.sav ./finalized_model.sav


