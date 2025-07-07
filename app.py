from fastapi import FastAPI, UploadFile, File

from pdf_ingester.pipeline import process_upload

app = FastAPI(title="PDF Phone Extractor")


@app.post("/ingest")
async def ingest_pdf(file: UploadFile = File(...)):
    numbers = await process_upload(file)
    return {"phones": numbers}
