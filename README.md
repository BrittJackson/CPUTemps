# CPUTemps

Command-line interface software application which reads in data from the open-source software Open Hardware Monitor.
The application requires a CSV file as input.

## Requirements
* Open Hardware Monitor
* Python 3.8
* NumPy Library
* Pandas Library
* Matplotlib

## Setup Prior to Using the CPUTemp Application
* Open the Open Hardware Monitor application and go to settings.
* Set the logging interval to 30 seconds.
* Go to Options then Log Sensors. This will allow the report to be recorded in a CSV file.
* The CSV file will automatically be saved to the Open Hardware Monitor folder.

## Sample Execution and Output

Running the program without an input file as: 
```
./core_temp.py
```
The following will be displayed:
```
Usage: ./core_temp.py [csv filename]
```
```
To run the program:
./core_temp.py filename.csv
```
Output written to each core text file in the form:
```
x_k <= x <= x_k+1; y_i = c0 + c1x; type

(Type refers to least squares approximation or linear interpolation)
```
Data is output to four files in the form:
```
cpuTemps-core-0.txt
cpuTemps-core-1.txt
cpuTemps-core-2.txt
cpuTemps-core-3.txt

A graph of linearly interpolated data is output.
```
