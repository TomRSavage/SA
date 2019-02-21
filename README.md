Simulated Annealing is implimented over an arbitary number of dimensions, and included are utilities for plotting the optimization trajectory as well as function value over time.

### Prerequisites

Python 3.0 is required. The PlottingUtility.py file must be in the same file as the SimulatedAnnealing.py file in order to enable the utility to be used to plot the trajectory of the function as well as a 2D contour.

## Function Use
```
INPUTS
    bounds : bounds on the function to be optimized, must be in the form [[x1,x2],[x3,x4]...]
    f      : function to be optimized
    temp_it: iterations per temperature
    t      : initial temperature
    td     : temperature decrease per iteration
    plot   : Set to true to display plotting utilities (Only valid for 2 variables)
    contour: Set to true to display a contour plot underneith trajectory (Only valid for 2 variables)
    
OUTPUTs
    p_best : optimal point
    f_best : function value at optimum point
 ```

## Example

With the PlottingUtilities.py, SimulatedAnnealing.py and TestFunctions.py files within the same directory.
Running the following:
```
SimulatedAnnealing([[-200,500],[0,600]],tf.Schwefel,20,100,0.02,plot=True,contour=True)
```
Produces the following outputs:
```
Optimum at: [423.4364436349647, 425.21396324812764]
Function value at Optimum: 3.044639708296245
```
- ![](GitHub1.png)
- ![](GitHub2.png)
## Authors

* **Tom Savage** - *Initial work* - [TomRSavage](https://github.com/TomRSavage)
