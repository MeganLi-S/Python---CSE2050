# Mod 4 Homework: Ranked Choice Voting
## Goal
In this assignment you will implement two ADTs that play a critical role in a framework that manages Ranked Choice Voting. As is almost always the case in practice (unless you're a founding member in a startup), you will be working in a code framework that was developed by others before your arival on the team, and will have to understand the framework's operation in order to complete the assignment. This assigment will also show you how a problem's complexity can be managed by spreading the funcionality needed to solve it among a number of intuitive classes.

## Ranked Choice Voting

Here are excerpts from a New York Times [article](https://www.nytimes.com/interactive/2021/nyregion/ranked-choice-voting-nyc.html) which describe this particular voting mechanism (please see the animation provided there -- it clarifies things very well):

* Instead of casting a single vote for a single candidate, voters in a ranked-choice system select a set number of candidates in order of preference. In New York’s mayoral primary, voters will be allowed to choose up to five.
* Think of ranked-choice voting as voting in rounds: If a single candidate receives more than 50 percent of first-choice votes in the first round, then he or she wins, and that’s the end of the race.
* If no one exceeds 50 percent of votes in the first round, the candidate in last place is eliminated, and all other candidates move on to the next round. All the votes for the eliminated candidate will be reallocated to whichever candidate those voters ranked second, and then the votes are retabulated. Then the candidate in last place after that will be eliminated.
* In New York’s primary, these rounds of elimination will continue until there are two candidates left — even if a candidate collects more than 50 percent of votes before the very end. The candidate with the most votes in the final round wins. In each round, when a candidate gets eliminated, his or her votes get redistributed to whoever was ranked next on the ballot.

## The Framework
The framework your team has designed consists of four intuitive classes which capture the main ingredients of the voting process.
* `Voter.py` is a small implementation of the voter concept. A voter has a name which distinguishes her from other voters. A voter performs only one action: she fills a Ballot. In order to fill a Ballot (where she'll find the list of candidates), the voter needs to choose a ranking to rank properly every candidate on the ballot. A ranking is a reordered list of indices assigned to the candidates. For example for 5 candidates, a correct ranking would be [4, 3, 0, 2, 1], i.e., the first candidate on the ballot is ranked 5-th, the second 4-th, the third 1st, and so on.
A valid ranking sequence needs to contain all the indices of the candidates without repetition. Ballots with invalid rankings will be discarded. 
* `Ballot.py` is an abstraction that has not been implemented yet and you, as a new member of the team, are asked to cut your teeth on this task. A ballot will contain the name of the voter who has filled it, a linear structure with the candidates participating in the election (some team members suggested Python's deque), and the ranking that the voter has chosen. It has been decided in the early design stages that once the voter has filled the ballot, the candidates are ordered according to that voter's choice (for convenience). Please see the file for a detailed description of the required ADT. There is one unusual feature in the Ballot class that is necessitated by the voting mechanism. As described above, once a candidate ranks the last in a given round, the references to that candidate are pruned from all the ballots. Hence the Ballot class needs to support removal of a given candidate, as well as peeking at the top candidate in the ranking in order to decide who the Ballot was cast for.
* `Candidate.py` is another abstraction that has not been implemented yet that you are expected to solve. The Candidate class should be a small implementation of the concept of a candidate. A candidate has a name which identifies her, and collects ballots cas for her into an internal linear collection. These ballots will be asked of a candidate to provide later when the vote tabulation occurs.
* `PollingStation.py` is the class where "rubber meets the road" as far as your team's implemenation is concerned. Examples of the operation of the PollingStation class are provided in the `VoteTesting.py` file. To conduct voting at a PollingStation one
   * first creates a list of candidates, and voters.
   * Then the PolingStation is initialized with the list of candidates.
   * The PollingStation scans the list of Voters asking each of them to cast the ballot that the PollingStation has provided (and pre-filled with the candidate list). The voter (for testing purposes) picks her ranking randomly and returns the ballot into a linear collection managed by the PollingStation.
   * The PollingStation tabulates then the votes and checks whether there is a candidate with a super-majority. If there is such a candidate, the PollingStation declares the winner.
   * If there is no candidate with super-majority, the PollingStation manages the rounds until only two candidates remain, and the candidate with the most votes among the two is declared the winner.

In the PollingStation class you are asked to implenent one method: `candidate_has_super_majority`. This method checks whether after the first tabulation there is a candidate who is the top choice for at least 50% of ballots. The method should raise an exception if no candididate has collected any ballots (i.e., when the sum of candidates' ballots is 0), return True if a candidate with supper-majority exists, and False otherwise.

In the `VoteTesting.py` you are asked to add two additional tests to see if your code works as expected. 
* In the first test you assume that there a two candidates "A" and "B" and four voters "a", "b", "c", and "d". The voters' rankings are respectively as follows  \[0, 1\], \[1, 0\], \[1, 0\], \[1, 0\] (i.e., voters "b", "c", "d" like the candidate "B" the most). Write a test that confirms that the winner will have a super-majority and that the winner is "B" with 3 votes.
* Do the same with candidates \[ "A", "B", "C"\], and voters \["a", "b", "c", "d", "e"\] who rank the candidates as follows:  \[0, 1, 2\], \[2, 1, 0\], \[2, 0, 1\], \[0, 1, 2\], \[1, 0, 2\]. Here there will be no candidate with a super-majority. After the rounds the winning candidate should be the candidate "B" with 3 votes.

When implementing the above tests, note that you will need to provide the ranking argument to 
`PollingStation.proces_vote(voter, ranking)` method. When that argument is not provided, the voter will choose a random ordering of the candidates.

Here are some details that the team has decided on.
   * For realistic simulations, the team decided that the Voters can  choose their rankings randomly. Hence in order obtain predictable results one needs to start any test involving voting with a call to random.seed(...) function (from the module random) to generate a random but fixed sequence of voters' rankings. They can also choose any given ranking they want, and they do that by explicitly specifying in the `PollingStation.proces_vote(...)` method the ranking they want.
   * In order to preserve the ballots of voters for possible recounts, the PollingStation copies them after the first tabulation into variables containing the particle "_surv" (for "surviving"). It is on those "_surv" variables that the voting rounds will be performed on (if needed). Such rounds alter the ballots and recounts could be impossible if the original votes were not preserved. They copying is done using the special copy module.
   * In order to keep the code simple, if two candidates obtain the same numbrer of votes in a round, we randomly choose the winner among them. This random choice is implicit: it is hidden in the sorting functions that are used in the framework. Whatever the candidate the sorting functions choose first, that will be the winner 

## Summary
* Implement the specifications in `Ballot.py`, `Candidate.py`, and `PollingStation.py` so that the tests in `VoteTesting.py` work.
* Add two new tests to `VoteTesting.py` 

## Submitting
Your task is to implment the required ADT so that the tests provided in `VoteTesting.py` file work. At a minimum, submit the following files:
   * `Voter.py`  (small file needed for the framework to work)
   * `Ballot.py` (implement the required ADT)
   * `Candidate.py` (implement the required ADT)
   * `PollingStation.py`(implement the function which checks for super-majority)
   * `VoteTesting.py`(add two tests for the voting process)


Students must submit to Mimir individually by the due date (typically, the Wednesday after this module at 11:59 pm EST) to receive credit.

## Grading

* 50 - `Ballot.py`
* 30 - `Candidate.py`
* 20 - `PollingStation.py`

## Feedback
If you have any feedback on this assignment, please leave it [here](https://s.uconn.edu/cse2050_feedback).

We check this feedback regularly, and it has resulted in many improvements.
