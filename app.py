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
            TP2 = float(request.form['TP2']),
            TP3 = float(request.form['TP3']),
            H1 = float(request.form['H1']),
            Dv_pressure = float(request.form['DV_pressure']),
            Reservoirs = float(request.form['Reservoirs']),
            Oil_temperature = float(request.form['Oil_temperature']),
            Motor_current = float(request.form['Motor_current']),
            COMP = float(request.form['COMP']),
            Dv_electric = float(request.form['DV_eletric']),
            Towers = float(request.form['Towers']),
            MPG = float(request.form['MPG']),
            LPS = float(request.form['LPS']),
            Pressure_switch = float(request.form['Pressure_switch']),
            Oil_level = float(request.form['Oil_level'])
        )
    new_data = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(new_data)

    results = pred

    return render_template("results.html", final_result = results)

if __name__ == "__main__": 
    app.run(host = "0.0.0.0", debug= True)
    
#http://127.0.0.1:5000/ in browser