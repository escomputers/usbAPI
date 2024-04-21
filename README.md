## Denkovi USB Relay Boards RestAPI
Simple REST API for controlling a local [USB Denkovi Relay Board](https://denkovi.com/relay-boards)


### Requirements
1. Set your paths inside [usbapi.service](usbapi.service) file:
```bash
ExecStart=python /home/emiliano/usbAPI/main.py
WorkingDirectory=/home/emiliano/usbAPI/
Environment=PYTHONPATH=/home/emiliano/usbAPI/env/lib/python3.9/site-packages
```

2. Set your Relay Board type and HTTP Port inside [helpers/common.py file](helpers/common.py) (Optional) 


### Install
```bash
bash install.sh
```


### Usage
```bash
curl http://localhost:8000/1/status
# or
curl http://localhost:8000/1/on
curl http://localhost:8000/1/off
```

