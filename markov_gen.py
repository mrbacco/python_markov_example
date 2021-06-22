# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 12:29:36 2020

@author: mrbacco 2021
"""

import numpy as np
import random as rm
import time
from datetime import datetime

# The statespace
states = ["Bike","Sailing","Run"]
sentence = ["Subject", "Verb", "Object"]

# Possible sequences of events
transitionName = [["SS","SR","SI"],["RS","RR","RI"],["IS","IR","II"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

# checking consistency of transition matrix
if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[1]) != 3:
    print("Somewhere, something went wrong. Transition matrix, perhaps?")
else: print("All is gonna be okay mrbacco, you should move on!! ;)")

x = 3
while x >=0:
    num1 = rm.randrange(0,3) # picking a number randomly from 1 to 3
    # definition of the main model
    def activity_forecast(act):
        
        activityToday = states[num1] # Choose the starting state, randomly
        activityList = [activityToday]
        print("start activity is: ", activityToday)
        i = 0
        prob = 1
        while i != act:
            if activityToday == "Bike":
                change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
                if change == "SS":
                    prob = prob * 0.2
                    activityList.append("Bike")
                    pass
                elif change == "SR":
                    prob = prob * 0.6
                    activityToday = "Run"
                    activityList.append("Run")
                else:
                    prob = prob * 0.2
                    activityToday = "Sailing"
                    activityList.append("Sailing")
            elif activityToday == "Run":
                change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
                if change == "RR":
                    prob = prob * 0.5
                    activityList.append("Run")
                    pass
                elif change == "RS":
                    prob = prob * 0.2
                    activityToday = "Bike"
                    activityList.append("Bike")
                else:
                    prob = prob * 0.3
                    activityToday = "Sailing"
                    activityList.append("Sailing")
            elif activityToday == "Sailing":
                change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
                if change == "II":
                    prob = prob * 0.1
                    activityList.append("Sailing")
                    pass
                elif change == "IS":
                    prob = prob * 0.2
                    activityToday = "Bike"
                    activityList.append("Bike")
                else:
                    prob = prob * 0.7
                    activityToday = "Run"
                    activityList.append("Run")
            i += 1
        return activityList
        
    # To save every activityList
    list_activity = []
    count = 0

    # `Range` starts from the first count up until but excluding the last count
    for iterations in range(1,1100):
        list_activity.append(activity_forecast(2))

    # Check out all the `activityList` we collected    
    print("\n",list_activity)

    # Iterate through the list to get a count of all activities ending with initial state
    for smaller_list in list_activity:
        if(smaller_list[2] == states[num1]):
            count += 1
            # print("\n", states[num1])
            # print(count)

    # Calculate the probability of starting from state:'Bike' and ending at state:'Run'
    percentage = (count/1000) * 100
    print("\n", "The probability of starting at state: ", states[num1]," and ending at state: ", states[num1], " = " + str(percentage) + "%")
    now = str(datetime.now().replace(microsecond=0))
    print("time now is: ", now)
    time.sleep(10)
