import Ballot as bal

class Candidate:
    def __init__(self, name):
        # This constuctor should be initalized with a candidate's name (a string)
        # The Candidate object should store a linear collection of ballots that were
        # cast for her. A ballot is considered cast for the candidate if that
        # candidate has the top ranking on that ballot.
        pass

    def get_name(self):
        # Return the name of the candidate
        pass

    def add_ballot(self, ballot):
        # Add the ballot to the internal collection of ballots that were cast for the
        # candidate. 

    def get_ballots(self):
        # Return the collection of ballots cast for the candidate
        pass

    def num_votes(self):
        # Return the number of ballots cast for the candidate
        pass

    def __eq__(self, other):
        # Two candidates are the same if they have the same names
        pass

    def __str__(self):
        # Print the candidate's name and the number of votes that were cast for her
        # The format should be
        # Candidate Name: some_name\n
        # Number of Votes: some_number\n
        pass
  


     
