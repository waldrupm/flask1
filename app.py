from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
  return "Hello to the world of Flask!"

if __name__ == '__main__':
  app.run()