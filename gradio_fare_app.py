
import gradio as gr

# Replace with real model intercept and coefficients
intercept = 2.5
coefs = [2.0, 0.3]  # trip_distance, trip_duration

def predict_fare(distance, duration):
    fare = intercept + coefs[0]*distance + coefs[1]*duration
    return round(fare, 2)

iface = gr.Interface(
    fn=predict_fare,
    inputs=[
        gr.Number(label="Trip Distance (miles)"),
        gr.Number(label="Trip Duration (minutes)")
    ],
    outputs=gr.Number(label="Predicted Fare ($)"),
    title="NYC Taxi Fare Predictor",
    description="Enter trip distance and duration to predict fare amount."
)

iface.launch()
