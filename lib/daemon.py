import sys
import os
import time
import signal

from lib.pomodoro import Pomodoro
from lib.notify import Notify


class Daemon(object):
    def __init__(self, pidfile):
        self.pidfile = pidfile

        self.duration = 25 * 60
        self.loop_delay = 5

        self._pidfile_check()
        self._pidfile_write()

        signals = (
            signal.SIGTERM,
            signal.SIGQUIT,
            signal.SIGINT
        )
        for s in signals:
            signal.signal(s, self._pidfile_remove)

    def _pidfile_check(self):
        if os.path.isfile(self.pidfile):
            print("Looks like another instance is already running, check pidfile:\n  %s" % self.pidfile)
            sys.exit(1)

    def _pidfile_write(self):
        with open(self.pidfile, 'w+') as fp:
            fp.write(str(os.getpid()))

    def _pidfile_remove(self, signum, frame):
        if os.path.isfile(self.pidfile):
            os.remove(self.pidfile)
        sys.exit(0)

    def run(self):
        p = Pomodoro()
        n = Notify()

        print("Watching pomidorkas ...")
        while True:
            if p.running and p.duration() > self.duration:
                n.send()
                p.stop()
            time.sleep(self.loop_delay)
