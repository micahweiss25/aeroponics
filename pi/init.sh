echo "UPDATING SYSTEM"
apt install upgrade
apt install update

echo "DOWNLOADING PYTHON3 AND PIP"
apt install python3
apt install pip3

echo "DOWNLOADING DEPENDENCIES"
sudo apt-get install python3-dev libmysqlclient-dev
pip3 install mysqlclient
pip3 install RPi.GPIO

