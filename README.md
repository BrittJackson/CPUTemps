# CPUTemps

Command-line interface software application which reads in data from the open-source software Open Hardware Monitor.
The application requires a CSV file as input.

# Requirements
* Open Hardware Monitor
* Python 3.8
* NumPy Library
* Pandas Library

# Sample Execution and Output

Running the program without an input file as: 
```
./core_temp.py
```
The following will be displayed:
```
Usage: ./core_temp.py [csv filename]
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
```
