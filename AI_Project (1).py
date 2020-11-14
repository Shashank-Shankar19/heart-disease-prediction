import numpy as np
import csv
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination


#read Cleveland Heart Disease data
heartDisease = pd.read_csv('heart_1.csv')
heartDisease = heartDisease.replace('?',np.nan)

#display the data
print('Few examples from the dataset are given below')
print(heartDisease.head())

#Model Bayesian Network
Model=BayesianModel([('age','trestbps'),('age','fbs'),('sex','trestbps'),
	('exang','trestbps'),('trestbps','target'),('fbs','target'),
	('target','restecg'),('target','thalach'),('target','chol')])

#Learning CPDs using Maximum Likelihood Estimators
Model.fit(heartDisease,estimator=MaximumLikelihoodEstimator)

#Inferencing with Bayesian Network
HeartDisease_infer = VariableElimination(Model)

#Asking for input
age = input("Enter age:")
sex = int(input("Enter sex(0 for male,1 for female):"))
cp = int(input("Enter chest pain type(0,1,2 or 3):"))
trestbps = input("Enter resting blood pressure(in mm Hg):")
chol = input("Enter serum cholestrol(mg/dl):")
fbs = int(input("Enter fasting blood sugar(0 or 1):"))
restecg = int(input("Enter resting electrocardiographic result(0,1 or 2):"))
thalach = input("Enter maximum heart rate achieved:")
exang = int(input("Exercise induced angina(1 for yes, 0 for no):"))
oldpeak = float(input("ST depression induced by exercise relative to rest:"))

#convert a particular range of values to a single value
if int(age) <= 30:
	age = 0
elif int(age) > 30 and int(age) <= 40:
	age = 1
elif int(age) > 40 and int(age) <= 50:
	age = 2
elif int(age) > 50 and int(age) <= 60:
	age = 3
elif int(age) > 60 and int(age) <= 70:
	age = 4
elif int(age) > 70:
	age = 5

if int(trestbps) <= 120:
	trestbps = 0
elif int(trestbps) <=150:
	trestbps = 1
elif int(trestbps) <=180:
	trestbps = 2
else:
	trestbps = 3

if int(chol) < 150:
	chol = 0
elif int(chol) < 300:
	chol = 1
elif int(chol) < 450:
	chol = 2
elif int(chol) < 600:
	chol = 3
elif int(chol) >= 600:
	chol = 4


if int(thalach) < 100:
	thalach = 0
elif int(thalach) < 150:
	thalach = 1
elif int(thalach) < 200:
	thalach = 2
else:
	thalach = 3

if float(oldpeak) < 1:
	oldpeak = 0
elif float(oldpeak) < 2:
	oldpeak = 1
elif float(oldpeak) < 3:
	oldpeak = 2
elif float(oldpeak) < 4:
	oldpeak = 3
elif float(oldpeak) < 5:
	oldpeak = 4
elif float(oldpeak) < 6:
	oldpeak = 5
elif float(oldpeak) >= 6:
	oldpeak = 6

print("\n Probability of heart disease:")
#Executing the query formed from the given data against the dataset
q = HeartDisease_infer.query(variables=['target'], evidence = {'age' : age,'sex' : sex,'trestbps' : trestbps,'chol':chol,'fbs':fbs,'restecg':restecg,'thalach':thalach,'exang':exang})
print(q)
print("target(0) = Probability of not having heart disease \n target(1) = Probability of having heart disease")