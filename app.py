from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)


tasks = []
task_id_control = 1


@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }

    return jsonify(output)


@app.route("/tasks/<int:task_id>")
def get_task(task_id):
    for t in tasks:
        if t.get_id() == task_id:
            return jsonify(t.to_dict())

    return jsonify({"message": "Task not found"}), 404


@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control,
                    title=data.get("title"),
                    description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)

    return jsonify({
        "message": "Tarefa criada com sucesso",
        "id": new_task.get_id()
    })


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = None

    for t in tasks:
        if t.get_id() == task_id:
            task = t

    if task is None:
        return jsonify({"message": "Tarefa nao encontrada"}), 404

    data = request.get_json()
    task.set_title(data.get("title"))
    task.set_description(data.get("description"))
    task.set_completed(data.get("completed"))

    return jsonify({"message": "Tarefa atualizada com sucesso"})


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = None

    for t in tasks:
        if t.get_id() == task_id:
            task = t
            break

    if not task:
        return jsonify({"message": "Tarefa nao encontrada"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa removida com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)
