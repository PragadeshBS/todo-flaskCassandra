from flask import Flask, render_template, url_for, request, redirect
import uuid
from flask_cqlalchemy import CQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = 'test'
db = CQLAlchemy(app)


class Todo(db.Model):
    id = db.columns.UUID(primary_key=True, default=uuid.uuid4)
    content = db.columns.Text(required=True)
    date_created = db.columns.DateTime(required=True, default=datetime.now)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            task_content = request.form['content']
            new_task = Todo.create(content=task_content)
            # db.session.add(new_task)
            # db.session.commit()
            return redirect('/')
        except Exception as e:
            print(e)
            return 'There was an issue adding your task'
    tasks = Todo.objects().all()
    return render_template('index.html', tasks=tasks)


@app.route('/delete/<string:id>')
def delete(id):
    task_to_delete = Todo.objects(id=id).first()
    task_to_delete.delete()
    return redirect('/')


@app.route('/update/<string:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.objects(id=id).first()
    if request.method == 'POST':
        task.content = request.form['content']
        task.save()
        return redirect('/')
    return render_template('update.html', task=task)


if __name__ == '__main__':
    app.run(debug=True)