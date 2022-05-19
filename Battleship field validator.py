def validate_battlefield(field):
    ships_true = {
        "battleship": 1,
        "cruiser": 2,
        "destroyers": 3,
        "submarines": 4
    }

    ships = {
        "battleship": 0,
        "cruiser": 0,
        "destroyers": 0,
        "submarines": 0
    }

    coordinats = {
        "0": [],
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": []
    }

    for horizontal_list in range(len(field)):
        # print(horizontal_list)
        for area in range(len(field[horizontal_list])):
            # print(area)
            if field[horizontal_list][area] == 1:
                coordinats[str(horizontal_list)].append(area)

    


    return coordinats
    # return True if ships == ships_true else False

battleField =   [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(validate_battlefield(battleField))