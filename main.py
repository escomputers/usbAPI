import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()

class App:
    @staticmethod
    def get_current_status(relay_port):
        command = f"/usr/bin/java/bin/java -jar /home/emiliano/DenkoviRelayCommandLineTool/DenkoviRelayCommandLineTool.jar DAE06Lcq 8 {relay_port} status"
        status = int(os.popen(command).read())
        return status

    @staticmethod
    def turn_on(relay_port):
        command = f"/usr/bin/java/bin/java -jar /home/emiliano/DenkoviRelayCommandLineTool/DenkoviRelayCommandLineTool.jar ID=0 8 {relay_port} 1"
        os.system(command)

    @staticmethod
    def turn_off(relay_port):
        command = f"/usr/bin/java/bin/java -jar /home/emiliano/DenkoviRelayCommandLineTool/DenkoviRelayCommandLineTool.jar ID=0 8 {relay_port} 0"
        os.system(command)


@app.get("/{relay_port}/status")
async def get_status(relay_port: int):
    status = App.get_current_status(relay_port)
    return {"status": status}

@app.post("/{relay_port}/on")
async def post_turn_on(relay_port: int):
    App.turn_on(relay_port)
    return {"message": "Device turned on"}

@app.post("/{relay_port}/off")
async def post_turn_off(relay_port: int):
    App.turn_off(relay_port)
    return {"message": "Device turned off"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="info")

