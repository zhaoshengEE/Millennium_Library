"""
Program a function that
* Accept two arrays of players and returns an array of the players who play in both sports
* Run in just O(N + M)

Magical Lookup via Hash Table

1. Iterate through the first array:
    1. Store each player's name into a hash table
2. Iterate through the second array:
    1. If the name already shows up in the hash table:
        1. Append this name to the name list
3. Print out the name list
"""

def find_common_players(array1, array2):
    table = {}
    name_list = []

    for player in array1:
        table[player["first_name"] + ' ' + player["last_name"]] = True
    
    for player in array2:
        if table.get(player["first_name"] + ' ' + player["last_name"]):
            name_list.append(player["first_name"] + ' ' + player["last_name"])
    
    print(name_list)


if __name__ == "__main__":
    basketball_players = [
        {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
        {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
        {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
        {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
        {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"},
    ]

    football_players = [
        {"first_name": "Hanzla", "last_name": "Radosti", "team": "32evrs"},
        {"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
        {"first_name": "Alex", "last_name": "Patel", "team": "32evrs"},
        {"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
        {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"},
    ]

    find_common_players(basketball_players, football_players)