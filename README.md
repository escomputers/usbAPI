# usbAPI
Simple restAPI for controlling a local USB device


### Install
```bash
# Create Python virtual environment
mkdir -p env
python -m venv env && source env/bin/activate
python -m pip install -r requirements.txt

# Change uvicorn.service paths before copying it to /etc
cp uvicorn.service /etc/systemd/system/
sudo systemctl enable uvicorn.service
sudo systemctl daemon-reload
sudo systemctl start uvicorn.service
```


### example usage
```
curl http://localhost:8000/cooler/status
```

