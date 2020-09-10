#!/bin/bash
set -euo pipefail
export MAKEFLAGS="-j4"

function cmakebuild() {
  cd $1
  if [[ ! -z "${2:-}" ]]; then
    git checkout $2
  fi
  mkdir build
  cd build
  cmake ..
  make
  make install
  cd ../..
  rm -rf $1
}

cd /tmp

STATIC_PACKAGES="libboost-chrono1.67.0 libboost-date-time1.67.0 libboost-filesystem1.67.0 libboost-program-options1.67.0 libboost-regex1.67.0 libboost-test1.67.0 libboost-serialization1.67.0 libboost-thread1.67.0 libboost-system1.67.0 python3-numpy python3-mako"
BUILD_PACKAGES="git cmake make gcc g++ libboost-dev libboost-chrono-dev libboost-date-time-dev libboost-filesystem-dev libboost-program-options-dev libboost-regex-dev libboost-test-dev libboost-serialization-dev libboost-thread-dev libboost-system-dev"

apt-get update
apt-get -y install --no-install-recommends $STATIC_PACKAGES $BUILD_PACKAGES

git clone https://github.com/EttusResearch/uhd.git
# 3.15.0.0 Release
mkdir -p uhd/host/build
cd uhd/host/build
git checkout v3.15.0.0
cmake ..
make
make install
cd ../../..
rm -rf uhd

git clone https://github.com/pothosware/SoapyUHD.git
cmakebuild SoapyUHD 3488a7f994b0d10e50cd3b542cfc7cab9d2d9c05

SUDO_FORCE_REMOVE=yes apt-get -y purge --autoremove $BUILD_PACKAGES
apt-get clean
rm -rf /var/lib/apt/lists/*
