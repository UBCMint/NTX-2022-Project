from genericpath import exists
import os
import threading
import pandas as pd
import datetime as dt

class recorder(fileName):

    fileName = "test.csv"

    def startRecord():
        bciConnection = True
        bciData = "0" # to be added
        time = dt.now()
        i = 0
        dataArray = [[],[],[]] #time, data, stimulus

        while(bciConnection):
            dataArray[0][i] = time - dt.now()
            dataArray[1][i] = bciData




    def save(stimName, data):

        outputName = stimName 
        i = 1

        while(exists(outputName + ".csv")):
            outputName = outputName + i
            i = i + 1
        
        outputName = outputName + ".csv"

        exportFile = open(outputName, 'w')
        for d in data:
            d[1]


