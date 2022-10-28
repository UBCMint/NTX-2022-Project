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
    rpath = os.path.join(os.getcwd(),'Data','Raw Data')
    fpath = os.path.join(os.getcwd(),'Data','Filtered Data')
    for folder in os.listdir(rpath):
        rpathexp = os.path.join(rpath,folder)
        for rfile in os.listdir(rpathexp):
            path_data_file = os.path.join(rpathexp,rfile)
            # load dataset
            data_file = pp.File(path_data_file)
            (info, rdata) = data_file.load()
            # initialise dataset
            p = pp.Preprocess()
            hdata = p.hpass(rdata)
            ldata = p.lpass(hdata)
            # remove powerline noise using notch filter
            # powerline noise in Canada at 60Hz
            # source: https://www.canada.ca/en/health-canada/services/health-risks-safety/radiation/everyday-things-emit-radiation/power-lines-electrical-appliances.html 
            ndata = p.notch(ldata, f = [60])
            
            pfile = "filtered_"+rfile
            path_fdata_file = os.path.join(fpath,folder,pfile)
            fdata_file =pp.File(path_fdata_file)
            fdata_file.write(ndata)

if __name__ == '__main__':
    main()
