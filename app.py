from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS=[
    {
      'id' : 1,
      'title': 'blockchain',
      'Location': 'UK',
      'salary': '1000$'
    },
  {
    'id' : 2,
    'title': 'banking',
    'Location': 'Switzerland',
    'salary': '5000$'
  },
  {
    'id' : 3,
    'title': 'real estate',
    'Location': 'Arizona',
    'salary': '100000$'
  },
  {
    'id' : 4,
    'title': 'Backend engineer',
    'Location': 'Ottawa',
    'salary': '10000$'
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

  
  
if __name__ == "__main__":
  app.run(host ='0.0.0.0', debug=True)