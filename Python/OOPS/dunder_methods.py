class Playlist:
    def __init__(self, name, songs):
        self.name=name
        self.songs=songs

    def __str__(self):
        return f" Playlist {self.name} with {len(self.songs)} songs"
    
    def __len__(self):
        return len(self.songs)
    
myplaylist=Playlist("chill vibes",["sunflower","ocean","dreams"])
myplaylist2=Playlist("silent music",["shine","dlower"])

print(myplaylist)
print(len(myplaylist))

print(myplaylist2)
print(len(myplaylist2))