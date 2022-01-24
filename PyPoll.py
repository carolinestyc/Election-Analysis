# deliverables for final script
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources',"election_results.csv")
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# open the file and read it
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# To do: read and analyze the data here.
# read & print the header row
    headers = next(file_reader)
    print(headers)