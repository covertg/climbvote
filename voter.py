import numpy as np
import pandas as pd
import pyrankvote
from pyrankvote import Candidate, Ballot
import sys

n_seats = int(sys.argv[2])
df = pd.read_csv(sys.argv[1])
candidates = df.columns[1:]
candidates = np.array([Candidate(c[c.rfind('[')+1:-1]) for c in candidates])
ballots = []

for i, row in df.iterrows():
    # print('Processing vote %d' % i)
    # Extract the ranking votes from our dataframe row
    ranked_vote = row.values[1:]  # The rankings assigned to each column (i.e. each candidate)
    NaNs = (ranked_vote != ranked_vote)
    ranked_vote[NaNs] = len(candidates) + 1  # Remove NaN (candidates that didn't get a ranking) and place them last
    
    # Turn these rankings into a list of candidate obects
    candidate_indices = np.argsort(ranked_vote)[0:(len(candidates) - sum(NaNs))]  # Count the number of NaNs in case there's not an expexcted number of unranked candidates
    ranked_candidates = candidates[candidate_indices]

    # Create ballot
    ballot = Ballot(ranked_candidates=ranked_candidates)
    ballots.append(ballot)
    # print ("Vote is {}".format(ballot))

# Run single transferable vote election
election = pyrankvote.single_transferable_vote(candidates, ballots, number_of_seats=n_seats)
print(election)

print("And the winners are:")
print(election.get_winners())

# breakpoint()