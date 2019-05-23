# VERSION:        0.1
# DESCRIPTION:    PLE
# AUTHOR:         Eder Santana <edercsjr@gmail.com>
# COMMENTS:
#     Pygame learning environment
# SETUP:
#   # Download PLE4ship Dockerfile
#   wget ...
#
#   # Build atom image
#   docker build -t ple .
#
#   UBUNTU:
#   docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix \
#       -e DISPLAY=unix$DISPLAY ple /bin/bash
#
#   MAC:
#   in a separate window run:
#       brew install socat
#       socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
#   finally:
#       run ifcongi and look for the ip of vboxnet0, say 192.168.99.1
#       docker run -i -t -e DISPLAY=192.168.99.1:0 ple /bin/bash
#
# USAGE:
#   cd ple4ship/games
#   python waterworld.py


FROM ubuntu:18.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update
RUN apt-get install -y \
  sudo vim man less git wget bzip2 build-essential \
  ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 \
    libsdl-image1.2-dev \
    libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev \
    libsmpeg-dev \
    libsdl1.2-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    libplib-dev \
    libopenal-dev \
    libalut-dev \
    libvorbis-dev \
    libxxf86vm-dev \
    libxmu-dev \
    libgl1-mesa-dev \
    git

RUN apt-get update && apt-get install -y wget && wget https://raw.githubusercontent.com/q3aql/ffmpeg-install/master/ffmpeg-install && chmod a+x ffmpeg-install && ./ffmpeg-install --install release


# install miniconda
ENV CONDA_PATH /opt/miniconda3
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc


RUN git clone --single-branch --depth 1 https://github.com/francois-baptiste/PLE4ship.git /src/PLE4ship \
   && cd /src/PLE4ship \
   && /opt/conda/bin/pip install -r requirements.txt \
   && /opt/conda/bin/pip install .

WORKDIR /src/PLE4ship

CMD ["/opt/conda/bin/python", "ple4ship/games/waterworld.py"]