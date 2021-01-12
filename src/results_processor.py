# This module processes the winner

def process_results(master_state_map, rigged_party="None"):
    """
    This function processes the election results
    :return:
    """
    voters = 0
    votes = 0
    reps = 0
    dems = 0
    party = ""
    for state_num, state_data in master_state_map.items():
        #print(f"state_num: {state_num}, this represents the item number in the dictionary.")
        #print(f"state_data: {state_data}, this contains all the state data")
        #print(state_data)
        for key, value in state_data.items():
            if key == 'state':
                #print(f"state: {value}")
                i = 0
            elif key == 'num_voters':
                #print(f"num_voters: {value}")
                voters += value
            elif key == 'party':
                #print(f"party: {value}")
                party = value
            elif key == 'votes':
                #print(f"votes: {value}")
                if party == 'republican':
                    votes += value
                elif party == 'democrat':
                    votes += value
                else:
                    voters = 0
            elif key == 'electorate':
                #print(f"electorate: {value}")
                if party == 'republican':
                    reps += value
                elif party == 'democrat':
                    dems += value

    if rigged_party == "None":
        if reps > dems:
            print(f"\nRepublicans - {reps} electorate points, {votes} votes out of {voters} voters.")
        else:
            print(f"\nDemocrats - {dems} electorate points, {votes} votes out of {voters} voters.")
    else:
        if rigged_party == 'Democrat':
            print(f"\n{rigged_party} - {reps} electorate points, {votes} votes out of {voters} voters.")
        elif rigged_party == 'Republican':
            print(f"\n{rigged_party} - {reps} electorate points, {votes} votes out of {voters} voters.")
        elif rigged_party == 'Libertarian':
            print(f"\n{rigged_party} - {reps} electorate points, {votes} votes out of {voters} voters.")
        elif rigged_party == 'Independent':
            print(f"\n{rigged_party} - {reps} electorate points, {votes} votes out of {voters} voters.")