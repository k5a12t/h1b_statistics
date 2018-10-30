# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run](README.md#run)

# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

Your code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code.

Raw data could be found [here](https://www.foreignlaborcert.doleta.gov/performancedata.cfm) under the __Disclosure Data__ tab (i.e., files listed in the __Disclosure File__ column with ".xlsx" extension). 
For your convenience we converted the Excel files into a semicolon separated (";") format and placed them into this Google drive [folder](https://drive.google.com/drive/folders/1Nti6ClUfibsXSQw5PUIWfVGSIrpuwyxf?usp=sharing). However, do not feel limited to test your code on only the files we've provided on the Google drive 

**Note:** Each year of data can have different columns. Check **File Structure** docs before development. 


# Approach

For a given input file, different functions are written to extract the necessary information. Three separate functions extract the column number that corresponds to: 1. the status of the application 2. the occupation name 3. the state where the employee will be working. 

A separate function gets the total number of certified applications in a given input file. 

Another function outputs a dictionary with the number of certified applications for a given variable (e.g. occupation or state).

A final function, summarized the results and writes the outputs files. 


# Run

The shell script run.sh will run the code using the provided example data. 

To run code:

python3 ./src/h1b_counting.py ./input/INPUT.csv ./output/top_10_occupations.txt ./output/top_10_states.txt
where INPUT.csv is the input file. The two output files top_10_occupations.txt and top_10_states.txt will be written to the output directory. 

to run unit tests:
python3 ./insight_testsuite/tests/your-own-test_1/test_helper.py
