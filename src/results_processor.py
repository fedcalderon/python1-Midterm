# This module processes the winner

def process_results(master_state_map):
    """
    This function processes the election results
    :return:
    """
    for state_num, state_data in master_state_map.items():
        print(state_data)