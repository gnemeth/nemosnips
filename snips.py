# -*- coding: utf-8 -*-
"""
Datacamp doodles
"""

import numpy as np
import pandas as pd

def logical_practice():
    my_house = np.array([18.0, 20.0, 10.75, 9.50])
    your_house = np.array([14.0, 24.0, 14.25, 9.0])

    #"logical and/or" enables boolean operations on arrays
    print(np.logical_and(my_house<11, your_house<11)) 
    print(np.logical_or(my_house<10, your_house>11)) 
    
def control_flow():
        
    area = 18
    
    if area > 20:
        print('large!')
    elif area > 15:
        print('medium!')
    else:
        print('small.')
        
def filtering_in_pandas():
    
    
    # isolate elements from the DataFrame where drives_right column is true
    dr = carinfo['drives_right'] == True
    
    #select the whole observations from the DataFrame where drives right is true
    selection = carinfo[dr]
    
    #one-liner version
    cars[cars['drives_right'] == True]
    
    #slicing with numbers/variables 
    #Idea: we could use cpc as a passthrough
    
    cpc = cars['cars_per_cap']
    many_cars = cpc>500
    car_maniac = cars[many_cars]
    
    #using numpy logical operators
    cpc = cars['cars_per_cap']
    between = np.logical_and(cpc > 100, cpc < 500)
    medium = cars[between]