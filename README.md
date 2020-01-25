This program reads data in a CSV file provided a race car's datalogger and plots the variables of your choosing
in a self-titled html file that relfects the selected variables. The program also identifies the correlation coefficient
and covariance between the variables you chose and prints them in the terminal. The program also plots a regression line
and shows the resulting formula in the legend. The legend displays 

In the background this program:
- cleans CSV file to identify header
- renames columns of the CSV file to something that is more recognizeable
- condenses the data to be one dimensional for statistical purposes
- concatenantes strings with other variables to create labels, legends, and file names
- cleans column names to become more usable in the user's selection of data
- calculates correlation coefficient and covariancea and prints to terminal
- takes the absolute value of all characteristics to accurately represent inputs (throttle, brake pressure, steering angle)
  relative to outputs (MPH, longitudinal gforce, lateral gforce)

Your variable choices are below:
- Time: Time throughout the two laps worth of data in 0.05 second increments
- Distance: Distance traveled throughout the lap
- Brake_Pressure: Braking force applied by driver
- Steering_Angle: Steering angle applied by driver (negative is left, positive is right)
- Vertical_GForce: The force of the vehicle rising or lowering on the springs
- Lateral_GForce: The force resulting of braking or accelerating
- Longitudinal_GForce: The force resulting of navigating turns
- Gear: Gear that the vehicle is in at the given Time
- RPM: Revolutions Per Minute of the engine
- Throttle%: The percent of throttle application by the driver
- MPH: Speed of vehicle in Miles Per Hour

The program will request X and Y variables, please type the variables you would like to see and the program will plot them
into the html file.

Future plans include:
- adding the statistical data to the plot instead of the terminal