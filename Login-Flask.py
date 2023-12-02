from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/', methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")


    return render_template('Login Page.html')
if __name__ == "__main__":
    app.run(use_reloader=True,host="127.0.0.1", port=5000)