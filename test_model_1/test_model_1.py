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
                    "image","image","image","image"
                ],
                "output": [
                    "string"
                ],
                "desc": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
                "instructions": [
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
    uvicorn.run(app, host="0.0.0.0", port=8001)