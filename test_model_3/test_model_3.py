from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import List


class Inputs(BaseModel):
    text: List[str]
    files: List[str]
    storage_url: str

app=FastAPI()

model_info =   {
                "input": [
                    # "text"
                    "text","text",
                    "text","text","text","text","text","text"
                ],
                "output": [
                    "string"
                ],
                "desc": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",
                "instructions": [
                    "string",
                    "string",
                    "string",
                    "string"
                ]
                } 

@app.post('/predict')
async def model_result(inputs:Inputs):
    return {"result":"","statement":""}

@app.get('/info')
async def get_info():
    return model_info


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)