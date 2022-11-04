import json
import pandas as pd
import joblib

def preprocess(df):
    #df = pd.DataFrame.from_dict(dict, orient='index')
 
    #label encoding property type
    types = []
    for row in df['property-type']:
        if row == 'APARTMENT' :  
            types.append('1')
        elif row == 'HOUSE':
            types.append('2')
        else:           
            types.append('Error')
    df['types'] = types
    
    #label encoding kitchen type
    encoded_kitchen = []
    for row in df['equipped-kitchen']:
        if row == True :  
            encoded_kitchen.append('4')
        elif row == False:        
            encoded_kitchen.append('2')
        else:
            encoded_kitchen.append('Error')
    df['encoded_kitchen'] = encoded_kitchen
    
    #merging for average salary of the zipcode
    df_avg_sal = pd.read_csv('/home/becode/Desktop/becode_projects/Real-Estate-Price-Prediction/Deployment/avg_sal_zipcodes.csv')
    df1 = pd.merge(df, df_avg_sal, on ="zip-code", how ='left')

    #renaming columns to suit the model train data
    df1.columns = df1.columns.str.replace('area', 'classified_land_surface')
    df1.columns = df1.columns.str.replace('rooms-number', 'classified_bedroom_count')

    #Building the dataframe with selected features
    data = df1[['classified_land_surface','types',
               'classified_bedroom_count','encoded_kitchen',
               'avg_sal_zip_code']].copy()
    
    #error_msg
    return(data)


def predict(df):
    data = preprocess(df)
    
    #Using the scaler from the model
    filename = '/home/becode/Desktop/becode_projects/Real-Estate-Price-Prediction/Deployment/finalized_scaler.sav'
    scaler = joblib.load(filename)
    data_scaled = scaler.transform(data)
    
    #Applying the model
    filename1 = '/home/becode/Desktop/becode_projects/Real-Estate-Price-Prediction/Deployment/finalized_model.sav'
    model = joblib.load(filename1)
    prediction = model.predict(data_scaled)
    return(prediction)


#getting the input data
dict1 = {"data": {
    "area":100, 
    "property-type": "APARTMENT", 
    "rooms-number": 3, 
    "zip-code": 9000, 
    "equipped-kitchen": True,
    "land-area": 400, #Not used
    "garden": False, #Not used
    "garden-area": 20, #Not used
    "full-address": "ABCDEF", #Not used
    "swimming-pool": False, #Not used
    "furnished": True, #Not used
    "open-fire": False, #Not used
    "terrace": False, #Not used
    "terrace-area": 10, #Not used
    "facades-number": 3, #Not used
    "building-state": "GOOD" #Not used
    }
    }
with open("data.json", "w") as outfile:
    json.dump(dict1, outfile)
with open("data.json") as infile:
    dict = json.load(infile)
df = pd.DataFrame.from_dict(dict, orient='index')
#print(df)
#predicting the price using the model
x = predict(df)
#print(f" The price is {x.round(2)} euros")

