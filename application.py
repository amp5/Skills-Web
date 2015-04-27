# Will need to get virtualenv working on computer. 
# Cannot do so at the moment. En route to Yosemite. No wireless....

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def start_page():
	return render_template("index.html")


@app.route('/application-form')
def application():
	return render_template("application-form.html")

@app.route('/application')
def submitted():
	firstname = request.args.get("firstname")
	lastname = request.args.get("lastname")
	salary = request.args.get("salary")
	job = request.args.get("job")

	return render_template("submitted.html", firstname=firstname, lastname=lastname, salary=salary, job=job)







# *****************************

if __name__ == "__main__" :
	app.run(debug = True)