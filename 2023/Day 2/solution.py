def parse_input(input_text):
    games = []

    for game_str in input_text.splitlines():
        game_info = game_str.split(":")  
        game_number = int(game_info[0].split()[1]) 
        cube_data = game_info[1].strip().split(";")  

        game = {"game_number": game_number, "cubes": []}

        for cube_str in cube_data:
            cubes = cube_str.strip().split(",")
            cube_dict = {}

            for cube in cubes:
                parts = cube.strip().split()
                # if len(parts) == 2:
                count, color = parts
                cube_dict[color.lower()] = int(count)

            game["cubes"].append(cube_dict)

        games.append(game)

    return games

def isValidCube(cube):
    if 'red' in cube:
        if cube['red'] > 12:
            return False
    if 'green' in cube:
        if cube['green'] > 13:
            return False
    if 'blue' in cube:
        if cube['blue'] > 14:
            return False
    return True

input_text = open(0).read()
parsed_games = parse_input(input_text)
total = 0

for game in parsed_games:
    isValid = True
    game_num = game['game_number']
    for cube in game['cubes']:
        if not isValidCube(cube):
            isValid = False
            break
    if isValid:
        total += game_num

print(total)