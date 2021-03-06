<p align="center">
    Election-Analysis (Deliverables 1 & 2)
</p>

<p align="center">
    Module 3 for Data Science Bootcamp - Python
</p>

<p align="center">
    STUDY GROUP FOR MODULE 3 - Ryan Knauff, Cayli Swartz, Marshall Miley, Lora Leonida
</p>

###  **Project Overview**
Seth and Tom need assistance in auditing election results. Specifically, they need help creating a python script that analyzes the election results spreadsheet and displays it in a way they can read and understand it. It's important that our results are accurate, our campaign relys on it.

- ### Election data and its purpose:
    1. Why are we analyzing this data?
    2. What is the goal and possible outcomes?
    3. What pieces of data can help build toward and obtain our goal(s)?

Our script must produce accurate results of the following parameters:
    -The voter turnout for each county
    -The percentage of votes from each county out of the total count
    -The county with the highest turnout
    
    
## **Analysis**

First it was important to create our variables, but in order to do that we needed to understand what our goals were.
We need to find:
    1. Total votes (count)
    2. Votes by County (count & percentage)
    3. Votes by Candidate (count & percentage)
    4. Winner
    5. Winning vote count
    6. Winning Percentage 
    7. Largets county turnout

The most logical next step in my mind was to focus on the count of each individual candidate. Using the csv reader we were able to count how many votes each individual candidate recieved.

The same was done for each individual county, as shown below.

<p align="center">
  <img src="https://github.com/lawnshogan/election-analysis/blob/main/Resources/Candidate%20%26%20County%20Votes%20-%20Code%20Block.png" width="700"/>
</p>

With this completed, it is also important we find the total votes:

<p align="center">
  <img src="https://github.com/lawnshogan/election-analysis/blob/main/Resources/Total%20Votes%20-%20Code%20Block.png" width="700"/>
</p>

For the finale, we need the information regarding our winning candidate, total votes of the winning candidate and percentage of their vote vs the total. The following code was used for both county and candidate variables.


<p align="center">
  <img src="https://github.com/lawnshogan/election-analysis/blob/main/Resources/Determining%20Winners%20-%20Code%20Block.png" width="700"/>
</p>



### **Results**


<p align="center">
  <img src="https://github.com/lawnshogan/election-analysis/blob/main/Resources/Deliverable%201%20-%20Text%20Output.png" width="700"/>
</p>


    - How many votes were cast in this congressional election?

### **369,711 Total Votes**

    - Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

### **Jefferson: 10.5% (38,855)**
### **Denver: 82.8% (306,055)**
### **Arapahoe: 6.7% (24,801)**


    - Which county had the largest number of votes?

### **Denver**

    - Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

### **Charles Casper Stockham: 23.0% (85,213)**
### **Diana DeGette: 73.8% (272,892)**
### **Raymon Anthony Doane: 3.1% (11,606)**


    - Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

### **Diana DeGette: 73.8% (272,892)**




### **Summary**


I would tell them if they got me more data there would be more analysis I could perform and more answers that could be answered. Sure it's great we got election results that are accurate, but what if we want to know more demographics about these these voters?

This script could also be used in State or even Federal elections as well and could be altered to look at districts, counties, states, regions - anything really.

If Diana DeGette could get information regarding her 272,892 voters, she might be able to win the following election as well. This analysis could be performed on her select group of voters with more data.
