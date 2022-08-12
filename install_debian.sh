sudo apt update -y
sudo apt upgrade -y
sudo apt install apt-transport-https -y
sudo tee /etc/apt/sources.list.d/notesalexp.list<<EOF
deb https://notesalexp.org/tesseract-ocr5/$(lsb_release -cs)/ $(lsb_release -cs) main
EOF
wget -O - https://notesalexp.org/debian/alexp_key.asc | sudo apt-key add
sudo apt update -y
sudo apt upgrade -y
sudo apt install tesseract-ocr -y
