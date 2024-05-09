## Denkovi USB Relay Boards RestAPI
Simple REST API for controlling a local [USB Denkovi Relay Board](https://denkovi.com/relay-boards)


### Requirements
1. Check your paths inside [usbapi.service](usbapi.service) file (especially the Python virtual environment path)

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

