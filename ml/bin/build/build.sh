#! /bin/bash

pip3 install --upgrade pip
pip3 install --no-cache-dir -r build/requirements.txt

mkdir ml repos databases thirdparty

apt-get --assume-yes install default-jre

apt-get --assume-yes install unzip
bash build/install-jsymbolic.sh
