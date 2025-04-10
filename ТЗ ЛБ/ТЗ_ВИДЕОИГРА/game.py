class Game:
    def __init__(self, game_id: int, name: str, price: int, players: int, comm: int, id_developer: int):
        self.game_id = game_id
        self.name = name
        self.price = price
        self.players = players
        self.comm = comm
        self.id_developer = id_developer

    def __str__(self):
        return f"{self. game_id}. {self.name} {self.price} {self.players} {self.comm}"

if __name__ == '__main__':
        gam = []
        with open("games.txt", "r", encoding="ansi") as games_f:
            for line in games_f:
                game_id, id_developer, name, price, players, comm = line.split(";")
                game_id = int(game_id)
                name = str(name)
                price = int(price)
                players = int(players)
                comm = int(comm)
                gams = Game(game_id, name, price, players, comm, id_developer)
                gam.append(gams)