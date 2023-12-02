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
                count, color = parts
                cube_dict[color.lower()] = int(count)

            game["cubes"].append(cube_dict)

        games.append(game)

    return games

# Example usage:
# input_text = """
# Game 1: 4 green, 7 blue; 2 blue, 4 red; 5 blue, 2 green, 2 red; 1 green, 3 red, 9 blue; 3 green, 9 blue; 7 green, 2 blue, 2 red
# Game 2: 1 blue, 2 red; 1 green, 2 blue, 1 red; 1 red, 5 green; 3 red, 2 blue, 8 green; 3 blue, 2 red, 4 green; 2 blue, 4 green, 3 red
# Game 3: 7 red, 7 blue, 9 green; 15 green, 4 red, 8 blue; 3 green, 12 blue, 6 red
# """

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
    max_red = 0
    max_green = 0
    max_blue = 0
    for cube in game['cubes']:
        if 'red' in cube:
            max_red = max(max_red, cube['red'])
        if 'green' in cube:
            max_green = max(max_green, cube['green'])
        if 'blue' in cube:
            max_blue = max(max_blue, cube['blue'])
    total += max_red * max_green * max_blue

print(total)