'''Anna doRosario 
CS152 B
09/29/2021
Project 04'''

import sys 
from hashlib import new
import random as rand

from matplotlib.pyplot import new_figure_manager, title 
'''Execute this code by entering the following in the terminal command line:
python3 penguin.py <number of simulations to run> <typical number of years between an El Nino event>'''

# Function should return list of specified size (N)
    # N: initial population size 
    # probFemale: probability of indiv. being female 

def initPopulation(N, probFemale):
    population = [] # initialize variable to the empty list 
    # iterates N times and generates penuguin using prob. that it is male or female 
    for i in range(N):
        random_number = rand.random() # generates random number between 0 and 1
        if random_number < probFemale: 
            population.append("f")
        else:
            population.append("m")
    
    return population

#pop = initPopulation(10, 0.5)
# print("Original population")
# print(pop)

# testing the initPopulations function 
def test():
    popsize = 10 
    probFemale = 0.5 

    pop = initPopulation(popsize, probFemale)
    
    print("Population of ", popsize, "individuals: ", pop)

    return pop

if __name__ == "__main__":
    test()

# T3: Function to simulate a single year 
'''og_pop: original population list 
elNinoProb: probability of an El Nino 
stdRho: growth factor in a regular year (>1)
elNinoRho: growth factor in an El Nino year 
probFemale: probabilty of a new indiv. being female 
maxCapacity: the max carrying capacity of the ecosytem '''
def simulateYear(og_pop, elNinoProb, stdRho, elNinoRho, probFemale, maxCapacity):
    
    # Determine if it is El Nino year 
    elNinoYear = False
    if rand.random() < elNinoProb:
        elNinoYear = True
    
    newpop = []
    # loop over original population list (given as a parameter)
    for penguin in og_pop:
        if len(newpop) > maxCapacity:
            break # no more penguins! 
        if elNinoYear == True:
            if rand.random() < (elNinoRho):
                newpop.append(penguin)
            
        else: 
            newpop.append(penguin)
            if rand.random() < (stdRho - 1.0 ):
                if rand.random() < probFemale:
                    newpop.append("f")
                else:
                    newpop.append("m")
    return newpop

#T4: Test simulateYear function --> should get 3-6 El Ninos and 11-14 standards
og_pop = initPopulation(10, 0.5)
newpop = simulateYear(og_pop, 1.0, 1.188, 0.4, 0.5, 2000) # new population in an El Nino year (3-6 penguins)

print("El Nino year")
print(newpop)
print(len(newpop), "individuals")

newpop = simulateYear(og_pop, 0.0, 1.188, 0.4, 0.5, 2000) # new population in a standard year (11-14 penguins)
print("Standard year")
print(newpop)
print(len(newpop), "individuals")

 # T5: Function that runs a single simulation        
'''num_years: number of years to run the simulation
initPopsize: initial population size 
probFemale: probability a penguin is female
elNinoProb: prob el Nino occurs in a given year
stdRho: pop growth in non-El Nino year
elNinoRho: pop growth in an El Nino year
maxCapacity: max carrying capacity of ecosystem
minViable: min viable population'''
def runSimulation(num_years, initPopsize, probFemale, elNinoProb, stdRho, elNinoRho, maxCapacity, minViable):
    # initialize population 
    init_population = initPopulation(initPopsize, probFemale)
    #endDate = num_years

    # list to store new population 
    newPopulation = []
    for i in range(num_years):
        year = simulateYear(init_population, elNinoProb, stdRho, elNinoRho, probFemale, maxCapacity)
        newPopulation.append(year)
    
    # test if there is a viable population 
        if (len(year) < minViable):
        
            endDate = i 
            break
        elif not 'f' in year or not 'm' in year:
            endDate = i 
            break
        
        else: 

            endDate = num_years
        #print(len(year))
        
    
    #print("Number of years simulation ran: ", endDate)
    return endDate
    # small elNino prob (0.1) --> return num_years, pop survives
    # large elNino prob (0.5) --> return value < num_years 


# T6 Test runSimulation (see above for description of parameters)
runSimulation(201, 500, 0.5, (0.1/7.0), 1.188, 0.41, 2000, 10)

    

# T7: This is a main function that runs many simulations 
def main(argv):
    #print("Please enter python3 (name of your program) (number of simulations to run) (typical number of years between an El Nino event)")
    # usage statement
    if len(argv) < 3:
        print("You have incorrectly entered the parameters. \nThis program requires four inputs. Please enter: python3 (name of your program) (number of simulations to run) (typical number of years between an El Nino event) ")

    # Extract values from the command line arguments
    #print(argv)
    # argv[0] is name of program: penguin.py
    
    numSim = int(argv[1]) # number of simulations to run 
    ElNino_year_diff = int(argv[2]) # typical number of years between an El Nino event 
   
    # Local variables 
    num_years = 201 #number of years 
    N = 500 # initial population size 
    probFemale = 0.5 # probability of a female 
    elNinoProb = (1.0/ElNino_year_diff) # probability of an El Nino 
    stdRho = 1.188 # growth factor in standard year 
    elNinoRho = 0.41 # growth factor in El Nino year 
    maxCapacity = 2000 # max. carrying capacity 
    minViable = 10 # minimum viable population
    sim_results = [] # empty list to hold results of simulations 


    # Main loop that runs simulations 
    for i in range(numSim):
        sim = runSimulation(num_years, N, probFemale, elNinoProb, stdRho, elNinoRho, maxCapacity, minViable)
        sim_results.append(sim) 
    

    # Probability of survival after N years 
    num_years_extinct = 0
    for i in sim_results:
        if i < numSim:
            num_years_extinct += 1 
    
    prob_extinction = (num_years_extinct)/(numSim)
    print("Probability of extinction: ")
    print(prob_extinction)

    

    sim_results = main(sys.argv)

    # T8: Compute Cumulative Extinction Probabilty Distribution 

    def computeCEPD(sim_results, num_years_sim ):
        CEPD = [] # list with zeroes (amount: number of years the simulation ran)
        # append num_years_sim zeroes to list 
        for i in range(num_years_sim):
            CEPD.append(0)
        
        # loop over list of sim_results(extinction years)
        for extinction_year in sim_results: 
            if extinction_year < num_years_sim:
                for i in range(num_years_sim-extinction_year):
                    CEPD[num_years_sim-extinction_year+i] += 1

        # loop over CEPD list and divide each entry by length of extinction year results list 
        for i in range(CEPD):
            CEPD[0] = (CEPD/num_years_sim)
                    
        return CEPD

    computeCEPD(sim_results, numSim)


if __name__ == "__main__":
    main(sys.argv)

