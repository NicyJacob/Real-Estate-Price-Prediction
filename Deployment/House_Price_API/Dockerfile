FROM python:3.7

WORKDIR /app

COPY . /app/

RUN pip3 install --upgrade pip
RUN pip3 install joblib
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install Flask
RUN pip3 install scikit-learn

CMD [ "python3", "app_price.py"]

