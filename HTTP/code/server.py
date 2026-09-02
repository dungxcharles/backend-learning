from fastapi import FastAPI
import uvicorn

app = FastAPI()

host = "127.0.0.1"

@app.get("/user-profiles")
def get_profile():
    return {
        "name": "Charles",
        "age": 18,
        "major": "student",
        "cpa": 4.0,
        "friend": "Tom Holland"
    }


if __name__ == "__main__":
    uvicorn.run("server:app", host=host, port=5000)