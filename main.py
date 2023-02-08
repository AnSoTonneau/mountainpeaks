from fastapi import FastAPI

from db import MountainPeak, database

app = FastAPI(title="API for mountain peaks retrieving")


@app.get("/")
async def read_root():
    return await MountainPeak.objects.all()


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await MountainPeak.objects.get_or_create(name="K8", lon=64.58, lat=556.4, altitude=8000)


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()

'''
@app.get("/")
def read_root():
    return {"Mountain Peaks API": "Ready"}


@app.get("/peaks/{peak_id}")
def read_peak(peak_id: int, q: Union[str, None] = None):
    return {"peak_id": peak_id, "q": q}

@app.put("/peaks/{peak_id}")
def update_peak(peak_id: int, peak: MountainPeak):
    return {"peak_name": peak.name, "peak_id": peak_id}

@app.post("/peaks/{peak_id}")
def create_peak(peak_id: int, peak: MountainPeak):
    return {"peak_name": peak.name, "peak_id": peak_id}

@app.delete("/peaks/{peak_id}")
def delete_peak(peak_id: int):
    return {"peak_id": peak_id}

@app.get("/peaks")
def get_peaks():
    return ["peak1", "peak2"]
'''
