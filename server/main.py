from fastapi import FastAPI
from config import get_config

app = FastAPI()

# To do: use environment variables to get the proper configs
# All we have at the moment is app.debug, which can't be set
# from the uvicorn command line
config = get_config(debug = app.debug, testing = False)

@app.get("/")
def read_root():
    return {}