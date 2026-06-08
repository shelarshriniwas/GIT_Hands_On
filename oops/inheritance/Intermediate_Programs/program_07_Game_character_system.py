# program_07_Game_character_system.py

class Player:

    def login(self):

        print("Player Logged In")


class Sniper(Player):

    def weapon(self):

        print("Sniper Uses Rifle")


obj = Sniper()

obj.login()
obj.weapon()