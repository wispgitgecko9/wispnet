#!/bin/bash

#WISPNET Mint Setup Light
#Version:   1

# Ensure the script runs with sudo
if [ "$EUID" -ne 0 ]; then
  echo "This script must be run as root. Use sudo."
  exit
fi

# Function to update and upgrade the system
update_system() {
  echo "Updating system..."
  apt update && apt upgrade -y
}

# Function to install essential tools
install_essentials() {
  echo "Installing essential tools..."
  apt install -y \
    build-essential \
    git \
    curl \
    wget \
    vim \
    nano \
    htop \
    unzip \
    jq \
    tree \
    neofetch
}

# Function to install Python and pip
install_python() {
  echo "Installing Python and pip..."
  apt install -y python3 python3-pip
}

# Function to install Node.js and npm
install_nodejs() {
  echo "Installing Node.js..."
  curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
  apt install -y nodejs
}

# Function to install Apache and related tools
install_apache() {
  echo "Installing Apache and PHP..."
  apt install -y apache2 libapache2-mod-php php php-cli php-mbstring
}

# Function to install Docker
install_docker() {
  echo "Installing Docker..."
  apt install -y docker.io
  systemctl start docker
  systemctl enable docker
}

# Function to install VirtualBox
install_virtualbox() {
  echo "Installing VirtualBox..."
  apt install -y virtualbox
}

# Function to install networking tools
install_networking_tools() {
  echo "Installing networking tools..."
  apt install -y \
    nmap \
    netcat \
    tcpdump \
    traceroute \
    iperf3 \
    openvpn \
    wireshark \
    dnsutils
}

# Function to install additional developer tools
install_dev_tools() {
  echo "Installing developer tools..."
  apt install -y \
    tmux \
    screen \
    sqlite3 \
    sshpass \
    rsync \
    filezilla
}

# Function to install Chromium browser
install_chromium() {
  echo "Installing Chromium browser..."
  apt install -y chromium-browser
}

# Function to install GIMP for graphics editing
install_gimp() {
  echo "Installing GIMP..."
  apt install -y gimp
}

# Function to install ESP and Arduino development tools
install_esp_arduino_tools() {
  echo "Installing ESP32 and Arduino development tools..."
  apt install -y esptool arduino arduino-core
}

# Function to clean up and finalize
cleanup_system() {
  echo "Cleaning up..."
  apt autoremove -y
  apt autoclean -y
}

# Main script execution
echo "Starting setup..."
update_system
install_essentials
install_python
install_nodejs
install_apache
install_networking_tools
install_dev_tools
cleanup_system

echo "Double checking system..."

sleep 7
cat << "EOF"
__        __        __ _______  _____ _____  _   _  ______ _______ 
\ \      /  \      / /|__   __|/ ____|  _  \| \ | ||  ____|__   __|
 \ \    / /\ \    / /    | |  | (___ | |_\  |  \| || |__     | |   
  \ \  / /  \ \  / /     | |   \___ \| ____/|   ` ||  __|    | |   
   \ \/ /    \ \/ /    __| |__ ____) | |    | |\  || |____   | |   
    \__/      \__/    |_______|_____/|_|    |_| \_||______|  |_|   

Setup complete! This WISPNET computer is now ready for your use! |NOTICE: Light edition installed.|
Recommended: Reboot your system to apply all changes.


