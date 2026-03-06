import logging
import unittest
from lesson_13.homework_10 import log_event


class TestLogger(unittest.TestCase):
    def test_logger_success(self):
        with self.assertLogs("log_event", level="INFO") as cm:
            log_event('', 'success')
        self.assertEqual(cm.records[0].levelno, logging.INFO)
        self.assertEqual(len(cm.records), 1)

    def test_logger_expired(self):
        with self.assertLogs("log_event", level="WARNING") as cm:
            log_event('', 'expired')
        self.assertEqual(cm.records[0].levelno, logging.WARNING)
        self.assertEqual(len(cm.records), 1)

    def test_logger_error(self):
        with self.assertLogs("log_event", level="ERROR") as cm:
            log_event('', 'failed')
        self.assertEqual(cm.records[0].levelno, logging.ERROR)
        self.assertEqual(len(cm.records), 1)


if __name__ == '__main__':
    unittest.main()