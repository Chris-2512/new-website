from flask import Flask, render_template, jsonify, request 
app = Flask(__name__)

JOBS=[
    {
      'id' : 1,
      'title': 'Twitter by X'
    },
  {
    'id' : 2,
    'title': 'Instagram'
  },
  {
    'id' : 3,
    'title': 'Facebook'
  },
  {
    'id' : 4,
    'title': 'Redit / Discord'
  },
]
@app.route("/")
def hello_world():
  return render_template('home.html', 
        jobs=JOBS,
                        my_name='Chris') 
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
class LocalData:
    def __init__(self, username, text):
        self.username = username
        self.text = text

@app.route("/jobpage")
def new_page():
  return render_template('jobpage.html', 
        jobs=JOBS,
                        my_name='Chris') 





@app.route("/jobs/apply" , methods=['post'])
def apply_to_jobs(id):
  data = request.form
  return render_template('application_submitted.html',data=data)
  
if __name__ == "__main__":
  app.run(host ='0.0.0.0', debug=True)