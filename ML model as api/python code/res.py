#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
import requests
cus={"Unnamed_0": 0 ,"i":70172 ,"Gender": 1,"Customer_Type":1 ,"Age":23,"Type_of_Travel":1,"Class":1, "Flight_Distance": 2223,"Inflight_wifi_service":1,"Departure_Arrival_time_convenient":1,"Ease_of_Online_booking":1, "Gate_location":1, "Food_and_drink":1,"Online_boarding":1,"Seat_comfort":1 ,"Inflight_entertainment" :1 ,"On_board_service":1, "Leg_room_service":1,"Baggage_handling":1, "Checkin_service":1,"Inflight_service":1,"Cleanliness":1,"Departure_Delay_in_Minutes":1}


res = requests.post("http://localhost:8000/customer_prediction", json = cus)

print(res)

print(res.json())


# In[ ]:




