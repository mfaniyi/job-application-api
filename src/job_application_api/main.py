from fastapi import FastAPI


app = FastAPI(title="Job Application API")


@app.get("/")
def read_root():
    return {"message":"Job Application API is running"}