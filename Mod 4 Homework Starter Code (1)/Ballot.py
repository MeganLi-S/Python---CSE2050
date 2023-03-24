

class Ballot:
    def __init__(self, voter, candidates):
        # The Ballot class should be initialized on a Voter object and
        # a list of Candidate objects (see the files Voter.py & Candidate.py)
        pass

    def get_candidates(self):
        # Should return the linear collection of Candidate objects.
        # If the Candidate objects have been ranked by the rank_candidates
        # method, then the internal collection should be sorted according to
        # that ranking, and the collection returned here should follow that
        # ordering as well.
        pass

    def rank_candidates(self, ranking):
        # ranking is a reordering of the list [0, ..., n-1]
        # where n is the number of candidates.
        # 1) This function should raise a ValueError if the ranking argument
        #    is too short or contains repetions (or equivalently, some of the
        #    indexes are missing)
        # 2) The original ranking argument should be saved in an internal data member
        #    (say self._ranking) for potential inspection during recounts
        # 3) The underlying collection of candidates should ordered according to the
        #    ranking argument. That is candidate whose rank is i should appear on the
        #    i-th place in the underlying collection (no sorting is needed for this)
        pass

    def remove_candidate(self, candidate):
        # If this function is called before the rank_candidates has been called, raise
        # an exception of type Exception. One can test whether rank_candidates has been
        # called by testing whether the ranking argument described above has been saved
        
        # This function should simply remove the given Candidate object from the
        # stored collection without changing the order of the remaning Candidates
        pass

    def peek_top(self):
        # Simply return the highest ranked Candidate without removing it
        pass

    def remove_top(self):
        # Return an remove the top ranking Candidate from the underlying collection
        pass

    def __str__(self):
        # Create a string which prints the content of the ballot. The printout should
        # have the following format:

        # Voter name: ____\n
        # Voter Ranking:\n
        # 1. some_candidate_name\n
        # 2. some_candidate_name\n
        # ....
        # k. some_candidate_name\n

        # Note that for consistency all the printouts should and with the new line character "\n"
        pass



