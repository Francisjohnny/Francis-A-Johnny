game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]
        new_enemy = enemies[2]

    print(new_enemy)