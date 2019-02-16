player_names = []
run_program = True

while run_program:
    user_response = input("Would you like to add players?")
# if user responds with yes below runs
    if user_response.lower() == "yes":
        player_name = input("Enter the name of the player to add to the team:")
        player_names.append(player_name.title())
    else:
        print(player_names)
        print("Number of players on the team: {}".format(len(player_names)))
        goal_keeper_index = int(input("Who will be the goalkeeper? Select a number from (1-{})".format(len(player_names))))
        goal_keeper = player_names[goal_keeper_index - 1]
        print("{} will be the goalkeeper!!".format(goal_keeper))
        break
