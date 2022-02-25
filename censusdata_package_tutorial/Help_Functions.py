# +
import pandas as pd
import numpy as np
import re

def census_cut(tracts, data):
    '''
    This function is use to cut based on Census Tract for data download by using censusdata package.
        
        Parameters:
            tracts: A list of string which are the Census Tract. Such as 'Census Tract 0000'.
            data: Data download by using censusdata package.
        Return:
            result: A new set of data which only include the data based on Census Track.
    '''
    mask = []
    for i in range(len(data.index)):
        string = str(data.index[i])
        check = True
        for tract in tracts:
            match = re.search(tract, string)
            if match:
                mask.append(True)
                check = False
        if check:
            mask.append(False)
    len(mask), len(data.index)
    result = data[mask]
    return result
