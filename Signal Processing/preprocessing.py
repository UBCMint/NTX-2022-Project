"""
    the preprocessing class will perform filtering on raw EEG data
    and return the filtered data
"""

import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class File:
    def __init__(self, path: str)-> None:
        self.path = path

    # execute load only if type = 'r'
    def load(self, cutoff: int = 200)->tuple(np.ndarray,np.ndarray):
        """
            Loads data from the txt as csv at the path. 
            Store info (first few lines of csv) in a separate variable
            Store important data in dataset variable
            Param
            -----
            cutoff : 
        """
        # Extract file info (top few lines)
        info = pd.read_csv(self.path, nrows=4, header= None).to_numpy()


        # Header (Column names)
        header = pd.read_csv(self.path, skiprows=3, nrows=1).to_numpy()

        #Make 9 column data 2D array
        full_data = pd.read_csv(self.path, skiprows=4).to_numpy()
        time_index_data = full_data[cutoff:,:9]

        #convert time index to seconds
        if float(info[2,0].split()[-2])>0:
            sample_rate = float(info[2,0].split()[-2])
        else:
            sample_rate = 250.0
            
        num_sample = len(time_index_data[:,0])
        total_time = num_sample/sample_rate
        step = 1/sample_rate
        time = np.arange(0, total_time, step, dtype=float)

        data = time_index_data.copy()
        data[:,0] = time
        
        # returns a tuple with as (info, dataset)
        return (info, data)

    # execute write only if type = 'w'
    def write(self, dataset: np.ndarray):
        """
            Writes filtered data file to path as csv
        """
        dataset = np.insert(dataset, 0, ['Time (s)','EEG 1','EEG 2','EEG 3','EEG 4','EEG 5','EEG 6','EEG 7','EEG 8'], axis =0)
        np.savetxt(self.path, dataset, delimiter=",")




class Preprocess(object):
    sample_rate = 250.0
    """
        Performs filtering on eeg data

        Parameter data for all functions is time series eeg data except for 
        1) ifft where it is frequency data, and
        2) plot where it depends on type of data
    """
    def fft(self, data: np.ndarray) -> np.ndarray:
        """
            Computes discrete Fourier Transform of data from all channels, 
            DFT sample frequencies

            Returns
            -------
            tuple (fft data of channels removing negative fouriers, fft frequencies)

        """
        fft_data = np.fft.fft(data, axis = 0)
        freq = np.fft.fftfreq(len(data[:,1]), d=0.004)
        fft_data[:,0] = freq

        return fft_data
    
    def ifft(self, data: np.ndarray)-> np.ndarray:
        """
            Convert filtered data back to time series using inverse fft
        """
        num_sample = len(data[:,0])
        total_time = num_sample/self.sample_rate
        step = 1/self.sample_rate
        time = np.arange(0, total_time, step)
        ifft_data = np.fft.ifft(data, axis = 0)
        ifft_data[:,0] = time
        return ifft_data

    def hpass(self, data: np.ndarray, f = 0.5)-> np.ndarray:
        """
            Applies High Pass filter to fft data and converts it to time series
            params
            
            data = [[time, e1, e2, e3, e4, e5, e6, e7, e8], [time, e1, e2, e3, e4, e5, e6, e7, e8], ..]
            
            1. Use fft function to create new variable (fftdata) 
            
            data = [[freq, e1, e2, e3, e4, e5, e6, e7, e8], [freq, e1, e2, e3, e4, e5, e6, e7, e8], ..]
            
            2. Index through each array (row) within data. 
            3. Index through the array within the row. 
            4. Filter each channel: 
                    - remove frequencies below threshold (0.5) 
                    - make that index equal to 0
            5. return the filtered array 
            
        """
        fftdata = self.fft(data) 
        
        for i in len(fftdata):

            if abs(fftdata[i, 0]) < f:
            
                for j in range(1,len(fftdata[i])):
                    fftdata[i, j] = 0
            
        return self.ifft(fftdata) 

    def lpass(self, data: np.ndarray, f = 100)-> np.ndarray:
        """
           TODO: Applies Low Pass filter to fft data and convert it to time series
        """
        
        fftdata = self.fft(data) 
        
        for i in len(fftdata):
            
            if abs(fftdata[i, 0]) > f:
                
                for j in range(1,len(fftdata[i])):
                    fftdata[i, j] = 0  
            
        return self.ifft(fftdata)

    def notch(self, data: np.ndarray, f = [50, 60])-> np.ndarray:
        """
            Applies notch filter to either 50hz+harmonics or 
            60 hz + harmonics, or 50 and 60 hz+ harmonics depending on f and converts it to time series
            
            1. The notch filter either nullifies frequencies at 50, 60 or both 50 and 60
            
        """
        
        fftdata = self.fft(data)
        for p in f:
            for i in len(fftdata): 
                if abs(fftdata[i,0])%p == 0:
                    for j in range(1,len(fftdata[i])):
                        fftdata[i, j] = 0

        return self.ifft(fftdata)

    def plot(self, data: np.ndarray, type: str = 'Raw'):
        """
            Create a plot for different types of EEG series: 'Raw' time series,
            'Filtered' time series, and 'FFT' plot
            
            data = [[time (frequency for fft), e1, e2, e3, e4, e5, e6, e7, e8],[time, e1, e2, e3, e4, e5, e6, e7, e8]] each array representing a row in the csv 
            
            ELECTRODES: variable for the list of electrode names (positions x to y in each array within data)
                loop through each electrode
                0-FP1, 1-FP2 2-Cz 3-C5 4-P3 5-Oz 6-P4 7-C6

            time: certain element in each array element 
            
            create a separater to create space between each electrode plot 
            
            electrodes (mV)
            |
            | //\\/\/\/\/\/\/\/\
            |
            | //\/\\/\\/\/\/\/\\
            |
            | \/\/\\/\\\\/\\\//\
            |
            | \/\/\\/\\\\/\\\//\
            |
            | \/\/\\/\\\\/\\\//\
            |___________________
                    time (frequency fft)
                    
            loop through each of the electrodes, 
            
        """
        ELECTRODES = ('FP1', 'FP2', 'Cz', 'C5', 'P3', 'Oz', 'P4', 'C6')
        figure, axis = plt.subplots(8,1)
        xlab = 'Time (s)'

        if type == 'FFT':
            data = self.fft(data)
            xlab = 'Frequency (Hz)'
        
        x = data[:, 0] # x-axis

        for i, e in enumerate(ELECTRODES):
            y = data[:,i+1]

            if type=='FFT':
                y = data[:, i+1]
                y = abs(x[:int(len(x)/2)])**2
        
            axis[i].plot(x, y)
            axis[i].set_ylabel(e)
            
            plt.xlabel(xlab)
            figure.suptitle(type)
            plt.show()
