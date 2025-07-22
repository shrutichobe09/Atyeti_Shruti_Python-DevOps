from app.core.collector import LogCollector
from app.core.processor import LogProcessor
from app.core.alerter import AlertManager
from app.db.database import SessionLocal, init_db
from app.db.models import AlertLog

def main():
    init_db()
    log_path = "app/logs/sample.log"

    collector = LogCollector(log_path, follow=False)  # ⬅️ follow=False for test
    processor = LogProcessor()
    alerter = AlertManager(threshold=3)
    db = SessionLocal()

    for line in collector.read_log():
        print(f"Line: {line}")
        counts = processor.process_line(line)
        error_count = counts.get("ERROR", 0)
        if alerter.should_alert(error_count):
            msg = f"High ERROR count: {error_count}"
            alerter.send_alert(error_count)
            db.add(AlertLog(message=msg))
            db.commit()
            break  # Optional: stop after first alert for test mode

if __name__ == "__main__":
    main()
