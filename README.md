# usbAPI
simple restAPI for controlling local USB device


### install
```
mkdir -p env
python -m venv env && source env/bin/activate
python -m pip install -r requirements.txt
cp uvicorn.service /etc/systemd/system/
sudo systemctl enable uvicorn.service
sudo systemctl daemon-reload
sudo systemctl start uvicorn.service
```


### example usage
```
curl http://localhost:8000/cooler/status
```

