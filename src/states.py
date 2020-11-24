"""This module returns states data."""


def get_electorate_values_per_state(state):
    """
    This function returns the electorate value per state
    :param state: State string being inquired
    :return: The electorate value
    """
    electorate = {
        'Alabama': 9,
        'Alaska': 3,
        'Arizona': 11,
        'Arkansas': 6,
        'California': 55,
        'Colorado': 9,
        'Connecticut': 7,
        'Delaware': 3,
        'District_of_Columbia': 3,
        'Florida': 29,
        'Georgia': 16,
        'Hawaii': 4,
        'Idaho': 4,
        'Illinois': 20,
        'Indiana': 11,
        'Iowa': 6,
        'Kansas': 6,
        'Kentucky': 8,
        'Louisiana': 8,
        'Maine': 4,
        'Maryland': 10,
        'Massachusetts': 11,
        'Michigan': 16,
        'Minnesota': 10,
        'Mississippi': 6,
        'Missouri': 10,
        'Montana': 3,
        'Nebraska': 5,
        'Nevada': 6,
        'NewHampshire': 4,
        'NewJersey': 14,
        'NewMexico': 5,
        'NewYork': 29,
        'NorthCarolina': 15,
        'NorthDakota': 3,
        'Ohio': 18,
        'Oklahoma': 7,
        'Oregon': 7,
        'Pennsylvania': 20,
        'RhodeIsland': 4,
        'SouthCarolina': 9,
        'SouthDakota': 3,
        'Tennessee': 11,
        'Texas': 38,
        'Utah': 6,
        'Vermont': 3,
        'Virginia': 13,
        'Washington': 12,
        'WestVirginia': 5,
        'Wisconsin': 10,
        'Wyoming': 3
    }
    points = electorate[state]
    return points


def get_states():
    """
    This function returns a list of all US states
    :return: a list of all US states
    """
    states = [
        'Alabama',
        'Alaska',
        'Arizona',
        'Arkansas',
        'California',
        'Colorado',
        'Connecticut',
        'Delaware',
        'District_of_Columbia',
        'Florida',
        'Georgia',
        'Hawaii',
        'Idaho',
        'Illinois',
        'Indiana',
        'Iowa',
        'Kansas',
        'Kentucky',
        'Louisiana',
        'Maine',
        'Maryland',
        'Massachusetts',
        'Michigan',
        'Minnesota',
        'Mississippi',
        'Missouri',
        'Montana',
        'Nebraska',
        'Nevada',
        'NewHampshire',
        'NewJersey',
        'NewMexico',
        'NewYork',
        'NorthCarolina',
        'NorthDakota',
        'Ohio',
        'Oklahoma',
        'Oregon',
        'Pennsylvania',
        'RhodeIsland',
        'SouthCarolina',
        'SouthDakota',
        'Tennessee',
        'Texas',
        'Utah',
        'Vermont',
        'Virginia',
        'Washington',
        'WestVirginia',
        'Wisconsin',
        'Wyoming'
    ]
    return states