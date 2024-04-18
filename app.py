from flask import Flask, request, render_template, jsonify

from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')
    
@app.route('/predict', methods = ['POST', "GET"])
def predict_datapoint(): 
    if request.method == "GET": 
        return render_template("form.html")
    else: 
        data = CustomData(
            TP2 = float(request.form.get('TP2')),
            TP3 = float(request.form.get('TP3')),
            H1 = float(request.form.get('H1')),
            DV_pressure = float(request.form.get('DV_pressure')),
            Reservoirs = float(request.form.get('Reservoirs')),
            Oil_temperature = float(request.form.get('Oil_temperature')),
            Motor_current = float(request.form.get('Motor_current')),
            COMP = float(request.form.get('COMP')),
            DV_eletric = float(request.form.get('DV_eletric')),
            Towers = float(request.form.get('Towers')),
            MPG = float(request.form.get('MPG')),
            LPS = float(request.form.get('LPS')),
            Pressure_switch = float(request.form.get('Pressure_switch')),
            Oil_level = float(request.form.get('Oil_level'))
            
        )

    

    new_data = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(new_data)

    results = pred

    return render_template("results.html", final_result = results)

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", debug= True)
    
#http://127.0.0.1:5000/ in browser