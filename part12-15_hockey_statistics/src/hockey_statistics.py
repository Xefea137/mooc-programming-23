# Write your solution here
import json

class FileHandler:
    def __init__(self, filename: str):
        self.filename = filename

    def read_data(self):
        with open(self.filename) as file:
            return json.loads(file.read())

class Player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = self.goals + self.assists

    def __str__(self):
        return f"{self.name:21}{self.team:3}{self.goals:4} + {self.assists:2} = {self.points:3}"

class PlayerManagement:
    def __init__(self):
        self.player_dictionary = {}

    def file_managenment(self, name: str):
        for player in FileHandler(name).read_data():
            self.player_dictionary[player['name']] = Player(player['name'], player['nationality'], player['assists'], player['goals'], player['penalties'], player['team'], player['games'])
        
        return len(self.player_dictionary)

    def player_detail(self, player_name: str):
        return self.player_dictionary[player_name]

    def get_team_names(self):
        return [value.team for value in self.player_dictionary.values()]

    def get_country_names(self):
        return [value.nationality for value in self.player_dictionary.values()]

    def players_of_team(self, team_name: str):
        return sorted([player for player, value in self.player_dictionary.items() if value.team == team_name], 
        key = self.points_scored, reverse = True)

    def players_from_country(self, country_name: str):
        return sorted([player for player, value in self.player_dictionary.items() if value.nationality == country_name], 
        key = self.points_scored, reverse = True)
        
    def most_points(self, amount: int):
        return sorted(
            sorted(
                [player for player, value in self.player_dictionary.items()], 
                key = lambda x: self.player_dictionary[x].goals, reverse = True), 
                key = lambda x: self.player_dictionary[x].points, reverse = True)[:amount]

    def most_goals(self, amount: int):
        return sorted(
            sorted(
                [player for player, value in self.player_dictionary.items()],
                key = lambda x: self.player_dictionary[x].games),
                key = lambda x: self.player_dictionary[x].goals, reverse = True)[:amount]

    def points_scored(self, player: list):
        return self.player_dictionary[player].points

class PlayerApplication:
    def __init__(self):
        self.player = PlayerManagement()
        
    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def execute(self):
        self.file_details()
        self.help()
        while True:
            print()
            command = int(input("commands: "))
            if command == 0:
                break
            elif command == 1:
                self.search_for_player_by_name()
            elif command == 2:
                self.team_names()
            elif command == 3:
                self.country_names()
            elif command == 4:
                self.players_in_team()
            elif command == 5:
                self.players_in_country()
            elif command == 6:
                self.players_most_points()
            elif command == 7:
                self.players_most_goals()

    def file_details(self):
        file_name = input("file name: ")
        length = self.player.file_managenment(file_name)
        print(f"read the data of {length} players\n")

    def search_for_player_by_name(self):
        player_name = input("name: ")
        print(self.player.player_detail(player_name))

    def team_names(self):
        team_names = self.player.get_team_names()
        for name in sorted(set(team_names)):
            print(name)

    def country_names(self):
        country_names = self.player.get_country_names()
        for name in sorted(set(country_names)):
            print(name)

    def players_in_team(self):
        team = input("team: ")
        players = self.player.players_of_team(team)
        for player in players:
            print(self.player.player_dictionary[player])

    def players_in_country(self):
        country = input("country: ")
        country = self.player.players_from_country(country)
        for player in country:
            print(self.player.player_dictionary[player])

    def players_most_points(self):
        amount = int(input("how many: "))
        players = self.player.most_points(amount)
        for player in players:
            print(self.player.player_dictionary[player])

    def players_most_goals(self):
        amount = int(input("how many: "))
        players = self.player.most_goals(amount)
        for player in players:
            print(self.player.player_dictionary[player])

x = PlayerApplication()
x.execute()