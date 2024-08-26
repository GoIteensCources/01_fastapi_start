import uvicorn
from home_route import read_calc


if __name__ == "__main__":
    uvicorn.run(app="main:app",
                host="0.0.0.0",
                port=8800,
                reload=True,
                # workers=2
                )
