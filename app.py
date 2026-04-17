from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from DevOps 🚀</h1>
    <p>Welcome to DevOps world</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
