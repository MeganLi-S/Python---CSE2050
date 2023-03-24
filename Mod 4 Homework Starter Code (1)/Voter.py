class Voter:
    def __init__(self, name):
        self._name = name;
        self._ranked_candidates = []

    def get_name(self):
        return self._name

    def vote(self, ballot, ranking):
        ballot.rank_candidates(ranking)
        self._ranked_candidates = ballot.get_candidates();
        return ballot;   # return is not necessary, added for clarity

if __name__ == "__main__":
   pass

