from servidor import app

@app.route("/", methods="GET")
def listarExamenes():
    return [{}]