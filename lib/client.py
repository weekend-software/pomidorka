from lib.pomodoro import Pomodoro


class Client(object):
    def __init__(self, daemon_pidfile, data_fname):
        self.daemon_pidfile = daemon_pidfile

        self.p = Pomodoro(data_fname)

    def start(self):
        duration = int(self.p.duration() / 60)
        if self.p.running:
            print("Another pomidorka is already running for %i minutes, stop it first." % duration)
        else:
            print("New pomidorka!")
            self.p.start()

    def stop(self):
        duration = int(self.p.duration() / 60)
        if self.p.running:
            print("Pomidorka done! It took %i minutes." % duration)
            self.p.stop()
        else:
            print("Nothing to stop.")

    def status(self):
        duration = int(self.p.duration() / 60)
        if self.p.running:
            print("Is running for %i minutes." % duration)
        else:
            print("No pomidorkas running.")
