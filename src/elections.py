# Imports

# from module import <function 1, function 2>
from src.states import get_electorate_values_per_state, get_states
from src.randomizing_factors import get_random_total_num_voters, get_random_number
from src.results_processor import process_results

print("This is an election computing model program.")


class Elections:
    """
    This class models an election program. The following websites may be used as a reference for historical
    data analysis on party victories:
    1) https://www.statista.com/statistics/1035521/popular-votes-republican-democratic-parties-since-1828/
    2) https://en.wikipedia.org/wiki/List_of_United_States_presidential_elections_by_popular_vote_margin.
    """
    def __init__(self):
        # Define constants
        self.REPUBLICAN = 'republican'
        self.DEMOCRAT = 'democrat'
        self.LIBERTARIAN = 'libertarian'
        self.INDEPENDENT = 'independent'
        self.INVALID = 'invalid'
        # Define program variables
        self.master_state_map = {}

    def run_model(self):
        self.start_state_voting()
        self.show_winner()

    def run_vote(self, population):
        """
        This method runs the voting process for a given population size and returns a winner
        :param population: the number of people who voted
        :return: the winner party
        """
        democrat_counter = 0
        republican_counter = 0
        libertarian_counter = 0
        independent_counter = 0
        invalid_counter = 0

        # Define state tally dictionary
        state_tally = {}
        # Get a list of random numbers representing votes for candidate parties
        votes = get_random_number(population)
        # Define how each vote number corresponds to a party
        tallies = {
            0: self.DEMOCRAT,
            1: self.REPUBLICAN,
            2: self.LIBERTARIAN,
            3: self.INDEPENDENT,
            4: self.INVALID
        }
        # For each vote number in votes, compute the vote
        for vote in votes:
            #state_tally = self.compute_votes(tallies[vote_num])
            if tallies[vote] == self.DEMOCRAT:
                democrat_counter += 1
            # If the vote is republican, increment republican counter
            elif tallies[vote] == self.REPUBLICAN:
                republican_counter += 1
            # If the vote is independent, increment independent counter
            elif tallies[vote] == self.LIBERTARIAN:
                libertarian_counter += 1
            # If the vote is other, increment other counter
            elif tallies[vote] == self.INDEPENDENT:
                independent_counter += 1
            # If the vote is none of the above, increment democrat counter
            else:
                invalid_counter += 1
        winner = {}
        votes = [republican_counter, democrat_counter, libertarian_counter, independent_counter]
        votes.sort(reverse=True)
        highest = votes[0]
        if highest == republican_counter:
            winner[self.REPUBLICAN] = highest
        elif highest == democrat_counter:
            winner[self.DEMOCRAT] = highest
        elif highest == libertarian_counter:
            winner[self.LIBERTARIAN] = highest
        elif highest == independent_counter:
            winner[self.INDEPENDENT] = highest
        elif highest == invalid_counter:
            winner[self.INVALID] = highest
        return winner

    def start_state_voting(self):
        counter = 0
        # Outer loop: states
        for state in get_states():
            state_map = {}
            num_voters = get_random_total_num_voters()
            state_tally = self.run_vote(num_voters)
            party = ''
            votes = 0
            # Inner loop: stat data
            for key,value in state_tally.items():
                party = key
                votes = value
            state_map['state'] = state
            state_map['num_voters'] = num_voters
            state_map['party'] = party
            state_map['votes'] = votes
            state_map['electorate'] = get_electorate_values_per_state(state)
            self.master_state_map[counter] = state_map
            counter += 1

    def show_winner(self):
        """This method computes which party won"""
        print("And the winner is ... ")
        process_results(self.master_state_map)
