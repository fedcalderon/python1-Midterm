from random import seed
from random import randint


def get_random_total_num_voters():
    """
    This function obtains a random number which represents
    the population who voted.
    :return: random sample of voters
    """
    min_num_people_who_voted = 1_000
    max_num_people_who_voted = 10_000
    seed(randint(1, 17))
    value = randint(min_num_people_who_voted, max_num_people_who_voted)
    return value


def get_random_number(population):
    """
    For the purpose of this exercise, only 4 types of parties are considered. However, this is theoretical and does
    not correlate with actual historical data. This function must be modified in order to provide a historically
    accurate type of vote.
    This method generates a random number list which represents votes for a party.
    0: democrat
    1: republican
    2: libertarian
    3: independent
    4: invalid
    :return: a list of random numbers between 0 and 4
    """

    percent_factor = 0.95
    majority = int(population * percent_factor)
    minority = population - majority

    #print(majority)
    #print(minority)

    majority_vote_list = get_majority_votes(majority)
    minority_vote_list = get_minority_votes(minority)

    zeroes = 0
    ones = 0
    for m in majority_vote_list:
        if m == 0:
            zeroes += 1
        elif m == 1:
            ones += 1

    #print(f"democrats={zeroes}")
    #print(f"republicans={ones}")

    twos = 0
    threes = 0
    fours = 0
    for m in minority_vote_list:
        if m == 2:
            twos += 1
        elif m == 3:
            threes += 1
        elif m == 4:
            fours += 1

    #print(f"independent={twos}")
    #print(f"libertarians={threes}")
    #print(f"invalid={fours}")

    # print(majority_vote_list)
    # print(minority_vote_list)

    votes = []
    votes = majority_vote_list + minority_vote_list

    return votes


def get_majority_votes(population):
    votes = []
    seed()
    min_value_possible = 0
    max_value_possible = 1
    for _ in range(population):
        value = randint(min_value_possible, max_value_possible)
        votes.append(value)
    return votes


def get_minority_votes(population):
    votes = []
    seed()
    min_value_possible = 2
    max_value_possible = 4
    for _ in range(population):
        value = randint(min_value_possible, max_value_possible)
        votes.append(value)
    return votes