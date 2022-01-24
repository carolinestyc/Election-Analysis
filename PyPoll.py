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
# initialize a total vote counter
total_votes = 0
# candidate options
candidate_options = []
# create candidate votes
candidate_votes = {}
#winning candidate & winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# open the file and read it
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# To do: read and analyze the data here.
# read the header row
    headers = next(file_reader)
    # print each row in the CSV file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        #print the candidate name from each row
        candidate_name = row[2]
        #add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0
        #add a vote to the candidates count
        candidate_votes[candidate_name] += 1

    #determine the percentage of votes for each candidate by looping through the counts
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        #determine  winning vote count and candidate
        # determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #print out winning candidate summary
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------/n")
    print(winning_candidate_summary)
