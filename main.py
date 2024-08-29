from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(debug=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

favicon_path = 'static/images/favicon.ico'


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@app.get("/")
def read_root():
    return {"hi": "hello world!"}


@app.get("/greet/")
def read_greeting_query(name: str = Query(None,
                                          title="Hello api",
                                          example="John Doe",
                                          description="Enter your name")):
    """ My description of API"""
    if name is None:
        return {"message": f"hello!"}
    return {"message": f"hello, {name}",
            "name as query param": name
            }


@app.get("/greet/{name}/")
def read_greeting_url(name):
    return {"message": f"hello, {name}",
            "name as part URL": name
            }
