#!/bin/bash

# permissions
sudo chmod 775 ./scripts/make-stations/assets/*
sudo chmod 775 ./scripts/make-stations/build/*
sudo chmod 775 ./scripts/make-stations/*

# copy packs from git
sudo mkdir -p /mnt/RADIO/_Stations
sudo cp -r ./packs/stations/ /mnt/SDCARD/_Stations

current_dir=$PWD;cd /mnt/SDCARD/_Stations/stations/us/tn/bna/;sudo python import.py;cd $current_dir;
current_dir=$PWD;cd /mnt/SDCARD/_Stations/stations/uk/eng/lhr/;sudo python import.py;cd $current_dir;

# other tasks