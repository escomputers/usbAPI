import os
from fastapi import FastAPI
import uvicorn

app = FastAPI()


class App:
    def get_current_status():
        status = int(os.popen("/usr/bin/java/bin/java -jar /home/emiliano/DenkoviRelayCommandLineTool/DenkoviRelayCommandLineTool.jar DAE06Lcq 8 8 status").read())
        return status


    def turn_on():
        os.system("/usr/bin/java/bin/java -jar /home/emiliano/DenkoviRelayCommandLineTool/DenkoviRelayCommandLineTool.jar ID=0 8 8 1")


    def turn_off():
        os.system("/usr/bin/java/bin/java -jar /home/emiliano/DenkoviRelayCommandLineTool/DenkoviRelayCommandLineTool.jar ID=0 8 8 0")


@app.get("/cooler/status")
async def get_status():
    status = App.get_current_status()
    return {"status": status}

@app.post("/cooler/on")
async def post_turn_on():
    App.turn_on()
    return {"message": "Device turned on"}

@app.post("/cooler/off")
async def post_turn_off():
    App.turn_off()
    return {"message": "Device turned off"}


if __name__ == "__main__":
    uvicorn.run("main:app", log_level="info")