import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("builder.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    print(f"✅ AvaNews Builder is running at http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
