# Copyright 2025 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

FROM debian:12
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -yq --no-install-recommends \
    vim \
    nano \
    tree \
    htop \
    unzip \
    ca-certificates \
    openssl \
    python3 \
    python3-dev \
    python3-wheel \
    libyaml-dev \
    binutils \
    make \
    csh \ 
    g++ \
    sed \
    gawk \
    wget \
    autoconf \
    automake \
    autotools-dev \
    binutils-arm-linux-gnueabi \
    gcc-10-arm-linux-gnueabi \
    qemu-user-static

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade build
RUN rm -f get-pip.py
RUN mkdir /gen_arm32asm/
RUN mkdir /tests/
COPY gen_arm32asm /gen_arm32asm/
COPY setup.py /
COPY setup.cfg /
COPY pyproject.toml /
COPY MANIFEST.in /
COPY README.md /
COPY LICENSE /
COPY requirements.txt /
COPY tests /tests/
RUN pip3 install -r requirements.txt
RUN rm -f requirements.txt
RUN python3 -m build --no-isolation --wheel
RUN pip3 install /dist/gen_arm32asm-*-py3-none-any.whl
RUN rm -rf /gen_arm32asm/
RUN rm -rf dist/ tests/
RUN rm -f setup.cfg
RUN rm -f pyproject.toml
RUN rm -f MANIFEST.in
RUN rm -f setup.py
RUN rm -f README.md
RUN rm -f LICENSE

