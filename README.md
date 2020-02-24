This program reads data in a CSV file provided by a race car's datalogger and plots the variables of your choosing
in a html file that relfects the selected variables. Run the program and you will be prompted to compare X and Y variables of your choosing.

In the background this program:
- cleans CSV file to identify header
- renames columns of the CSV file to something that is more recognizeable
- makes all variables absolute values to accurately represent cause and effect
- condenses the data to be one dimensional for statistical purposes
- concatenantes strings with other variables to create labels, legends, and file names
- calculates all relevant statistical using SciPy, NumPy, and sklearn - prints to terminal
- Plots regression line


Your variable choices are below:
- Time: Time throughout the two laps worth of data in 0.05 second increments
- Distance: Distance traveled throughout the lap
- Brake Pressure: Braking force applied by driver
- Steering Angle: Steering angle applied by driver (negative is left, positive is right)
- Vertical GForce: The force of the vehicle rising or lowering on the springs
- Lateral GForce: The force resulting of braking or accelerating
- Longitudinal GForce: The force resulting of navigating turns
- Gear: Gear that the vehicle is in at the given Time
- RPM: Revolutions Per Minute of the engine
- Throttle%: The percent of throttle application by the driver
- MPH: Speed of vehicle in Miles Per Hour

The program will request X and Y variables, please type the variables you would like to see and the program will plot them
into the html file. You will receive an error if the variable that you typed is not in the dataset

NEW IMPLEMENTATIONS WILL INCLUDE
- Use wrapper or a second class for the assign to automatically calculate its executions and therefore execute
 the Y-Axis language automatically after the X-variable has been assigned