# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:31:44 2020

@author: YenLin
"""
import pandas as pd

def Reshape_Data( xlsxPath, Permutations, FirstLevelIndex, SecondLevelIndex, OutputPath, OutputSheetName='Sheet1' ): 
    
    Permutations = Permutations.split(',')
    
    raw_data = pd.read_excel( xlsxPath ) 
    raw_data.set_index( Permutations, inplace=True )
    reshaped_raw_data = raw_data.stack().unstack( [FirstLevelIndex, SecondLevelIndex] ) 
    reshaped_raw_data.to_excel( OutputPath, sheet_name=OutputSheetName )  