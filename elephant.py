'''Anna doRosario 
CS152 B 
10/06/2021
Lab 05'''

import sys 
import random as rand
import stats 

'''Please call this program by entering the following into the Terminal command line:

python3 elephant.py <probability of darting> '''


# Assigning names to indexes in parameter list 
IDXCalvingInt = 0
IDXPctDarted = 1
IDXJuvAge = 2
IDXMaxAge = 3
IDXPCalfSurv = 4
IDXPAdultSurv = 5
IDXPSenSurv = 6
IDXCarryCap = 7
IDXNumYears = 8




# test() function creates parameter list and returns, prints to terminal
def test():
    calving_int = 3.1
    pct_darted = 0.0
    juv_age = 12
    max_age = 60
    prob_calf_survivival = 0.85
    prob_adult_survival = 0.996
    prob_sen_survival = 0.20
    carry_capacity = 7000
    num_years = 200

    parameters = [calving_int, pct_darted, juv_age, max_age, prob_calf_survivival, prob_adult_survival, prob_sen_survival, carry_capacity, num_years]

    #print (parameters)

    return parameters
parameters = test()
# print(parameters[IDXJuvAge]) # should print the number 12, the maximum age of a juvenile elephant 

# Assigning names to indexes for elephant features 
IDXGender = 0 
IDXAge = 1
IDXMonthsPreg = 2
IDXMonthsRemContraceptive = 3 

# Function to create and return a new elephant 
def newElephant(parameters, age):
        
    elephant = [0, 0, 0, 0]
    # Assign gender
    elephant[IDXGender] = rand.choice(["f", "m"])
    # Assign age based on age parameter
    elephant[IDXAge] = age
    # Check if elephant is pregnant 
    if elephant[IDXGender] == 'f':
        if age > parameters[IDXJuvAge] and age <= parameters[IDXMaxAge]:
            if rand.random() <= (1.0/(parameters[IDXCalvingInt])):
                elephant[IDXMonthsPreg] = rand.randint(1,22)

    return elephant
    
# Test the function; pop is a nested list with 15 elephants 
# pop = []
# for i in range(15):
#     pop.append(newElephant(parameters, rand.randint(1, parameters[IDXMaxAge])))
    
# for e in pop: 
#     print (e)

# initPopulation function: take in para. list and return list of new elephants (list of lists)
def initPopulation(para_list, carry_capacity):
    population = []
    for i in range(carry_capacity):
        population.append(newElephant(para_list, rand.randint(1, parameters[IDXMaxAge])))

    return population
    
population = initPopulation(parameters, 20)
print(population)
    
    


# incrementAge function: increments the age of the population (returns population list)
def incrementAge(population):
    #print("Old population: ", population)
    for elephant in population:
        elephant[IDXAge] += 1
    return population

population = incrementAge(population)
print("Population size: ", len(population))
print("Incremented population: ", population)
            
# Task 1: calcSurvival function that calculates which elephants survive a year (returns population list)
def calcSurvival(parameters, population):
    # Accessing juvenile and max ages 
    juv_age = parameters[IDXJuvAge]
    senior_age = parameters[IDXMaxAge]
    
    new_population = [] 
    for elephant in population:
        if elephant[IDXAge] == 1: # checks if elephant is a calf 
            if rand.random() < parameters[IDXPCalfSurv]: # checks if it will survive 
                    new_population.append(elephant)
        elif juv_age <= elephant[IDXAge] < senior_age: # checks if elephant is an adult 
            if rand.random() < parameters[IDXPAdultSurv]: # checks survival 
                    new_population.append(elephant)
        elif elephant[IDXAge] >= senior_age: # checks if elephant is a senior 
            if rand.random() <parameters[IDXPSenSurv]: # checks survival 
                    new_population.append(elephant)
            
    return new_population
survival_population = calcSurvival(parameters, population)
print ("Surv. population size: ", len(survival_population))
print("Survival population: ")
print(survival_population)

    
# Task 2: dartElephants function randomly darts female elephants, should return population list 
def dartElephants(parameters, population):
    # Assign parameters to local variables 
    darting_pct = parameters[IDXPctDarted]
    juv_age = parameters[IDXJuvAge]
    max_age = parameters [IDXMaxAge] 

    # Loop over each elephant in population list and check if elephant is viable female 
    for elephant in population:
        if elephant[IDXGender] == "f" and (juv_age < elephant[IDXAge] < max_age):
            if rand.random() < darting_pct: # test if elephant should be darted 
                elephant[IDXMonthsPreg] = 0 
                elephant[IDXMonthsRemContraceptive] = 22 
    return population


# Task 3: cullElephants function cull elephants from the population, return tuple containing first new population list, second number of elephants culled 
def cullElephants(parameters, population):
    # Assign 
    carry_capacity = parameters[IDXCarryCap]
    current_pop_size = len(population) # current size of population before culling takes place 
    num_culled = (current_pop_size - carry_capacity) # this is the number of elephants that need to be culled 
    
    
    # Check if there are too many elephants 
    if num_culled > 0: 
        rand.shuffle(population)
        culled_pop = population[:carry_capacity]
        return (culled_pop, num_culled)
    else:
        return (population, 0) 

# Task 4: controlPopulation function determines whether pop should be darted or culled; return tuple with first item new pop list, second item number culled 
def controlPopulation(parameters, population):
    if parameters[IDXPctDarted] == 0: 
        (newpop, num_culled) = cullElephants(parameters, population)
        
    else:
        newpop = dartElephants(parameters, population)
        num_culled = 0 
        
    return (newpop, num_culled)


# Task 5: Function that simulates a month (should return population list)
def simulateMonth(parameters, population):
    # Subtask 1: Assign three parameters to local variables
    calving_int = parameters[IDXCalvingInt]
    juv_age = parameters[IDXJuvAge]
    max_age = parameters[IDXMaxAge]
    # Subtask 2: Loop over pop list 
    for elephant in population:
        # Accessing info and assigning it to variables 
        gender = elephant[IDXGender]
        age = elephant[IDXAge]
        monthsPregnant = elephant[IDXMonthsPreg]
        monthsContraceptive = elephant[IDXMonthsRemContraceptive]
        
        if gender == 'f' and (juv_age < age < max_age):
            if monthsContraceptive > 0:
                elephant[IDXMonthsRemContraceptive] -= 1 
            elif monthsPregnant > 0:
                if monthsPregnant >= 22:
                    baby_elephant = newElephant(parameters, 1)
                    population.append(baby_elephant)
                    elephant[IDXMonthsPreg] = 0 
                else:
                    elephant[IDXMonthsPreg] += 1
            else:
                if rand.random() <= (1.0/((calving_int*12)-22)):
                    elephant[IDXMonthsPreg] = 1 
    '''Note:
    local variable monthsPregnant references the actual number of months the elephant has been pregnant
    while IDXMonthsPregnant stores the INDEX to reference this actual number'''
    return population
          
# Task 6: Function to simulate a year 
def simulateYear(parameters, population):
    population = calcSurvival (parameters, population)
    population = incrementAge(population)

    for i in range(11):
        month_simulation = simulateMonth(parameters, population)
        return month_simulation

    
# Task 7: Function to calcuate statistics on the simulation (returns a list with values of number of calves, juvs., adult males, adult females, & seniors; total number in population; total culled)
def calcResults(parameters, population, numberCulled):
    # Access juvenile age and max age parameters
    juv_age = parameters[IDXJuvAge]
    max_age = parameters[IDXMaxAge]
    
    # Create variables number of each age of elephant
    num_calves = 0
    num_juvs = 0 
    num_adultFemale = 0
    num_adultMale = 0
    num_seniors = 0 

    # Loop over pop list 
    for elephant in population:
        age = elephant[IDXAge] 
        if age == 1:
            num_calves += 1
        elif 1 < age <= juv_age: 
            num_juvs += 1 
        elif juv_age < age < max_age:
            if elephant[IDXGender] == 'f':
                num_adultFemale += 1
            elif elephant[IDXGender] == 'm':
                num_adultMale += 1 
        elif age >= max_age:
            num_seniors += 1 
    
    # Total population size:
    total_pop = stats.sum([num_calves, num_juvs, num_adultFemale, num_adultMale, num_seniors])
    population_stats_list = [total_pop, num_calves, num_juvs, num_adultFemale, num_adultMale, num_seniors, numberCulled]

    # Assigning names to index in the population stats list 
    IDXTotalPop = 0 
    IDXNumCalves = 1
    IDXNumJuvs = 2
    IDXNumAdFem = 3
    IDXNumAdMale = 4
    IDXNumSeniors = 5
    IDXNumCulled = 6
     
    # print ("Total population: ", population_stats_list[IDXTotalPop])
    # print("Number of calves: ", population_stats_list[IDXNumCalves])
    # print("Number of juveniles: ", population_stats_list[IDXNumJuvs])
    # print("Number of adult females: ", population_stats_list[IDXNumAdFem])
    # print("Number of adult males: ", population_stats_list[IDXNumAdMale])
    # print("Number of seniors: ", population_stats_list[IDXNumSeniors])
    # print("Number culled: ", population_stats_list[IDXNumCulled])

    return population_stats_list

# (calcResults(parameters, population, 5))


# Task 8: Run a simulation (returns list of demographics)
# N: number of years to run the simulation 
def runSimulation(parameters, N=parameters[IDXNumYears]): 
    popsize = parameters[IDXCarryCap]

    # Initialize an elephant population 
    init_population = initPopulation(parameters, parameters[IDXCarryCap])
    [population, numCulled] = controlPopulation(parameters, init_population)
    

    # Run the simulation for N years and store the results 
    results = []
    for i in range(N):
        population = simulateYear(parameters, init_population) # returns population list 
        #print(population)
        [controlled_population, numCulled] = controlPopulation(parameters, population)
        results.append(calcResults(parameters, controlled_population, numCulled))
        print("Total population that year: ", results[i][0])
        if results [i][0] > (2 * popsize) or (results[i][0] == 0): #population_stats_list = [total_pop, num_calves, num_juvs, num_adultFemale, num_adultMale, num_seniors, numberCulled]
            print('Terminating early')
            break 
    
    
    return (results)




# Task 9: Main function 
def main(argv):
    if len(argv) < 2:
        print("You have incorrectly entered the parameters. \nThis program requires three inputs in the command line. Please enter: python3 elephant.py (probability of darting) ")
    
    # Creating variable for probability of darting from command line input 
    probability_darting = float(argv[1])

    # Set up parameters 
    calving_int = 3.1
    pct_darted = probability_darting # changes probability of being darted based on command line argument (user input)
    juv_age = 12
    max_age = 60
    prob_calf_survivival = 0.85
    prob_adult_survival = 0.996
    prob_sen_survival = 0.20
    carry_capacity = 7000
    num_years = 200
    # List for parameters 
    parameters = [calving_int, pct_darted, juv_age, max_age, prob_calf_survivival, prob_adult_survival, prob_sen_survival, carry_capacity, num_years]

    results = runSimulation(parameters)
    print(results[-1]) 
    
    # Calculate averages 
    total_pop_eachYear = []
    for i in range(len(results)):
        total_pop_eachYear.append(results[i][0])
    avg_total_pop = stats.mean(total_pop_eachYear)
    print("Average total population: ", avg_total_pop)
    
    total_calves_eachYear = []
    for i in range(len(results)):
        total_calves_eachYear.append(results[i][1]) #population_stats_list = [total_pop, num_calves, num_juvs, num_adultFemale, num_adultMale, num_seniors, numberCulled]
    avg_total_calves = stats.mean(total_calves_eachYear)
    print("Average total calves: ",avg_total_calves)
    
    total_juvs_eachYear = []
    for i in range(len(results)):
        total_juvs_eachYear.append(results[i][2])
    avg_total_juvs = stats.mean(total_juvs_eachYear)
    print("Average total juveniles: ",avg_total_juvs)
    
    total_adultFemale_eachYear = []
    for i in range(len(results)):
        total_adultFemale_eachYear.append(results[i][3])
    avg_total_adultFemale = stats.mean(total_adultFemale_eachYear)
    print("Average total adult females: ",avg_total_adultFemale)
    
    total_adultMale_eachYear = []
    for i in range(len(results)):
        total_adultMale_eachYear.append(results[i][4])
    avg_total_adultMale = stats.mean(total_adultMale_eachYear)
    print("Average total adult males: ",avg_total_adultMale)
    
    total_seniors_eachYear = []
    for i in range(len(results)):
        total_seniors_eachYear.append(results[i][5])
    avg_total_seniors = stats.mean(total_seniors_eachYear)
    print("Average total seniors: ",avg_total_seniors)
    
    total_culled_eachYear = []
    for i in range(len(results)):
        total_culled_eachYear.append(results[i][6])
    avg_total_culled = stats.mean(total_culled_eachYear)
    print("Average total culled: ", avg_total_culled)

if __name__ == "__main__":
    main(sys.argv)



