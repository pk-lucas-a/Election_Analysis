#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options, candidate votes, counties, and county votes.
candidate_optionsA = []
candidate_votesB = {}

# 1: Create a county list and county votes dictionary.
countiesC = []
county_votesD = {}

# Track the winning candidate, vote count and percentage
winning_candidatea = ""
winning_countb = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
top_countyc = 0
top_turnoutd = 0
top_winning_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:
        
        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_optionsA:

            # Add the candidate name to the candidate list.
            candidate_optionsA.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votesB[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votesB[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in countiesC:

            # 4b: Add the existing county to the list of counties.
            countiesC.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votesD[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votesD[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votesD:
    
        # 6b: Retrieve the county vote count.
        county_votes = county_votesD.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(county_votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({county_votes:,})\n")
        print(county_results)
        
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_votes > top_turnoutd) and (county_vote_percentage > top_winning_percentage):
            top_turnoutd = county_votes
            top_countyc = county_name
            top_winning_percentage = county_vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    top_countyc_summary = (
        f"-------------------------\n"
        f"County with Largest turnout: {top_countyc}\n"
        f"-------------------------\n")
    print(top_countyc_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(top_countyc_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votesB:

        # Retrieve vote count and percentage
        votes = candidate_votesB.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_countb) and (vote_percentage > winning_percentage):
            winning_countb = votes
            winning_candidatea = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidatea_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidatea}\n"
        f"Winning Vote Count: {winning_countb:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidatea_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidatea_summary)


# In[ ]:




