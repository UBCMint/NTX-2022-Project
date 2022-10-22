"""
    the preprocessing class will perform filtering on raw EEG data
    and return the filtered data
"""

import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

class File:
    def __init__(self, path, type):
        self.path = path
        self.type = type

    # execute load only if type = 'r'
    def load(self):
        """
            Loads data from the txt as csv at the path. 
            Store info (first few lines of csv) in a separate variable
            Store important data in dataset variable
        """
        # returns a tuple with as (info, dataset)
        return (0,0)
    
    # execute write only if type = 'w'
    def write(self, dataset):
        """
            Writes filtered data file to path as csv
        """




class Preprocess:

    def __init__(self, data):
        """
            Computes discrete Fourier Transform of data from all channels, 
            DFT sample frequencies
        """
        self.data = data
        
        # perform fft, remove negative Fouriers
        self.fftdata = -1
        self.freq = -1


    def hpass(self, f = 0.5):
        """
            TODO: Applies High Pass filter to fft data and converts it to time series
        """

        return 0

    def lpass(self, f = 100):
        """
           TODO: Applies Low Pass filter to fft data and convert it to time series
        """
        return 0

    def notch(self, f = [50, 60]):
        """
            TODO: Applies notch filter to either 50hz+harmonics or 
            60 hz + harmonics, or 50 and 60 hz+ harmonics depending on f and converts it to time series
        """
        return 0
    
    def ifft(self):
        """
            Convert filtered data back to time series using inverse fft
        """
        return 0

    def plot(self, type = 'Raw'):
        """
            Create a plot for different types of EEG series: 'Raw' time series,
            'Filtered' time series, and 'FFT' plot
        """

    

