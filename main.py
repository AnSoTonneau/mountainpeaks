from fastapi import FastAPI, HTTPException
import asyncpg

from db import MountainPeak, database
import ormar

app = FastAPI(title="API for mountain peaks retrieving")

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create dummy entries
    await MountainPeak.objects.get_or_create(name="Everest", lat=27.988056, lon=86.925278, altitude=8849)
    await MountainPeak.objects.get_or_create(name="K2", lat=35.8825, lon=76.513333, altitude=8611)
    await MountainPeak.objects.get_or_create(name="Mont Blanc", lat=45.832778, lon=6.865, altitude=4696)
    await MountainPeak.objects.get_or_create(name="Pic du Midi de Bigorre", lat=42.936389, lon=0.142778, altitude=2877)

@app.get("/")
def read_root():
    return {"Mountain Peaks API": "Ready"}

@app.get("/peaks")
async def read_peaks():
    return await MountainPeak.objects.all()

@app.get("/peaks/{peak_id}")
async def read_peak(peak_id: int):
    try:
        return await MountainPeak.objects.get(MountainPeak.id == peak_id)
    except ormar.exceptions.NoMatch:
        raise HTTPException(status_code=404, detail=f"Peak {peak_id} not found")

@app.put("/peaks/{peak_id}")
async def update_peak(peak_id: int, peak: MountainPeak):
    peak_db = await MountainPeak.objects.get(MountainPeak.id == peak_id)
    return await peak_db.update(**peak.dict())

@app.post("/peaks")
async def create_peak(peak: MountainPeak):
    try:
        await peak.save()
        return peak
    except asyncpg.exceptions.UniqueViolationError:
        raise HTTPException(status_code=400, detail=f"Peak name {peak.name} or id {peak.id} already exists")

@app.delete("/peaks/{peak_id}")
async def delete_peak(peak_id: int):
    try:
        peak_db = await MountainPeak.objects.get(MountainPeak.id == peak_id)
        await peak_db.delete()
        return peak_db
    except ormar.exceptions.NoMatch:
        raise HTTPException(status_code=404, detail=f"Peak {peak_id} not found")


@app.get("/peaks/list/")
async def read_geoloc(lat_min: float, lat_max: float, lon_min: float, lon_max: float):
    books = await MountainPeak.objects.filter((MountainPeak.lat >= lat_min) & (MountainPeak.lat <= lat_max) &
                                              (MountainPeak.lon >= lon_min) & (MountainPeak.lon <= lon_max)).all()
    return books

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
