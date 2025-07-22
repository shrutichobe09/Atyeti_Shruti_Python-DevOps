from app.core.processor import LogProcessor

def test_error_count():
    processor = LogProcessor()
    processor.process_line("2025-07-21 ERROR Something failed")
    assert processor.counts["ERROR"] == 1
     