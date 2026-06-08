# program_03_Media_player_project.py

class AudioPlayer:

    def play(self):

        print("Playing Audio")


class VideoPlayer:

    def play(self):

        print("Playing Video")


players = [AudioPlayer(), VideoPlayer()]

for player in players:

    player.play()