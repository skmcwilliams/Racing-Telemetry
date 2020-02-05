import csv
import pandas as pd
import numpy as np
from bokeh.models import Slope, Label
from bokeh.plotting import figure, output_file, show
from sklearn.linear_model import LinearRegression
import traceback


#Open CSV, clean data, renames columns to more widely-used names, takes absolute value of data
rawdata = pd.read_csv('RayRF9708012014r003.csv', skiprows=18,skip_blank_lines=True)
lapdata = rawdata.dropna(axis='columns', how='all')
lapdata.columns = ['Time', 'Distance', 'Brake_Pressure', 'Steering_Angle', 'Vertical_GForce', 'Lateral_GForce', 'Longitudinal_GForce', 'Gear', 'RPM', 'Throttle%', 'MPH']
lapdata = abs(lapdata)

#Clean new columns so  they can be presented as variables later on
variables = [column for column in lapdata.columns]

#make variables as string to be easily added to input request below
variables = str(variables)

#Write user prompts to select the variables they wish to compare
xprompt = input('Type Your Desired X-Axis Variable From ' + variables)
yprompt = input('Type Your Desired Y-Axis Variable From ' + variables)

"""
#Write Prompts and define variables
selectx = input(xprompt + variables)
selecty = input(yprompt + variables)
"""

def variable_array(variable):
    """convert selected variable to an array for statistics and graphing purposes"""
    var = lapdata[[variable]]
    return np.squeeze(np.array(var))

x = variable_array(xprompt)
y = variable_array(yprompt)

#Create scatterplot of selected variables
file_name = str(xprompt + yprompt +'.html')
p = figure(title='Lap Data - Summit Point Raceway', x_axis_label=str(xprompt),
y_axis_label=str(yprompt),toolbar_location="left", tools="pan,reset,save,wheel_zoom")
p.title.align = 'center'
p.title.text_font = 'helvetica'
p.circle(x,y, size=2, color="blue", legend_label=str(xprompt + ' vs. ' + yprompt))

#Update plot with statistics
par = np.polyfit(x, y, 1, full=True)
slope=par[0][0]
intercept=par[0][1]
y_predicted = [slope * i + intercept  for i in x]

#TRYING TO ADD MORE DATA TO PLOT - BELOW DATA PRINTS TO TERMINAL
covariance = np.cov(x, y, bias=True)[0][1]
correlation = np.corrcoef(x, y)[0, 1]
cov = ('Covariance: ' + str(covariance))
cc = ('Correlation: ' + str(correlation))
print(cov)
print(cc)

#Plot regression line and legend to plot
p.line(x,y_predicted, color='orange', legend_label='Regression Line: y='+str(round(slope,2))+'x+'+str(round(intercept,2)))

#Try to save file, print error if not possible
try: 
    show(p)
except Exception:
    traceback.print_exc()
print('View in browser to see plot')