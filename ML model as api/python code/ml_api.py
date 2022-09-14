# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:37:46 2022

@author: ShubhangiL
"""

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import json


app = FastAPI()

class model_input(BaseModel):
    
    Unnamed_0 : int
    i  : int
    Gender : int
    Customer_Type : int
    Age : int
    Type_of_Travel : int
    Class: int
    Flight_Distance : int
    Inflight_wifi_service : int
    Departure_Arrival_time_convenient : int
    Ease_of_Online_booking : int
    Gate_location : int
    Food_and_drink : int
    Online_boarding : int
    Seat_comfort : int
    Inflight_entertainment : int
    On_board_service : int
    Leg_room_service : int
    Baggage_handling : int
    Checkin_service : int
    Inflight_service : int
    Cleanliness : int
    Departure_Delay_in_Minutes : int
        
# loading the saved model
customer_model = joblib.load('model_joblib1')[-1]
print(customer_model)


#create our api
@app.post('/customer_prediction')
def customer_pred(input_dictionary : model_input):
    
    #input_data = input_parameters.json()
    #input_dictionary = json.loads(input_data)
    print(input_dictionary)
    
    X1 = input_dictionary.Unnamed_0
    X2 = input_dictionary.i
    X3 = input_dictionary.Gender
    X4 = input_dictionary.Customer_Type
    X5 = input_dictionary.Age
    X6 = input_dictionary.Type_of_Travel
    X7 = input_dictionary.Class
    X8 = input_dictionary.Flight_Distance
    X9 = input_dictionary.Inflight_wifi_service
    X10 = input_dictionary.Departure_Arrival_time_convenient
    X11 = input_dictionary.Ease_of_Online_booking
    X12 = input_dictionary.Gate_location
    X13 = input_dictionary.Food_and_drink
    X14 = input_dictionary.Online_boarding
    X15 = input_dictionary.Seat_comfort
    X16 = input_dictionary.Inflight_entertainment
    X17 = input_dictionary.On_board_service
    X18 = input_dictionary.Leg_room_service
    X19 = input_dictionary.Baggage_handling
    X20 = input_dictionary.Checkin_service
    X21 = input_dictionary.Inflight_service
    X22 = input_dictionary.Cleanliness
    X23 = input_dictionary.Departure_Delay_in_Minutes   
    
    input_list = [ X2, X3, X4, X5, X6, X7, X8, X9, X10, X11, X12, X13, X14, X15, X16, X17, X18, X19, X20, X21, X22, X23]
    print(input_list)    
    prediction = customer_model.predict([input_list])
    print(prediction)
    
    
    if (prediction[0] == 0):
        return 'The person is not satisfied'
    else:
        return 'The person is satisfied'    