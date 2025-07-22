import time
import os

class LogCollector:
    def __init__(self, file_path, follow=True):
        self.file_path = file_path
        self.follow = follow  # default: True for tailing

    def read_log(self):
        with open(self.file_path, 'r') as f:
            if self.follow:
                f.seek(0, os.SEEK_END)  # Tail mode
                while True:
                    line = f.readline()
                    if not line:
                        time.sleep(0.2)
                        continue
                    yield line.strip()
            else:
                # Read whole file at once (test mode)
                for line in f:
                    yield line.strip()
