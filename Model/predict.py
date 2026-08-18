import pandas as pd
import pickle

with open('Model/model.pkl', 'rb') as f:
    model = pickle.load(f)
    
MODEL_VERSION = "1.0.1"

class_labels = model.steps[-1][1].classes_.tolist()

def predict_op(user_input: dict):
    input_df = pd.DataFrame([user_input])
    
    predicted_class = model.predict(input_df)[0]
    
    probablities = model.predict_proba(input_df)[0]
    confidence = max(probablities)
    
    class_probs = dict(zip(class_labels,map(lambda p : round(p,4),probablities))) 
    
    
    
    return {
        "predicted category": predicted_class,
        "confidence":round(confidence,4),
        "class_probablities":class_probs
        
    }