mkdir -p env
python -m venv env && source env/bin/activate
python -m pip install -r requirements.txt

sudo cp usbapi.service /etc/systemd/system/
sudo systemctl enable usbapi.service
sudo systemctl daemon-reload
sudo systemctl start usbapi.service

sudo systemctl status usbapi.service