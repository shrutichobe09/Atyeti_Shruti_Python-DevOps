class AlertManager:
    def __init__(self, threshold=5):
        self.threshold = threshold

    def should_alert(self, error_count):
        return error_count >= self.threshold

    def send_alert(self, error_count):
        print(f"[ALERT] Too many errors! Count: {error_count}")
        # Later: send email, GCP PubSub, Slack etc.
