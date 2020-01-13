import csv
import pandas as pd
import numpy as np
from bokeh.models import Slope, Label
from bokeh.plotting import figure, output_file, save
from sklearn.linear_model import LinearRegression


#Open CSV, clean data, and Rename columns to more widely-used names
rawdata = pd.read_csv('RayRF9708012014r003.csv', skiprows=17,skip_blank_lines=True)
lapdata = rawdata.dropna(axis='columns', how='all')
lapdata.columns = ['Time', 'Distance', 'Brake_Pressure', 'Steering_Angle', 'Vertical_GForce', 'Lateral_GForce', 'Longitudinal_GForce', 'Gear', 'RPM', 'Throttle%', 'MPH']
lapdata.Steering_Angle.abs() 
variables = str(lapdata.head(0))


"""
#Check dataframe
print(lapdata.head())
"""

#Write user prompts to select the variables they wish to compare
xprompt = 'Type Your Desired X-Axis Variable From'
yprompt = 'Type Your Desired Y-Axis Variable From'

#Write Prompts and define variables
selectx = input(xprompt + variables)
xvariable = lapdata[[selectx]]
x = np.squeeze(np.array(xvariable))
selecty = input(yprompt + variables)
yvariable = lapdata[[selecty]]
y = np.squeeze(np.array(yvariable))

#Create scatterplot of selected variables
title = 'Lap Data - Summit Point Raceway'
file_name = str(selectx + selecty +'.html')
p = figure(title=title, x_axis_label=str(selectx), y_axis_label=str(selecty))
p.title.align = 'center'
p.title.text_font = 'helvetica'
p.circle(x.squeeze(), y.squeeze(), size=2, color="blue", legend_label=str(selectx + ' vs. ' + selecty))

#Update plot with statistics
par = np.polyfit(x, y, 1, full=True)
slope=par[0][0]
intercept=par[0][1]
y_predicted = [slope*i + intercept  for i in x]
p.line(x,y_predicted, color='orange', legend_label='Regression Line: y='+str(round(slope,2))+'x+'+str(round(intercept,2)))
output_file(file_name)

#TRYING TO ADD MORE DATA TO GRAPH - BELOW DATA PRINTS TO TERMINAL
covariance = np.cov(x, y, bias=True)[0][1]
correlation = np.corrcoef(x, y)[0, 1]
cov = ('Covariance: ' + str(covariance))
cc = ('Correlation: ' + str(correlation))
print(cc)
print(cov)

try: 
    save(p)
except: print("ERROR: Chart Did Not Print")
print("Open" + file_name + 'to view chart')