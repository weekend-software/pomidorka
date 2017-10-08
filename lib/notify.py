import subprocess


class Notify(object):
    def __init__(self, logger):
        self.logger = logger

    def send(self):
        subprocess.Popen(['notify-send', '--expire-time=5000', '--icon=emblem-important', 'Pomidorka done!', 'Get a break for a few minutes and then get back to work.'])
        self.logger.info("Pomidorka done!")
