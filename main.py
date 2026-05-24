from flask import Flask, render_template, request, redirect, send_file
from extractors.ber import extract_ber_jobs
from extractors.web3 import extract_web3_jobs
from file import save_to_file

app = Flask("Jobscapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html", name="KingSoo")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    print(keyword)
    if keyword in db:
        jobs = db[keyword]
    else:
        berlinstartupjobs = extract_ber_jobs(keyword)
        web3 = extract_web3_jobs(keyword)
        jobs = berlinstartupjobs + web3
        db[keyword] = jobs
    return render_template("Search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run("0.0.0.0")
