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

class Variable:
    def __init__(self,name):
        self.name = name
        self.counter = 0
    
    def assign(self):
        """user selected variables assigned"""
        if self.counter < 1:
            selection = input('Type Your Desired X-Axis Variable From ' + variables)
            self.counter += 1   
        else:
            selection = input('Type Your Desired Y-Axis Variable From ' + variables)
            self.counter += 1 

        return selection

    def array(self,input):
        """convert selected variable to an array for statistics and graphing purposes"""
        var = lapdata[[input]]
        return np.squeeze(np.array(var))

    def regression(self,input):
        """Form statistical plotting for regression line (if desired)"""
        global par
        global x
        par = np.polyfit(x, input, 1, full=True)
        global slope 
        slope = par[0][0]
        global intercept
        intercept = par[0][1]
        return [slope * i + intercept  for i in x]
    

#Call to assign X and Y variables
xvar = Variable('xvar')
yvar = Variable('yvar')
xvariable = xvar.assign()
yvariable = yvar.assign()
#call to array variables
x = xvar.array(xvariable)
y = yvar.array(yvariable)

#call to create regession line
y_predicted = yvar.regression(y)


def stats(variable):
    """print stats for variables to terminal"""
    global covariance
    global correlation
    global xvariable
    global yvariable
    covariance = np.cov(x, variable, bias=True)[0][1]
    correlation = np.corrcoef(x, variable)[0, 1]
    cov = ('Covariance of ' + str(xvariable) + ' and ' + str(yvariable) + ': ' + str(covariance))
    cc = ('Correlation of ' + str(xvariable) + ' and ' + str(yvariable) + ': ' + str(correlation))
    print(cov)
    print(cc)

#call to print stats of X vs. Y
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