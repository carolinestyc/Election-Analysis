# Election-Analysis
### Challenge 3

## Overview of Election Audit
Tom and Seth with the Colorado Board of Elections have requested assistance with the election audit for a local Congressional race. They want to use Python to verify the results and ask that I share the information in a terminal output and a txt file. There are five (5) initial points of information needed for the audit:
1. Total number of votes cast.
2. A complete list of candidates who received votes.
3. Total number of votes each candidate received.
4. Percentage of votes each candidate won.
5. The winner of the election based on popular vote.
### Additional Audit Overview
After the initial analysis was shared with the Election Commission, they requested some additional information regarding the counties. There are three (3) additional points of information requested:
1. The voter turnout for each county.
2. The percentage of votes from each county of the total count.
3. The county with the highest turnout.

This information will then be shared with Seth & Tom to communicate appropriately to the Elections Commission.
## Resources
Data Source: election_results.csv

Software: Python 3.9.7, Visual Studio Code 1.63.2
## Election Audit Results
The analysis of the election shows that:
* There were 369,711 total votes cast in the Congressional Election.
* There were 3 candidates that received votes. Those candidates and results are:

   Charles Casper Stockham: 85,213 votes (23.05%)
   
   Diana DeGette: 272,892 votes (73.81%)
   
   Raymon Anthony Doane: 11,606 votes (3.14%)
* The Winner of the election is Diana DeGette who received 73.81% of the total vote count with 272,892 votes.
* Voter turnout by County is as follows:

   Jefferson: 38,855 votes (10.51%)
   
   Denver: 306,055 votes (82.78%)
   
   Arapahoe: 24,801 votes (6.71%)
* Denver County had the highest voter turnout with 82.78% of the total vote count.

These results can also be visulized in the txt file (first image below) and terminal (second image below) when the PyPoll_Challenge.py file is run.

![Election Analysis Termintal Output](https://user-images.githubusercontent.com/96352625/150733540-b59ca4ad-2534-415b-a322-b0f5365f41be.png)
![Election Analysis txt Output](https://user-images.githubusercontent.com/96352625/150733549-2a5f605b-b836-4852-8a9e-df2185879ae4.png)
## Election Audit Summary
Using Python to perform the election audit is more efficient and repeatable for any future elections and audits. This code can be easily modfied to use again in future scenarios. This is a pretty simple data set; most election data will have the same information: Ballot ID, County Name, Candidate Name (the person that received the vote). As elections are managed at the local county level, this is standard information. Therefore, this code can be used with other datasets, even ones with more counties or candidates. Beyond the local level, if one wanted to analyze results at the national level and look state by state, the county portion of this code could be modified to analyze states. Additionally, most elections require candidates to declare a party affiliation (Republican (R), Democrat (D), etc.). If the information is not provided but we know the candidates affiliation, the data set can be appended to include that information in a new column. With this data, one could look beyond individual candidate and more generally at party affiliation. For instance, how many votes each party received by county could be added as additional analysis. With these two (2) modifications and many more that aren't discussed here, the benefits of investing in Python as an analytical tool are nearly endless. Election results are pure data, and this code (even with small modifications) will deliver analysis in the most efficient way.
