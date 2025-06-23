class MusicPlayer:    
    def play_song(self,song_name):
        print(f"playing song {song_name}")

class DeviceController:
    def turn_on_device(self,device_name):
        print(f" turn on device {device_name}")

class SmartAssistant(MusicPlayer,DeviceController):
    def respond_to_command(self, command_type,value):
        if command_type=="music":
            self.play_song(value)
        elif command_type=="device":
            self.turn_on_device(value)

assistant= SmartAssistant()
assistant.respond_to_command("music","Senorita")
assistant.respond_to_command("device","living room light")