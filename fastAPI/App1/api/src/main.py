# sample code file.
from typing import Union
from fastapi import FastAPI

app = FastAPI()



# defining a sample path.
@app.get("/health")
def api_health():
    return {'status': "Active"}
