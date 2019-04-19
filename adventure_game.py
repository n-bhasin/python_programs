location = {0: {"desc": "sitting in front of computer",
                "exit": {},
                "nameExit": {}},
            1: {"desc": "You are on Road",
                "exit": {"W": 2,  "E": 3,  "N": 5,  "S": 4,  "Q": 0},
                "nameExit": {"2": 2, "3": 3, "5": 5, "4": 4}},
            2: {"desc": "You are on Hill",
                "exit": {"N": 5, "Q": 0},
                "nameExit": {"5": 5}},
            3: {"desc": "You are on Building",
                "exit": {"W": 1, "Q": 0},
                "nameExit": {"1": 1}},
            4: {"desc": "You are on Valley",
                "exit": {"W": 2,  "N": 1,  "Q": 0},
                "nameExit": {"2": 2, "1": 1}},
            5: {"desc": "You are on Forest",
                "exit": {"W": 2, "2": 2, "S": 1, "Q": 0},
                "nameExit": {"2": 2, "1": 1}}
            }

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}

loc = 1
while True:
    availableExits = ", ".join(location[loc]["exit"].keys())
    print(location[loc]["desc"])

    if loc == 0:
        break
    else:
        allExits = location[loc]["exit"].copy()
        allExits.update(location[loc]["nameExit"])

    direction = input("Available Exits are: "+ availableExits + "\nEnter the exit you want to take: \t").upper()
    print()

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            direction = vocabulary[word]
            break

    if direction in allExits:
        loc = allExits[direction]

    else:
        print("Sorry, we do not have this direction.")
