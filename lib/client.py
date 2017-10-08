from lib.pomodoro import Pomodoro


class Client(object):
    def __init__(self, logger, daemon_pidfile, data_fname):
        self.daemon_pidfile = daemon_pidfile

        self.logger = logger

        self.p = Pomodoro(data_fname)

    def start(self):
        duration = int(self.p.duration() / 60)
        if self.p.running:
            self.logger.info("Another pomidorka is already running for %i minutes, stop it first." % duration)
        else:
            self.logger.info("New pomidorka!")
            self.p.start()

    def stop(self):
        duration = int(self.p.duration() / 60)
        if self.p.running:
            self.logger.info("Pomidorka done! It took %i minutes." % duration)
            self.p.stop()
        else:
            self.logger.info("Nothing to stop.")

    def status(self):
        duration = int(self.p.duration() / 60)
        if self.p.running:
            self.logger.info("Is running for %i minutes." % duration)
        else:
            self.logger.info("No pomidorkas running.")
