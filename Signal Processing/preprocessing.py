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
        if self.type == "r":
            
            #Extract file info (top few lines)
            info = pd.read_csv(self.path, nrows=3, delimiter=" ").to_numpy()


            #Header (Column names)
            header = pd.read_csv(self.path, skiprows=4, nrows=1).to_numpy()

            #Make 9 column data 2D array
            full_data = pd.read_csv(self.path, skiprows=5).to_numpy()
            time_index_data = full_data[:,:9]

            #convert time index to seconds
            if float(info[1,2])>0:
                sample_rate = float(info[1,2])
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
        if self.type == "w":
            np.savetxt("processed_data.csv", dataset, delimiter=",")




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
        fft_data = np.fft.fft(data, axis = 0)
        freq = np.fft.fftfreq(len(data[:,1]), d=0.004)
        fft_data[:,0] = freq
        
        
        return fft_data
     

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
        sample_rate = 250.0
        num_sample = len(data[:,0])
        total_time = num_sample/sample_rate
        step = 1/sample_rate
        time = np.arange(0, total_time, step, dtype=float)
        ifft_data = np.fft.ifft(data, axis = 0)
        ifft_data[:,0] = freq
        return ifft_data

    def plot(self, data: np.ndarray, type: str = 'Raw'):
        """
            Create a plot for different types of EEG series: 'Raw' time series,
            'Filtered' time series, and 'FFT' plot
        """
