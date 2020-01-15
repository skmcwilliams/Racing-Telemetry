import csv
import pandas as pd
import numpy as np
from bokeh.models import Slope, Label
from bokeh.plotting import figure, output_file, save
from sklearn.linear_model import LinearRegression
import traceback


#Open CSV, clean data, and Rename columns to more widely-used names
rawdata = pd.read_csv('RayRF9708012014r003.csv', skiprows=17,skip_blank_lines=True)
lapdata = rawdata.dropna(axis='columns', how='all')
lapdata.columns = ['Time', 'Distance', 'Brake_Pressure', 'Steering_Angle', 'Vertical_GForce', 'Lateral_GForce', 'Longitudinal_GForce', 'Gear', 'RPM', 'Throttle%', 'MPH']

#Clean columns so  they can be presented as variables laer on
variables = []
for column in lapdata.columns: 
    if column not in variables: 
        variables.append(column)

#make variables as string to be easily added to input request below
variables = str(variables)

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

#TRYING TO ADD MORE DATA TO GRAPH - BELOW DATA PRINTS TO TERMINAL
covariance = np.cov(x, y, bias=True)[0][1]
correlation = np.corrcoef(x, y)[0, 1]
cov = ('Covariance: ' + str(covariance))
cc = ('Correlation: ' + str(correlation))
print(cov)
print(cc)

#Plot regression line and legend to graph
p.line(x,y_predicted, color='orange', legend_label='Regression Line: y='+str(round(slope,2))+'x+'+str(round(intercept,2)))
output_file(file_name)

try: 
    save(p)
except Exception:
    traceback.print_exc()
print("Open " + file_name + ' to view chart')