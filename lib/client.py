import datetime
import math

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

    def log_show(self):
        data = self.p.log_show()
        print("Started at       Duration")
        print("-------------------------")

        total = 0
        date_last = ""

        for p_item in data:
            # https://stackoverflow.com/questions/9744775/
            dt = str(datetime.datetime.fromtimestamp(int(float(p_item[0]))))
            date = dt.split(' ')[0]
            if date == date_last:
                date = " " * 10
            else:
                date_last = date
            time = dt.split(' ')[1][:-3]
            duration = math.ceil(float(p_item[1]) / 60.0)
            total += duration
            print("%s %s + %2i min" % (date, time, duration))

        print("-------------------------")
        print("Total:            %3i min" % (total))
