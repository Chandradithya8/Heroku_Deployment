import numpy as np 
from flask import Flask,request,render_template
import pickle

app = Flask(__name__)
model=pickle.load(open('diabetes_prediction.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features=[x for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction = model.predict(final_features)
     
    if prediction==0:
        a= 'CONGRATULATIONS! YOU DONT HAVE DIABETES'
    else:
        a= 'OOPS! YOU HAVE DAIBETES'   

    return render_template('index.html', prediction_text=a)


if __name__ == '__main__':
    app.run(debug=True)