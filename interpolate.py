from scipy.interpolate import interp1d
import numpy as np
import pandas as pd

df = pd.read_csv("output.csv", sep = ',', header=[0], encoding="utf-8") 
print(df)

# dataframe to add extra columns for quaters interpolation
df_qtr = pd.DataFrame()
len_df_cols = len(df.columns)
print (list(df.columns), len_df_cols, df_qtr)

print (df.columns, df_qtr)


## Add columns
for index in range (len_df_cols):
    print(df.columns[index])
    colName = df.columns[index]
    if colName.isdigit():
        print(colName)
        # Add year column from original dataframe
        df_qtr[colName] = df[colName]
        # Add three extra columns for quarter interpolation
        for ind in range(1,4):
            df_qtr[colName + "-" + str(ind)] = np.nan
        print(df_qtr)
    else:
        # Add non year column from original dataframe
        df_qtr[colName] = df[colName]
"""		
df.iteritems()
print('Colunm Name : ', columnName)
print('Column Contents : ', columnData.values)
df.assign(Marks = [10,20, 45, 33, 22, 11],  Total = [50]*6  )"""

# Get the mexican growth percentage row
mexican_growth_percentage=df_qtr.loc[df_qtr.IndicatorCode == 'SP.POP.GROW', "2005":].transpose()

print(mexican_growth_percentage)


mexican_growth_percentage_interpol = mexican_growth_percentage.interpolate(method ='linear', limit_direction ='forward')
print(mexican_growth_percentage_interpol)

"""
Interpolation methods:
method : {‘linear’, ‘time’, ‘index’, ‘values’, ‘nearest’, ‘zero’,

        ‘slinear’, ‘quadratic’, ‘cubic’, ‘barycentric’, ‘krogh’, ‘polynomial’, ‘spline’ ‘piecewise_polynomial’, ‘pchip’}
"""

mexican_growth_percentage_interpol = mexican_growth_percentage.interpolate(method ='linear', limit_direction ='backward')
print(mexican_growth_percentage_interpol)

