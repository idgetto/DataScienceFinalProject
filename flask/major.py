from flask import Flask
from flask import request
import pickle
import pandas as pd

app = Flask(__name__)
course_codes = pickle.load(open("../data/coursecodes.p", 'rb'))
fr_alg_d = pickle.load( open( "../data/fr_major.p", "rb" ) )
so_alg_d = pickle.load( open( "../data/so_major.p", "rb" ) )
jr_alg_d = pickle.load( open( "../data/jr_major.p", "rb" ) )
sr_alg_d = pickle.load( open( "../data/sr_major.p", "rb" ) )

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/freshman", methods=['POST'])
def freshman():
	data = request.get_json()
	courses_taken = set(data['courses']) & set(course_codes)
	df = pd.DataFrame(columns = course_codes)
	df.loc[0] = False
	df.loc[0, course_taken] = True
	fr_prediction = {}
	for key in fr_alg_d:
		fr_prediction[key] = fr_alg_d[key].predict_proba(df)[:,1]
	return fr_prediction

@app.route("/sophomore", methods=['POST'])
def sophomore():
	data = request.get_json()
	courses_taken = set(data['courses']) & set(course_codes)
	df = pd.DataFrame(columns = course_codes)
	df.loc[0] = False
	df.loc[0, course_taken] = True
	so_prediction = {}
	for key in fr_alg_d:
		so_prediction[key] = so_alg_d[key].predict_proba(df)[:,1]
	return so_prediction

@app.route("/junior", methods=['POST'])
def junior():
	data = request.get_json()
	courses_taken = set(data['courses']) & set(course_codes)
	df = pd.DataFrame(columns = course_codes)
	df.loc[0] = False
	df.loc[0, course_taken] = True
	jr_prediction = {}
	for key in fr_alg_d:
		jr_prediction[key] = jr_alg_d[key].predict_proba(df)[:,1]
	return jr_prediction

@app.route("/senior", methods=['POST'])
def senior():
	data = request.get_json()
	courses_taken = set(data['courses']) & set(course_codes)
	df = pd.DataFrame(columns = course_codes)
	df.loc[0] = False
	df.loc[0, course_taken] = True
	sr_prediction = {}
	for key in fr_alg_d:
		sr_prediction[key] = sr_alg_d[key].predict_proba(df)[:,1]
	return sr_prediction

if __name__ == "__main__":
    app.run()