from collections import defaultdict

class LogProcessor:
    def __init__(self):
        self.counts = defaultdict(int)

    def process_line(self, line):
        if "ERROR" in line:
            self.counts["ERROR"] += 1
        elif "WARNING" in line:
            self.counts["WARNING"] += 1
        elif "INFO" in line:
            self.counts["INFO"] += 1
        return self.counts
