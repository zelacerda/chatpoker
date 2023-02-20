# chatpoker
A terminal-based video poker game written in Python.

This game implements the ["Jacks or Better"](https://en.wikipedia.org/wiki/Video_poker#Jacks_or_Better) video poker version and runs entirely on terminal, with some nice colors and simple graphics.

![Game Screen](./assets/screen.png)

## Requisites

**chatpoker** was only tested on my machine (Linux with Manjaro distro) with Python 3.10.9 version, but probably will work on previous versions.

A terminal compatible with ANSI escape code and UFT-8 font is necessary to render colors and suit symbols used in the cards (♣ ♥ ♠ ♦).

Since the game not uses third party libraries, you don't need any virtual environment neither `requirements.txt` file. Just clone this repo, run the `poker.py` file on terminal and have fun :)

```
git clone https://github.com/zelacerda/chatpoker.git
```

```
cd chatpoker
```

```
python poker.py
```

## Docker version

There's also a [Docker version on Docker Hub](https://hub.docker.com/r/zelacerda/chatpoker/tags) that you can use without install any file or dependency. Use the command below to pull the image and run the containerized version:

```
docker run --rm -it zelacerda/chatpoker
```

Feel free to use, modify and distribute!

**version 1.0 - 2023 - by zelacerda**
