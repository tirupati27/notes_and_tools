#!bin/bash

#Defining a function to seperate the message prints
message(){
  echo -e "\n\033[1;95m=================================\033[0m\n\033[1;91m  $1\033[0m\n\033[1;95m=================================\033[0m\n"
}

clear



ln -sf /storage/emulated/0 ~/0
message "ShortCut of the directory 'storage/emulated/0' created in the Ubuntu's Home directory as 0"

apt upadate
apt upgrade -y
apt clean
message "Package update and upgrade Done!"

apt install -y r-base
message "r-base installed successfully inside the ubuntu!"

apt upadate
apt upgrade -y
apt clean
message "Package update and upgrade Done Again!"

python file_distributor_for_termux_setup
message "Done: All setup files distributed to their locations!"

cp /data/data/com.termux/files/home/a ~
message "python file 'a' saved to the Ubuntu's Home directory!"

message "Ubuntu/Termux Setup done!\n\tEnjoy both!"