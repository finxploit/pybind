FROM archlinux/base

LABEL maintainer="dimitar.petrov@finxploit.com"

ENV PYENV_ROOT /root/.pyenv
ENV PATH /root/.pyenv/shims:/root/.pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV PYTHON_VERSIONS 3.6.6 3.7.0
ENV PIPENV_VENV_IN_PROJECT 1
ENV PIPENV_DONT_LOAD_ENV=1

WORKDIR /build

RUN pacman --noconfirm -Syyu \
    && pacman --noconfirm -S \
       base-devel \
       git \
       curl \
       python-pip \
       python-pipenv \
       # python-docker \
       bzip2 \
       expat \
       gdbm \
       libffi \
       openssl \
       zlib \
       bluez-libs \
       libnsl \
       sqlite \
       valgrind \
       xz \
       tk \
       libsm \
       tesseract-data-eng \
       tesseract \
       tzdata \
       pandoc \
       hdf5 \
       # ansible \
       docker \
       openssh \
       snappy \ 
       mpfr \ 
       gcc-fortran \
    && rm -rf /var/cache/pacman/pkgs/*

RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen

ENV LC_ALL en_US.utf-8
ENV LANG en_US.utf-8

# Install python with pyenv and testing requirements
RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash \
    && pyenv install --list \
    && yes | for version in $PYTHON_VERSIONS; do pyenv install $version; done \
    && pip install --upgrade pip pipenv setuptools tox tox-pyenv

# Add local pypi server for private dependencies
RUN mkdir /root/.pip \
    && echo '[global]' > /root/.pip/pip.conf \
    && echo 'trusted-host = pypi.finxploit.com' >> /root/.pip/pip.conf \
    && echo 'index-url = https://pypi.finxploit.com' >> /root/.pip/pip.conf
