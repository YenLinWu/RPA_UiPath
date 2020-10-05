# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 16:46:25 2020

@author: YenLin
"""
import pandas as pd
import numpy as np

def Pivot_Table( xlsxPath, Groupers, Aggregations, FillValue, OutputPath, OutputSheetName='Sheet1', DropNAN=False ): 
    
    IndexCols = Groupers.split( ',' )
    AggCols = Aggregations.split( ',' )
    
    raw_data = pd.read_excel( xlsxPath ) 
    pt = pd.pivot_table( raw_data, 
                         index = IndexCols,
                         values = AggCols, 
                         aggfunc = { AggCols[0]:np.sum, AggCols[1]:np.mean }, 
                         dropna = DropNAN, 
                         fill_value = FillValue )
    pt.reset_index( inplace = True )
    pt.to_excel( OutputPath, sheet_name = OutputSheetName, index = False )   