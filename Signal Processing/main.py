"""
    This is the main script for preprocessing the raw EEG.
    Input:
        data files in Raw Data folder obtained after collection from OpenBCI headset
        filtering frequencies
    Output:
        filtered data file stored in Filtered Data folder   
"""
import os
import preprocessing as pp

def main():
    """
        The main function to start calling Preprocess class
    """
    # path to Raw Data
    rpath = os.path.join(os.path.dirname(os.getcwd()),'Data','Raw Data')
    fpath = os.path.join(os.path.dirname(os.getcwd()),'Data','Filtered Data')
    for folder in os.listdir(rpath):
        rpathexp = os.path.join(rpath,folder)
        for rfile in os.listdir(rpathexp):
            path_data_file = os.path.join(rpathexp,rfile)
            # load dataset
            data_file = pp.File(path_data_file, 'r')
            (info, rdata) = data_file.load()
            # initialise dataset
            p = pp.Preprocess()
            hdata = p.hpass(rdata)
            ldata = p.lpass(hdata)
            ndata = p.notch(ldata)
            p.plot(rdata, 'Raw')
            p.plot(ndata, 'Filtered')
            p.plot(rdata, 'FFT')
            p.plot(ndata, 'FFT')

            path_fdata_file = os.path.join(fpath,folder,rfile)
            fdata_file =pp.File(path_fdata_file,'w')
            fdata_file.write(ndata)

if __name__ == '__main__':
    main()
