import csv
import numpy as np
import pandas as pd


def convert_row( row ):
	row_dict = {}
	for key, value in row.items():
	    keyAscii = key.encode('ascii', 'ignore' ).decode()
	    valueAscii = value.encode('ascii','ignore').decode()
	    row_dict[ keyAscii ] = valueAscii
	return row_dict

#open new dataset
f = open('heart_1.csv','w')
writer = csv.writer(f)
#writing the field names
writer.writerow(['age', 'sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target'])


fieldnames = ['age', 'sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target']
writer = csv.DictWriter(f, fieldnames=fieldnames)

with open('heart.csv', newline='') as file:
	reader = csv.DictReader(file)
	for row in reader:
        #convert fieldnames from utf-8 format to ascii format
		row = convert_row(row)
        #convert a particular range of values to a single value
		if int(row['age']) <= 30:
			age = 0
		elif int(row['age']) > 30 and int(row['age']) <= 40:
			age = 1
		elif int(row['age']) > 40 and int(row['age']) <= 50:
			age = 2
		elif int(row['age']) > 50 and int(row['age']) <= 60:
			age = 3
		elif int(row['age']) > 60 and int(row['age']) <= 70:
			age = 4
		elif int(row['age']) > 70:
			age = 5
		sex = int(row['sex'])
		cp = int(row['cp'])
		if int(row['trestbps']) <= 120:
			trestbps = 0
		elif int(row['trestbps']) <=150:
			trestbps = 1
		elif int(row['trestbps']) <=180:
			trestbps = 2
		else:
			trestbps = 3
		if int(row['chol']) < 150:
			chol = 0
		elif int(row['chol']) < 300:
			chol = 1
		elif int(row['chol']) < 450:
			chol = 2
		elif int(row['chol']) < 600:
			chol = 3
		elif int(row['chol']) >= 600:
			chol = 4
		fbs = int(row['fbs'])
		restecg = int(row['restecg'])
		if int(row['thalach']) < 100:
			thalach = 0
		elif int(row['thalach']) < 150:
			thalach = 1
		elif int(row['thalach']) < 200:
			thalach = 2
		else:
			thalach = 3
		exang = int(row['exang'])
		if float(row['oldpeak']) < 1:
			oldpeak = 0
		elif float(row['oldpeak']) < 2:
			oldpeak = 1
		elif float(row['oldpeak']) < 3:
			oldpeak = 2
		elif float(row['oldpeak']) < 4:
			oldpeak = 3
		elif float(row['oldpeak']) < 5:
			oldpeak = 4
		elif float(row['oldpeak']) < 6:
			oldpeak = 5
		elif float(row['oldpeak']) >= 6:
			oldpeak = 6
		slope = int(row['slope'])
		ca = int(row['ca'])
		thal = int(row['thal'])
		target = int(row['target'])
        #writing the changed values in the new file
		writer.writerow({'age' : age,'sex' : sex,'cp': cp,'trestbps' : trestbps,'chol':chol,'fbs':fbs,'restecg':restecg,'thalach':thalach,'exang':exang,'oldpeak':oldpeak,'slope':slope,'ca':ca,'thal':thal,'target':target})


