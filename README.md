# climbvote

Hello intrepid climber and/or internet navigator! For now, here is a little bit to get you going.

## Setup

Use pip to install required libraries (basic ones: numpy, pandas; and pyrankvote):

```
pip install -r requirements.txt
```

## Data

The file `ballot.csv` holds some phony votes to decide who's the best food. It was downloaded from a Google Form that you could easily mimic with a multirow-multiple-choice question.

## Running elections

Usage:
```
python voter.py <votes csv> <number of open seats>
```

For example:
```
# python voter.py ballot.csv 2
FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Apples             4  Elected
Cantelope          4  Elected
Bananas            0  Rejected
Donuts             0  Rejected

And the winners are:
[<Candidate('Apples')>, <Candidate('Cantelope')>]

# python voter.py ballot.csv 3
ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Apples             4  Elected
Cantelope          4  Elected
Bananas            0  Hopeful
Donuts             0  Hopeful

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Apples             2  Elected
Cantelope          2  Elected
Bananas            3  Elected
Donuts             1  Rejected

And the winners are:
[<Candidate('Apples')>, <Candidate('Cantelope')>, <Candidate('Bananas')>]
```
