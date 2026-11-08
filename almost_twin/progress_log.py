"""Human-readable progress for slow metadata and generation requests.

Logs are emitted only when the CLI enables this logger; importing the runner
as a library keeps the normal quiet behavior for tests and integrations.
"""

import logging
import threading
from contextlib import contextmanager
from time import monotonic


progress = logging.getLogger('almost_twin.progress')
progress.addHandler(logging.NullHandler())
progress.propagate = False


def enable_progress():
    """Show progress immediately on stderr, including when stdout is buffered."""
    previous_level = progress.level
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('[progress] %(message)s'))
    progress.addHandler(handler)
    progress.setLevel(logging.INFO)
    return previous_level, handler


def restore_progress(previous):
    """Do not leave library calls verbose after a CLI invocation finishes."""
    previous_level, handler = previous
    progress.removeHandler(handler)
    progress.setLevel(previous_level)


@contextmanager
def timed_progress(label, heartbeat_seconds=20):
    """Log start, wait heartbeats, and completion/failure around one slow step."""
    if not progress.isEnabledFor(logging.INFO):
        yield
        return
    started = monotonic()
    stop = threading.Event()

    def heartbeat():
        while not stop.wait(heartbeat_seconds):
            progress.info('Still waiting on %s (%.0fs elapsed)', label, monotonic() - started)

    progress.info('Starting %s', label)
    worker = threading.Thread(target=heartbeat, daemon=True)
    worker.start()
    try:
        yield
    except BaseException:
        progress.info('Stopped %s after %.1fs (not successful)', label, monotonic() - started)
        raise
    else:
        progress.info('Finished %s in %.1fs', label, monotonic() - started)
    finally:
        stop.set()
        worker.join()
