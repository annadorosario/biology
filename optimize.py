'''Anna doRosario 
CS152-B
10/24/2021
Project 06'''

import sys 
import elephant 
import random as rand 
import matplotlib.pyplot as plt 
from matplotlib.pyplot import new_figure_manager, plot, title 
'''Execute this code by entering the following in the terminal command line:
python3 optimize.py <parameter to examine varying effect> '''

# T5: Function to optimize the percent darted 
'''Parameters:
min: minimum parameter value to search 
max: maximum parameter value to search 
optfunc: function to optimize 
parameters: optional parameter list to pass to optfunc
tolerance: how close to zero to get before terminating the search
malterations: how many iterations before terminating 
verbose: whether to print lots of information or not'''

def optimize(min, max, optfunc, parameters = None, tolerance = 0.001, maxIterations = 20, verbose = False):
    done = False

    while done == False: 
        
        testValue = ((max + min)/2)
        if verbose == True:
            print (testValue)

        result = optfunc(testValue, parameters)
        if verbose == True:
            print (result)

        if result >= 0: 
            max = testValue
        elif result < 0:
            min = testValue
        else:
            done = True

        if (max - min) < tolerance: 
            done = True 
        
        maxIterations -= 1 
        if maxIterations <= 0:
            done = True 
    

    return testValue


# test optimize function (a function that returns x - target)
def target(x, pars):
    return (x - 0.73542618)



# Tests binary search using a simple target function 
def testTarget():
    res = optimize(0.0, 1.0, target, tolerance= 0.01, verbose= True,)
    print (res)
    return



# T6: Test optimize function with elephantSim 
def testEsim():
    res = optimize(0.0, 0.5, elephant.elephantSim, tolerance= 0.001, verbose = True)
    print(res)
    return



# T7: Automate varying a simulation parameter (function evalutes the effects of the selected parameter on the dart percentage)
'''Paramters:
whichParameter: the index of parameter to test
testmin: minimum value to test
testmax: maximum value to test 
teststep: the step between parameter values to test 
defaults: default parameters to use'''

def evalParameterEffect(whichParameter, testmin, testmax, teststep, defaults = None, verbose = False):
    if defaults == None: 
        simParameters = elephant.defaultParameters()
    else: 
        simParameters = defaults[:]

    # Empty list to hold the results 
    results = []

    if verbose == True: 
        print("Evaluating parameter %d from %.3f to %.3f with step %.3f" % (whichParameter, testmin, testmax, teststep))

    # Creating plot 
    # plt.title("Effect of changing parameter of", simParameters[whichParameter] )
    # plt.xlabel(simParameters[whichParameter], "Survival probability")
    # plt.ylabel("Optimal Percented Darted")
    # plt.show()
    
    
    t = testmin
    while t < testmax:
        simParameters[whichParameter] = t
        #percDart = optimize(testmin, testmax, optimize, simParameters, tolerance=0.001, maxIterations=20, verbose=False)
        percDart = optimize(0.0, 0.5, elephant.elephantSim, simParameters, tolerance= 0.001, verbose = True)
        results.append((t, percDart))
        if verbose == True: 
            print ("%8.3f \t%8.3f" % (t, percDart))
            # plt.plot(t, percDart,'o')
        t += teststep
    if verbose == False:
        print("Terminating")

    return (results)





calf_surv_parameter = evalParameterEffect(elephant.IDXPCalfSurv, 0.98, 1.0, 0.001, verbose = True)
sen_surv_parameter = evalParameterEffect(elephant.IDXPSenSurv, 0.98, 1.0, 0.001, verbose = True)
calv_int_parameter = evalParameterEffect(elephant.IDXCalvingInt, 3.0, 3.4, 0.05, verbose = True)
max_age_parameter = evalParameterEffect(elephant.IDXMaxAge, 56, 66, 2, verbose = True)

plots = [calf_surv_parameter, sen_surv_parameter, calv_int_parameter, max_age_parameter]


if __name__ == "__main__":
    evalParameterEffect(elephant.IDXPAdultSurv, 0.98, 1.0, 0.001, verbose = True)

    