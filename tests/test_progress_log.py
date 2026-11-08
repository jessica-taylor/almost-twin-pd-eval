import logging
import time
import unittest

from almost_twin.progress_log import enable_progress, progress, restore_progress, timed_progress


class ProgressLogTests(unittest.TestCase):
    def test_start_heartbeat_finish(self):
        with self.assertLogs(progress, level='INFO') as captured:
            with timed_progress('mock slow request', heartbeat_seconds=0.002):
                time.sleep(0.075)
        messages = '\n'.join(captured.output)
        self.assertIn('Starting mock slow request', messages)
        self.assertIn('Still waiting on mock slow request', messages)
        self.assertIn('Finished mock slow request', messages)

    def test_error_is_logged_and_reraised(self):
        with self.assertLogs(progress, level='INFO') as captured:
            with self.assertRaisesRegex(RuntimeError, 'synthetic failure'):
                with timed_progress('mock failed request'):
                    raise RuntimeError('synthetic failure')
        self.assertIn('Stopped mock failed request', '\n'.join(captured.output))

    def test_is_quiet_when_disabled(self):
        previous = progress.level
        try:
            progress.setLevel(logging.WARNING)
            with timed_progress('nothing to log'):
                pass
        finally:
            progress.setLevel(previous)

    def test_cli_logging_does_not_leak_after_command(self):
        previous_level = progress.level
        previous_handlers = tuple(progress.handlers)
        state = enable_progress()
        try:
            self.assertEqual(progress.level, logging.INFO)
            self.assertEqual(len(progress.handlers), len(previous_handlers) + 1)
        finally:
            restore_progress(state)
        self.assertEqual(progress.level, previous_level)
        self.assertEqual(tuple(progress.handlers), previous_handlers)


if __name__ == '__main__':
    unittest.main()
