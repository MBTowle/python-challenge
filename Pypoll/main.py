import os
import csv
import sys
from collections import defaultdict

#Path to collect data from the Resources folder
csv_path = os.path.join('Resources','election_data.csv')

#Read in the csv file
with open(csv_path,'r') as csvfile:
    #split data on commas
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    voter_id = []
    county = []
    candidate_name = []
    candidate = []
    candidate_votes = []
    election_dic = {}
    

    #------------------- Loop to Read Data -------------------
    for row in csvreader:
       election_dic[row[2]] = candidate_name
       print(election_dic)
        #--------------- Determine votes by candidate ---------






    # Total votes cast
    #total_votes = len(voter_id)
    #print(f"{(total_votes)}")
    # Complete list of candidates who received votes
    # Percentage of votes each candidate won
    # Total number of votes each candiate won
    # The winner of the election based on popular vote