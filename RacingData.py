import csv
import pandas as pd
import numpy as np
from bokeh.models import Slope, Label
from bokeh.plotting import figure, show
from sklearn.linear_model import LinearRegression
import traceback


#Open CSV, clean data, renames columns to more widely-used names, takes absolute value of data
rawdata = pd.read_csv('RayRF9708012014r003.csv', skiprows=18,skip_blank_lines=True)
lapdata = rawdata.dropna(axis='columns', how='all')
lapdata.columns = ['Time', 'Distance', 'Brake Pressure', 'Steering Angle', 'Vertical GForce', 'Lateral GForce', 'Longitudinal GForce', 'Gear', 'RPM', 'Throttle %', 'MPH']
lapdata = abs(lapdata)

#Clean new columns so  they can be presented as variables later on
variables = str([column for column in lapdata.columns])

#Create variable counter for function
variable_counter = 0
def select_variable():
    """Write user prompts to select the variables they wish to compare"""
    global variable_counter
    if variable_counter < 1:
        selection = input('Type Your Desired X-Axis Variable From ' + variables)   
    else:
        selection = input('Type Your Desired Y-Axis Variable From ' + variables)

    return selection

#Call function for X and Y variables, update counter 
xvariable = select_variable()
variable_counter += 1
yvariable = select_variable()
variable_counter += 1

def variable_array(variable):
    """convert selected variable to an array for statistics and graphing purposes"""
    var = lapdata[[variable]]
    return np.squeeze(np.array(var))

x = variable_array(xvariable)
y = variable_array(yvariable)

def regression(variable):
    """Form statistical plotting for regression line (if desired)"""
    global par
    par = np.polyfit(x, variable, 1, full=True)
    global slope 
    slope = par[0][0]
    global intercept
    intercept = par[0][1]
    return [slope * i + intercept  for i in x]

y_predicted = regression(y)

def stats(variable):
    """print stats for variables to terminal"""
    global covariance
    covariance = np.cov(x, variable, bias=True)[0][1]
    global correlation
    correlation = np.corrcoef(x, variable)[0, 1]
    cov = ('Covariance of ' + str(xvariable) + ' and ' + str(yvariable) + ': ' + str(covariance))
    cc = ('Correlation of ' + str(xvariable) + ' and ' + str(yvariable) + ': ' + str(correlation))
    print(cov)
    print(cc)

stats(y)

#Create scatterplot of selected variables
#file_name = str(xvariable + 'vs.' + yvariable +'.html') - only use if saving file
p = figure(title='Lap Data - Summit Point Raceway', x_axis_label=str(xvariable),
y_axis_label=str(yvariable),toolbar_location="left", tools="pan,reset,save,wheel_zoom")
p.title.align = 'center'
p.title.text_font = 'helvetica'
p.circle(x,y, size=2, color="blue", legend_label=str(xvariable + ' vs. ' + yvariable))
#Plot regression line and legend to plot
p.line(x,y_predicted, color='orange', legend_label='Regression Line: y='+str(round(slope,2))+'x+'+str(round(intercept,2)))

#Try to show file, print error if not possible
try:
    #output_file(file_name) - only use if saving file
    show(p)
except Exception:
    traceback.print_exc()
print('View in browser to see plot')