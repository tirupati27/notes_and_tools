#!bin/bash

#Defining a function to seperate the message prints
message(){
  echo -e "\n\033[1;95m=================================\033[0m\n\033[1;91m  $1\033[0m\n\033[1;95m=================================\033[0m\n"
}

clear

termux-setup-storage
message "Storage permission Granted"

ln -sf /storage/emulated/0 ~/0
message "ShortCut of the directory 'storage/emulated/0' created in the Home directory as 0"


pkg update
pkg upgrade -y
apt clean
pkg clean
rm -rf ~/.cache/*
message "Package update and upgrade Done!"

pkg install python
pkg install matplotlib
pip install flask
pip install requests
message "Python with (matplotlib, numpy, flask, requests) installed successfully!"

pkg install git
pkg install termux-api
message "Git and Termux-api installed successfully!"

pkg install proot-distro -y
proot-distro install ubuntu
message "proot-distro and Ubuntu installed successfully!"

pkg update
pkg upgrade -y
apt clean
pkg clean
rm -rf ~/.cache/*
message "Package update and upgrade Done Again!"

message "Termux Setup done!\n\tNow Login and complete the Ubuntu setup!"