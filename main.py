from flask import Flask, request, render_template

app = Flask(__name__)


tarefas = [
    {

        "id": 1,
        "titulo": "Estudar JavaScript",
        "descricao": "Estudar JavaScript para para aprender a construir eventos",
        "status": "Em andamento",
        "prioridade": "Alta",
        "data_criacao": "17-08-2025",
        "responsavel": "Adalberto"

    },
    {
        "id": 2,
        "titulo": "Estudar Flask",
        "descricao": "Estudar Flask para para aprender sobre Web Services",
        "status": "Não iniciado",
        "prioridade": "Média",
        "data_criacao": "12-03-2026",
        "responsavel": "Maria Clara"
    }
]


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def ge_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return tarefa


@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1
    task['id'] = ultimo_id
    tarefas.append(task)
    return task

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None

    #Buscando a tarefa que será alterada
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    #Alterando a tarefa na lista
    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['prioridade'] = task_body.get('prioridade', task_search['prioridade'])
    task_search['data_criacao'] = task_body.get('data_criacao', task_search['data_criacao'])
    task_search['responsavel'] = task_body.get('responsavel', task_search['responsavel'])

    return task_search

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            tarefas.remove(tarefa)
            return ({'mensagem': 'Tarefa removida com sucesso'})
        return ({'erro': 'Tarefa não encontrada'}), 404


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)


