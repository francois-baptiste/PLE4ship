# PLE4ship

![Games](ple_games.jpg?raw=True "Games!")

**PLE4ship** is a fork of [**PyGame Learning Environment (PLE)**](https://github.com/ntasfi/PyGame-Learning-Environment) to create a naval environement to train and evaluate autonomous agents to avoid collisions.


## Installation

PLE requires the following dependencies:
* numpy
* pygame
* pillow

Clone the repo and install with pip.

```bash
git clone https://github.com/francois-baptiste/PyGame-Learning-Environment.git
cd PyGame-Learning-Environment/
pip install -e .
``` 

## Run PyGame-Learning-Environment on Docker

### Setup
`wget http://raw.githubusercontent.com/francois-baptiste/PyGame-Learning-Environment/master/docker/Dockerfile`

### Build PLE image
`docker build -t ple4ship .`

##### UBUNTU:  
`docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix \
  -e DISPLAY=unix$DISPLAY ple4ship /bin/bash`

##### MAC:
in a separate window run:  
  `brew install socat`  
  `socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"`

finally, run `ifconfig` and look for the ip of vboxnet0, say `192.168.99.1`  

  `docker run -i -t -e DISPLAY=192.168.99.1:0 ple4ship /bin/bash`

### Usage:
  `cd ple/games`  
  `python waterworld.py`


## Updating

`cd` into the `PyGame-Learning-Environment` directory and run the following:

```bash
git pull
```

## Headless Usage

Set the following in your code before usage:
```python
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.environ["SDL_VIDEODRIVER"] = "dummy"
```

Thanks to [@wooridle](https://github.com/ntasfi/PyGame-Learning-Environment/issues/26#issuecomment-289517054).


## Todos
 * Write a specific documentation for the fork.
 * Use a physical model for the ship (for instance [the one from ShipAI](https://github.com/jmpf2018/ShipAI))
 * Create a bridge to [OpenCPN](https://opencpn.org/) (AIS UDP stream or fake GPSd)
 * More tests
 * And more!


## Citing PLE

If PLE has helped your research please cite it in your publications. Example BibTeX entry:

```
@misc{tasfi2016PLE,
  author = {Tasfi, Norman},
  title = {PyGame Learning Environment},
  year = {2016},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ntasfi/PyGame-Learning-Environment}}
}
```
