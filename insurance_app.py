from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field,field_validator
from typing import Literal, Annotated
from Model.predict import predict_op,model,MODEL_VERSION
from Schema.predict_response import PredictionResponse
from Schema.user_input import UserInput


app = FastAPI()

# Third Improvement
 
@app.get('/')
def home():
    return {'message': 'Insurance Premium Prediction API'}

@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'Model_load': model is not None
    }

@app.post('/predict')
def predict_model(data: UserInput):
    user_input= {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    
    try:
        

        prediction = predict_op(user_input)

        return JSONResponse(status_code=200, content={'response': prediction})
    except Exception as e :
        return JSONResponse(status_code=500,content=str(e))