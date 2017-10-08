# Pomidorka

A tool to use [pomodoro technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) in daily work.

## Usage

Don't forget to put daemon to autostart, see Installation section for details.

```
$ pomidorka --daemon &
Starting daemon mode.

$ pomidorka start
New pomidorka!

$ pomidorka
Is running for 22 minutes.

$ pomidorka stop
Pomidorka done! It took 22 minutes.

$ pomidorka log
Started at       Duration
-------------------------
2017-10-08 11:20 + 17 min
           11:37 + 23 min
           14:54 + 10 min
           15:04 + 19 min
           15:24 + 11 min
           16:06 +  4 min
           16:12 + 26 min
-------------------------
Total:            110 min
```

## Installation

I'm not using packaging here cause it's too expensive to support packaging software for high number of great systems currently available. Let me know if you have simple yet flexible way to solve this issue.

For now, just place executable somewhere inside `${PATH}` and provide daemon autostart in manner suitable for your system. Here's an example for [Elementary OS](https://elementary.io/):

```
git clone https://github.com/weekend-software/pomidorka.git ~/.pomidorka
cd ~/.pomidorka

# Install executable
sudo ln -s ~/.pomidorka/pomidorka /usr/local/bin/pomidorka

# Provide autostart
cp ./misc/pomidorka.desktop ~/.config/autostart/pomidorka.desktop
```
