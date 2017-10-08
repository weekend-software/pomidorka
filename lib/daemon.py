import sys
import os
import time
import signal

from lib.pomodoro import Pomodoro
from lib.notify import Notify


class Daemon(object):
    def __init__(self, logger, pidfile, data_fname):
        self.pidfile = pidfile
        self.data_fname = data_fname

        self.logger = logger

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
            signal.signal(s, self._exit)

    def _pidfile_check(self):
        if os.path.isfile(self.pidfile):
            self.logger("Looks like another instance is already running, check pidfile:\n  %s" % self.pidfile)
            sys.exit(1)

    def _pidfile_write(self):
        with open(self.pidfile, 'w+') as fp:
            fp.write(str(os.getpid()))

    def _pidfile_remove(self):
        if os.path.isfile(self.pidfile):
            os.remove(self.pidfile)

    def _exit(self, signum, frame):
        self._pidfile_remove()
        sys.exit(0)

    def run(self):
        n = Notify()

        self.logger("Watching pomidorkas ...")
        while True:
            p = Pomodoro(self.data_fname)

            if p.running:
                duration = p.duration()
                left = self.duration - p.duration()
                self.logger('Found running pomidorka, checking duration')
                if duration > self.duration:
                    self.logger('Pomidorka done, notifying and stopping')
                    n.send()
                    p.stop()
                else:
                    self.logger('Pomidorka is going for %s seconds, %s seconds left' % (str(duration), str(left)))
            else:
                self.logger('No running pomidorkas')

            time.sleep(self.loop_delay)
