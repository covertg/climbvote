# climbvote

Hello intrepid climber and/or internet navigator! This code was written to count votes for some of the races in club elections for the Yale Climbing Team and Outdoor Climbing Club. It counts votes assuming multi-winner ranked-choice voting, and uses the `pyrankvote` library.

Here is a little bit to get you going.

## Setup

Use pip to install required libraries (classic ones: numpy, pandas; and pyrankvote):

```
pip install -r requirements.txt
```

## Data

The files `votes_food.csv`, `votes_aceg.csv` hold some phony votes for some phony candidates. They were downloaded from a Google Form that you could easily mimic with a multirow-multiple-choice question. The key assumptions that `climbvote` makes for its input data are that:
* The first column of the CSV is unecessary (timestamps); and
* Candidate names are given in the subequent columns, surrounded by brackets, e.g. [Name].

## Running elections

Here's a helpful help printout:
```
usage: climbvote.py [-h] [--output OUTPUT] <csv file> <# seats>

Count an election with multi-winner ranked-choice voting.

positional arguments:
  <csv file>       Path to a CSV file of all the votes (formatted like votes.csv)
  <# seats>        Number of open seats to win

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  Name of file to write output (in current directory)
```

For example, to name the top-two foods:
```
$ python climbvote.py votes_food.csv 2
FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Apples             4  Elected
Cantelope          4  Elected
Bananas            0  Rejected
Donuts             0  Rejected

Saved to file 20200423_164709.out
```

Alternatively, run the food election with three seats:
```
$ python climbvote.py votes_food.csv 3
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

Saved to file 20200423_164805.out
```