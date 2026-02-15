import os
from flask import Flask, render_template, request
from src.nlp.nl_to_sql import question_to_sql
from src.gcp.bigquery_client import run_query
from src.gcp.vertex_ai import explain_results

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None

    if request.method == "POST":
        question = request.form["question"]
        sql = question_to_sql(question)
        df = run_query(sql)
        answer = explain_results(question, df)

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))