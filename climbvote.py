import argparse
from datetime import datetime
import numpy as np
import pandas as pd
import pyrankvote
from pyrankvote import Candidate, Ballot
import sys

# Process arguments nicely
parser = argparse.ArgumentParser(description='Counts a ranked-choice voting election with potentially multiple winners using Single Transferrable Vote. Prints the count to stdout and saves to file.')
parser.add_argument('votes_csv', metavar='<csv file>', type=str, help='Path to a CSV file of all the votes (formatted like votes.csv)')
parser.add_argument('n_seats', metavar='<# seats>', type=int, help='Number of open seats to win')
parser.add_argument('--output', default=datetime.now().strftime('%Y%m%d_%H%M%S.out'), type=str, help='Name of file to write output. Default is current date and time.')
args = parser.parse_args()

# Read the votes CSV file, and create a list of candidates based on candidate-names in the CSV header
votes_df = pd.read_csv(args.votes_csv)
candidates = votes_df.columns[1:]
candidates = np.array([Candidate(c[c.rfind('[')+1:-1]) for c in candidates])  # Google forms puts candidate names in [brackets]
ballots = []

# Read the CSV row-by-row and create Ballot objects for pyrankvote
for i, row in votes_df.iterrows():
    # print('Processing vote %d' % i)

    # Extract the ranking votes from our dataframe row. First column is timestamp.
    ranked_vote = row.values[1:]  # List of rankings, index j refers to candidate j
    NaNs = (ranked_vote != ranked_vote)  # True where there are NaNs (candidates that didn't get a ranking)
    ranked_vote[NaNs] = len(candidates) + 1  # If the voter  didn't rank this candidate, they are disregarded (placed last, so the next line will cut them out)
    
    # Create a sorted list of Candidate objects based on this voter's rankings
    candidate_indices = np.argsort(ranked_vote)[:(len(candidates) - sum(NaNs))]  # Returns indices of candidates in sorted order, removing candidates that this voter didn't rank
    ranked_candidates = candidates[candidate_indices]  # Candidate objects corresponding to the sorted indices

    # Create ballot!
    ballot = Ballot(ranked_candidates=ranked_candidates)
    ballots.append(ballot)

    # print ("Vote is {}".format(ballot))

## Run single transferable vote election ##
# Note that in case of first-choice tie, the library uses second-choice for tiebreaks.
election = pyrankvote.single_transferable_vote(candidates, ballots, number_of_seats=args.n_seats)
print(election)

with open(args.output, 'w') as f:
    f.write(str(election))

print('Saved to file ' + args.output)
# breakpoint()