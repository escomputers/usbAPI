# Denkovi USB Relay Boards RestAPI
Simple REST API for controlling a local [USB Denkovi Relay Board](https://denkovi.com/relay-boards)


### Install
```bash
# Set up Python virtual environment
mkdir -p env
python -m venv env && source env/bin/activate
python -m pip install -r requirements.txt

# Change these lines inside usbapi.service file before copying it to /etc
#ExecStart=python /home/emiliano/usbAPI/main.py
#WorkingDirectory=/home/emiliano/usbAPI/
#Environment=PYTHONPATH=/home/emiliano/usbAPI/env/lib/python3.9/site-packages

sudo cp usbapi.service /etc/systemd/system/
sudo systemctl enable usbapi.service
sudo systemctl daemon-reload
sudo systemctl start usbapi.service

sudo systemctl status usbapi.service # verify it's working properly
```

### Optional steps (only for USB devices like Denkovi Relay Boards)
```bash
# Download Denkovi Relay Command Line Tool
wget http://denkovi.com/Software/DenkoviRelayCommandLineTool/Current-Version/DenkoviRelayCommandLineTool.zip

unzip DenkoviRelayCommandLineTool.zip

# Install JDK 1.8 
tar -xf jdk-8u361-linux-arm32-vfp-hflt.tar.gz
mv jdk1.8.0_361 java
sudo cp -r java/ /usr/bin/

# append this to $HOME/.bashrc at the end
export PATH="/usr/bin/java/bin:$PATH"
source ~/.bashrc

java -version # verify installation
```

### Example usage
```bash
curl http://localhost:8000/cooler/status
```

