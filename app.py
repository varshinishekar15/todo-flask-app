from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [task.strip() for task in f.readlines()]
    except:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    tasks = load_tasks()
    if task:
        tasks.append(task)
        save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    tasks = load_tasks()
    if 0 <= id < len(tasks):
        tasks.pop(id)
        save_tasks(tasks)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
