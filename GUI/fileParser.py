from genericpath import exists
import os
import threading
import pandas as pd
import datetime as dt

class recorder:

    def __init__(self, stimE, bciConnectionE):
        self.stimEvent = stimE
        self.bciConnectionEvent = bciConnectionE 

    def startRecord(self):
        bciConnection = True
        stimStart = False
        bciData = "0" # to be added
        dataArray = [[],[],[]] #time, data, stimulus
        time = dt.now()
        i = 0

        while(bciConnection):
            dataArray[i][0] = time - dt.now()
            dataArray[i][1] = bciData
            dataArray[i][2] = stimStart
            if(self.stimEvent.is_Set()):
                stimStart = True
            if(self.bciConnectionEvent.is_Set() == False):
                bciConnection = False
        return dataArray

    def save(stimName, data):

        outputName = stimName 
        i = 1
        if(exists(outputName + ".csv")):
            while(exists(outputName + i + ".csv")):
                i = i + 1
        
        outputName = outputName + i + ".csv"
        outDf = pd.DataFrame(data)
        outDf.to_csv(outputName)
            


