from fastapi import FastAPI, HTTPException, Depends
import pandas as pd
from pydantic import BaseModel
import joblib
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
model = joblib.load("model.pkl")
security = HTTPBasic()

class DataInput(BaseModel):
    data: list

@app.post("/predict")
def predict(data_input: DataInput, credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "password":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    try:
        df = pd.DataFrame(data_input.data)
        predictions = model.predict(df)
        return {"predictions": predictions.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
