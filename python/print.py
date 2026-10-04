class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")
    def add_song(self, song):
        self.songs.append(song)
        print(f"'{song}' added to the playlist {self.name}.")
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed from the playlist {self.name}.")
        else:
            print(f"'{song}' is not in the playlist {self.name}.")
    def display_songs(self):
        print(f"\n--- {self.name} ({self.genre}) ---")
        if self.songs:
            for i, song in enumerate(self.songs, 1):
                print(f"  {i}. {song}")
            else:
                print("No songs in the playlist; Add some songs to enjoy your playlist!")
    def __del__(self):
        print(f"Playlist '{self.name}' is deleted. Bye!")
my_playlist = Playlist ("Road trip mix", "Lofi beats")
while True:
    print("\n1. Add song\n2. Remove song\n3. Display songs\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        song = input("Enter the song name to add: ")
        my_playlist.add_song(song)
    elif choice == "2":
        song = input("Enter the song name to remove: ")
        my_playlist.remove_song(song)
    elif choice == "3":
        my_playlist.display_songs()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
