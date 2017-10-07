import time

class Pomodoro(object):
    def __init__(self, fname):
        self.fname = fname

        data = self._read()
        self.running = bool(int(data[0]))
        self.started = float(data[1])
        self.log = [i.split(':') for i in data[2].split(',')] if len(data[2]) > 1 else []

    def _read(self):
        open(self.fname, 'a').close()  # touch
        data = open(self.fname, 'rb+').read()
        data = filter(None, data.strip())
        if not data:
            data = "0;0.0;"
        return data.split(';')

    def _write(self):
        data = ';'.join([
            str(int(self.running)),
            str(float(self.started)),
            ','.join([':'.join(i) for i in self.log])
        ])
        with open(self.fname, 'w+') as fp:
            return fp.write(data)

    save = _write

    def start(self):
        if self.running:
            return False
        self.running = True
        self.started = time.time()
        return self._write()

    def stop(self):
        if not self.running:
            return True
        self.log.append([str(self.started), str(self.duration())])
        self.running = False
        self.started = 0.0
        return self._write()

    def duration(self):
        if not self.running:
            return 0
        return time.time() - self.started
