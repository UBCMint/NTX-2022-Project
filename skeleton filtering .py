"""
    the preprocessing class will perform filtering on raw EEG data
    and return the filtered data
"""

import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

class File:
    def __init__(self, path: str, type: str)-> None:
        self.path = path
        self.type = type

    # execute load only if type = 'r'
    def load(self)->tuple(np.ndarray,np.ndarray):
        """
            Loads data from the txt as csv at the path. 
            Store info (first few lines of csv) in a separate variable
            Store important data in dataset variable
        """
        # returns a tuple with as (info, dataset)
        return (0,0)
    
    # execute write only if type = 'w'
    def write(self, dataset: np.ndarray):
        """
            Writes filtered data file to path as csv
        """




class Preprocess(object):
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
        
        return 

    def hpass(self, data: np.ndarray, f = 0.5)-> np.ndarray:
        """
            TODO: Applies High Pass filter to fft data and converts it to time series
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
        
        fftdata = fft(data) 
        
        for i in len(fftdata) {
            
            if fftdata[i, 0] < f:
            
            for j in len(fftdata[i]) {
                fftdata[i, j] = 0
            }   
                
        }
            
        return ifft(fftdata) 

    def lpass(self, data: np.ndarray, f = 100)-> np.ndarray:
        """
           TODO: Applies Low Pass filter to fft data and convert it to time series
        """
        
        fftdata = fft(data) 
        
        for i in len(fftdata) {
            
            if fftdata[i, 0] > f:
            
            for j in len(fftdata[i]) {
                fftdata[i, j] = 0
            }   
                
        }
            
        return ifft(fftdata)

    def notch(self, data: np.ndarray, f = [50, 60])-> np.ndarray:
        """
            TODO: Applies notch filter to either 50hz+harmonics or 
            60 hz + harmonics, or 50 and 60 hz+ harmonics depending on f and converts it to time series
            
            1. The notch filter either nullifies frequencies at 50, 60 or both 50 and 60
            
        """
        
        fftdata = fft(data) 
        
        for i in len(fftdata) 
        {  
            if fftdata%f == 0:
                fftdata[i, f] = 0
        }
        
        return ifft(fftdata) 
    
    def ifft(self, data: np.ndarray)-> np.ndarray:
        """
            Convert filtered data back to time series using inverse fft
        """
        return 0

    def plot(self, data: np.ndarray, type: str = 'Raw'):
        """
            Create a plot for different types of EEG series: 'Raw' time series,
            'Filtered' time series, and 'FFT' plot
        """
