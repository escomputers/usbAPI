"""Script that spawns a REST API server and translates HTTP requests
to system calls for dealing with a USB device"""
import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()


class App:
    """Main Class that defines functions as methods"""

    @staticmethod
    def get_current_status(relay_port):
        """Function that gets the Status for a specific relay port
        on USB device via a system call"""
        command = f"/usr/bin/java/bin/java -jar /home/emiliano/usbcli/DenkoviRelayCommandLineTool.jar DAE06Lcq 8 {relay_port} status"
        status = int(os.popen(command).read())

        return status

    @staticmethod
    def turn_on(relay_port):
        """Function that executes command ON for a specific relay port
        on USB device via a system call"""
        command = f"/usr/bin/java/bin/java -jar /home/emiliano/usbcli/DenkoviRelayCommandLineTool.jar ID=0 8 {relay_port} 1"
        os.system(command)

    @staticmethod
    def turn_off(relay_port):
        """Function that execute command OFF for a specific relay port
        on USB device via a system call"""
        command = f"/usr/bin/java/bin/java -jar /home/emiliano/usbcli/DenkoviRelayCommandLineTool.jar ID=0 8 {relay_port} 0"
        os.system(command)


@app.get("/{relay_port}/status")
async def get_status(relay_port: int) -> dict:
    """Get Status async function"""
    status = App.get_current_status(relay_port)
    return {"status": status}


@app.post("/{relay_port}/on")
async def post_turn_on(relay_port: int) -> dict:
    """Turn ON async function"""
    App.turn_on(relay_port)
    return {"message": "Device turned on"}


@app.post("/{relay_port}/off")
async def post_turn_off(relay_port: int) -> dict:
    """Turn OFF async function"""
    App.turn_off(relay_port)
    return {"message": "Device turned off"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="info")
