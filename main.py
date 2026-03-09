#import FastAPI
from fastapi import FastAPI

#Initiate it
app =FastAPI()

#Define the root endpoint
@app.get("/")
def read_root():
    return{"Hello": "World"}