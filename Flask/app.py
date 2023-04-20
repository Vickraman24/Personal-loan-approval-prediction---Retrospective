from flask import Flask,render_template, request
import numpy as np
import pandas
import os
import pickle


app = Flask(__name__)
model = pickle.load(open(r'rdf.pkl','rb'))

#scale = pickle.load(open(r'scale.pkl','rb'))

@app.route('/')
def home():
    return render_template('predict.html')
    
    
@app.route('/Submit',methods=["POST","GET"])
def submit():
     input_features = [int(x) for x in request.form.values() ]
     input_features =[np.arrays(input_features)]  
     print(input_features)
     names = ['Gender',
              'Married',
              'Dependents',
              'Education',
              'Self_Employed',
              'Applicant_Income',
              'CoapplicantIncome',
              'LoanAmount',
              'Loan_Amount_Term',
              'Credit_History',
              'Property_Area']
     data = pandas.DataFrames(input_features,columns=names)
     print(data)
     prediction = model.predict(data)
     print(prediction)
     prediction = int(prediction)
     print(type(prediction))

     if(prediction == 0):
         return render_template("predict.html",result = "Loan will Not be Approved")
     else:
        return render_template("predict.html",result = "Loan will be Approved") 

if __name__ == "__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(debug = False)

