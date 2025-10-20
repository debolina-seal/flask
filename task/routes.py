# Flask modules
from flask import Blueprint, redirect, url_for, render_template
from flask_login import current_user, login_required

# Local modules
from app.models import Task
from app.extensions import db, bcrypt
from task.forms import CreatTaskForm

routes_task = Blueprint('tasks', __name__, url_prefix="/task")

@routes_task.route("/add_task", methods=['GET', 'POST'])
@login_required
def add_task():
    form = CreatTaskForm()
   
    if form.validate_on_submit():
        name = form.name.data
        status = form.status.data
        new_task = Task(name=name, status=status, user=int(current_user.get_id()))
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("routes.dashboard"))


    return render_template('task.html',form=form)

@routes_task.route("/change_task/<id>", methods=['GET', 'POST'])
@login_required
def change_task(id):
    task = db.session.query(Task).get(id)
    form = CreatTaskForm(obj=task)
    if form.validate_on_submit():
        task.name = form.name.data
        task.status = form.status.data
        db.session.commit()
        return redirect(url_for("routes.dashboard"))


    return render_template('task.html',form=form, changePage = True)