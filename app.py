from flask import Flask, render_template

app = Flask(__name__)

RequestType = [
{
  'id' : 1,
  'title' : 'Emergency'
},
{
  'id' : 2,
  'title' : 'During Working Days'
},
{
  'id' : 3,
  'title' : 'For festival, function,etc'
},
{
  'id' : 4,
  'title' : 'Health issues'
}


]

@app.route("/")
def hello_world():
  return render_template('home.html' ,request= RequestType)

@app.route("/api/request")
def list_request():
  return jsonify(RequestType)
print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)