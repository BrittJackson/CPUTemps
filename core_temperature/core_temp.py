#! /usr/bin/env python
'''
Created on June 9, 2021

@author: Brittney Jackson
'''
import pandas as pd
import sys
from least_squares import arrangeMatrix
from linear_interpolation import getTempData

"""
Main driver for program
Takes a CSV file from Open Hardware Monitor of core temperatures and time steps as input
"""

def main():
    
    try:
        df = pd.read_csv(sys.argv[1])
    
    except:
        print('Usage: ./test.py [csv filename]')
        sys.exit(1)
    
    #grab temperature data from file and put into dataframe
    final_df = df.iloc[1:,[6,7,8,9]]
    final_df = final_df.astype(float)
    
    core_list = final_df.values.tolist()
    
    core = list(core_list[1:])
    
    core0,core1,core2,core3 = zip(*core)
    
    #time steps of 30 second intervals for each recorded temperature
    step_size = tuple(range(0, len(core0)*30, 30))
    
    arrangeMatrix(core0, core1, core2, core3, step_size)
    getTempData(core0, core1, core2, core3, step_size)
    
if __name__ == '__main__':
    main()
