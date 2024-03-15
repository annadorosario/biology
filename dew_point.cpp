/*
* main.cpp
*
* COSC 1020 Spring 2024
* Project #1B
*
* Due on: FEB 14, 2024
* Author: Anna do Rosario afd47
*
*
* In accordance with the class policies and Georgetown's
* Honor Code, I certify that, with the exception of the
* class resources and those items noted below, I have neither
* given nor received any assistance on this project.
*
* References not otherwise commented within the program source code.
* Note that you should not mention any help from the TAs, the professor,
* or any code taken from the class textbooks.
*/



// import library 
#include <iostream>
#include <cmath>
#include <iomanip> // Include for std::setprecision
#include <map> 

using namespace std; 


/* DEFINE constants:
MIN_HUMIDITY
MAX_HUMIDITY
MAX_TEMP
MIN_TEMP
*/

// Humidity limits:
    const double MIN_HUMIDITY = 0.00000;
    const double MAX_HUMIDITY = 1.00000;

// Temperature limits
    // (in C):
    const double C_MIN_TEMP = -100.00000; 
    const double C_MAX_TEMP = 60.00000;
    
    // in F:
    const double F_MIN_TEMP = -148.00000; 
    const double F_MAX_TEMP = 140.00000; 

    // in K:
    const double K_MIN_TEMP = 173.15000; 
    const double K_MAX_TEMP = 333.15000; 




// Date Limits: 
    // Years: 
    const int MIN_YEAR = 1492;
    const int MAX_YEAR = 2024;
    //Months: 
    const int MIN_MONTH = 1;
    const int MAX_MONTH = 12;
    // Day of the month: 
    const int MIN_DAY = 1;
    const int MAX_DAY31 = 31; 
    const int MAX_DAY30 = 30; 
    const int FEB_MAX = 28;

// Temperature Conversion Constants
    const double F_WATER_FP = 32.00000; // freezing point of water in Farenheit (32)
    const double K_WATER_FP = 273.15000; // freezing point of water in Kelvin
    const double CONVERT_COEFF = 0.5555555555555556; // conversation from F to C coefficient  

// Dew Point Constants
    const double a = 17.27000;
    const double b = 237.70000; 

// Calculation Errors Correction
    const double EPSILON = 1e-5; 
    
// Messages
    const string WElCOME = "WELCOME!!! to the Betty Rubble Weather Analytics,"
                            " LLC Dew Point Calculator\n";
    
    const string GOODBYE = "\nTHANK YOU!!! for using the Betty Rubble Weather Analytics, "
                            "LLC Dew Point Calculator.\n"
                            "Goodbye.\n" 
                            "Send any improvement recommendations to headquarters.";

// START FUNCTION MAIN 

int main()
{

// Set glob. output format for floats to fixed-point notation with 5 decimal places
    std::cout << std::fixed << std::setprecision(5);


/* DEFINE variables for input: 
date
humidity
temperature
tempUnit
*/
    string date; 
    double humidity = 0.1; // relative humidity (RH)
    /*this is the initial string that user enters when 
    prompted for temp (might 1 letter or 100 but recorded as string)
    */ 
    string unitInput = "abc";
    char tempUnit = 'x';
    string fullTempUnit = "temp";
    double temperature = 0; // air temperature (T) in initial units
    double tempInC = 0; // temperature in Celsius
    double dewPointInC = 0; 
    
// OUTPUT welcome message 
    cout << WElCOME;

// DATE
//Date Input Handling: 

    int year = 0000; 
    int month = 00; 
    int day = 00; 
    char slash = '/';

// OUTPUT message that prompts users for the date in the format yyyy/mm/dd
    cout << "PLEASE!!! Enter the date for this temperature reading in the format yyyy/mm/dd:\n";
    
    // putting components of Terminal input into variables
    cin >> ws >> year >> slash >> month >> slash >> day;
     
    
// Checking date against max and mins
    
    // checking if year and month are within range
    if (year < MIN_YEAR || year > MAX_YEAR || month < MIN_MONTH || month > MAX_MONTH ){   
        // checking to make sure year and month is within range
        cout << "ERROR!!! The date entered " << year << slash << month << slash << day << 
                " does not seem to be correct.\n"
                "Check that the year is in the range [1492, 2024]\n"
                "Check that the month is in the range [1, 12]\n"
                "The program will now end... \n";
        
        cout << GOODBYE;
        return 1;
    }
    // checking if day of month is within range
    /*
    month = 
    January: 01 31 days
    February: 02 28 days
    March: 03 31 days
    April: 04 30 days
    May: 05 31 days
    June : 06 30 days
    July : 07 31 days 
    August : 08 31 days 
    September : 09 30 days
    October : 10 31 days
    November : 11 30 days
    December: 12 31 days
    */

   map<int, string> monthMap;
   // Insert some values into the map
    monthMap[1] = "January";
    monthMap[2] = "February";
    monthMap[3] = "March";
    monthMap[4] = "April";
    monthMap[5] = "May"; 
    monthMap[6] = "June";
    monthMap[7] = "July";
    monthMap[8] = "August";
    monthMap[9] = "September";
    monthMap[10] = "October";
    monthMap[11] = "November"; 
    monthMap[12] = "December";
    
    if (month != 2){ // if month is NOT Feb
        if (month == 1 || 3 || 5 || 7 || 8 || 10 || 12){ // months with 31 days
            if (day < MIN_DAY || day > MAX_DAY31){
                cout << "ERROR!!! The date entered "
                        "does not seem to be correct.\n"
                        "Check that the year is in the range [1492, 2024]\n"
                        "Check that the month is in the range [1, 12]\n"
                        "Check that the day is within the range [" 
                        << MIN_DAY << "," << MAX_DAY31 << "]\n"
                        << "You entered " << monthMap.at(month) << " for the month.\n"
                        "The program will now end...\n";
                    
                cout << GOODBYE;
                return 1; 

                
            }
        }
        
        if(month == 4 || month == 6 || month == 9 || month == 11){ // months with 30 days
            if (day < MIN_DAY || day > MAX_DAY30){
                cout << "ERROR!!! The date entered "
                        "does not seem to be correct.\n"
                        "Check that the year is in the range [1492, 2024]\n"
                        "Check that the month is in the range [1, 12]\n"
                        "Check that the day is within the range [" 
                        << MIN_DAY << "," << MAX_DAY30 << "]\n"
                        << "You entered " << monthMap.at(month) << " for the month.\n"
                        "The program will now end...\n";
                
                cout << GOODBYE;
                return 1;
            }
        }
        
        
        
    }    
        
    else{ // if the month IS Feb. the day must be in range 01, 28
        if (day < MIN_DAY || day > FEB_MAX){ 
            cout << "ERROR!!! The date entered " 
                    << year << slash << month << slash << day <<
                    " does not seem to be correct.\n" 
                    "Check that the year is in the range [1492, 2024]\n"
                    "Check that the month is in the range [1, 12]\n"
                    "Remember that " << monthMap.at(month) << " has " << FEB_MAX << " days.\n"
                    "The program will now end...\n";
                
            cout << GOODBYE;
            return 1; 
        }


    }   
                 
    

// HUMIDITY
// OUTPUT message prompting for relative humidity between given range 
    cout << "\nPLEASE!!! Enter the relative humidity "
            "between 0.00000 (exclusive) and 1.00000 (inclusive):\n";

// user will INPUT the relative humidity, INPUT handling for humidity below:
    cin >> ws >> humidity;
    // humidity cannot be zero, so must throw error message even if humidity is zero
    if (humidity <= MIN_HUMIDITY || humidity > MAX_HUMIDITY){ 
        cout << "\nERROR!!! The relative humidity must be between "
                "0.00000 (exclusive) and 1.00000 (inclusive).\n"
                "The program will now end...\n";
        
        cout << GOODBYE;
        return 1; 
    }

// TEMPERATURE UNIT
// Prompt for the temperature units and corresponding single-letters for each unit of measurement
    cout << "\nPLEASE!!! Enter the temperature units"
            "(F for Fahrenheit, C for Celsius, or K for Kelvin):\n";

//INPUT handling for tempUnit below:
    cin >> ws >> unitInput;
    cin.ignore(500, '\n');

    // Convert the first character to standarize the input 
    tempUnit = toupper(unitInput[0]);

    // check to make sure proper unit is recorded
    if (tempUnit != 'F' && tempUnit != 'C' && tempUnit != 'K' ){
        cout << "ERROR!!! The only valid values for temperature units are "
                "F for Fahrenheit, C for Celsius, or K for Kelvin. \n"
                "The program will now end...\n ";
        
        cout << GOODBYE;
        return 1; // this will terminate program due to the error 
    }
    

//TEMPERATURE
// OUTPUT message prompting user for air temperature within specified range 

    switch (tempUnit) {
    
    case 'F':
        fullTempUnit = "Fahrenheit";
        cout << "PLEASE!!! " 
                "Enter the air temperature between " 
                "-148.00000 degrees Fahrenheit and 140.00000 degrees Fahrenheit (inclusive):\n";
        cin >> ws >> temperature;
        
        //checking if temp in F is within range: 
        if (temperature < F_MIN_TEMP || temperature > F_MAX_TEMP ) {
            cout << "ERROR!!!" 
                    "for degrees Fahrenheit, the temperature entered must be between"
                    "-148.00000 F (inclusive) and 140.00000 F (inclusive). \n" 
                    "The program will now end. \n ";
            
            cout << GOODBYE;
            return 1; // this will terminate program due to the error
            
        }
       
        // convert to C
        tempInC = CONVERT_COEFF*(temperature - F_WATER_FP);
        break;
    
    case 'K':
        fullTempUnit = "Kelvin";
        cout << "PLEASE!!! "
                "Enter the air temperature between "
                "173.15000 Kelvin and 333.15000 Kelvin (inclusive)"
                << endl;
        
        cin >> temperature;
        
        // checking if temp in K is within range: 
        if (temperature < K_MIN_TEMP || temperature > K_MAX_TEMP){
            cout << "ERROR!!!" 
                    "The temperature in Kelvin must be between "
                    "173.15000 Kelvin and 333.15000 Kelvin (inclusive).\n"
                    "The program will now end.\n";
            
            cout << GOODBYE;
            return 1; // this will terminate program due to the error 

        }
                
        // convert to C
        tempInC = temperature - K_WATER_FP;
        break;
    
    case 'C':
        // Interpret as Celsius
        fullTempUnit = "Celsius";

        cout << "PLEASE!!! "
                "Enter the air temperature between "
                "-100.00000 degrees Celsius and 60.00000 degrees Celsius (inclusive): \n";
        cin >> ws >> temperature;

        // checking to see if temp in C is within range: 
        if (temperature < C_MIN_TEMP || temperature > C_MAX_TEMP){
            cout << "ERROR!!!" 
                    "The temperature in Celsius must be between"
                    "-100.00000 degrees Celsius and 60.00000 degrees Celsius (inclusive): \n"
                    "The program will now end. \n ";
            
            cout << GOODBYE;
            return 1; 

        }
        
        tempInC = temperature;    
        break;
    

    }

    


//DEW POINT CALCULATION

// CALCULATE dew point

// Step 1: Calculate f(temperature, humidity)
    double interStep; 
    interStep = ((a * tempInC)/(b + tempInC )) + log (humidity);

// Step 2: Calculate final dew point in C
    dewPointInC = (b*interStep) / (a - interStep); // THIS IS STILL IN Celsius

    double finalDewPoint;
    // Convert back to C
    switch (tempUnit) {
    
    case 'F':
        finalDewPoint = (1/CONVERT_COEFF)*dewPointInC + F_WATER_FP;
        break;
    
    case 'K':
        finalDewPoint = dewPointInC + K_WATER_FP;
        break;
    
    case 'C':
        finalDewPoint = dewPointInC;
        break;
    }




/* Program will OUTPUT (pretty print) the following strings: 
date
relative humidity
air temperature
calculated due point
*/

    cout << "You entered " << year << slash << month << slash << day <<
         " for the date of this observation\n";
    cout << "You entered a relative Humidity of " << humidity;
    cout << endl;
    cout << "You entered air temperature of " << temperature << " degrees " << fullTempUnit;
    cout << endl;
    cout << "The calculated dew point is " << finalDewPoint << " degrees " << fullTempUnit;
    cout << endl;
    cout << GOODBYE; 



}
// END program main
