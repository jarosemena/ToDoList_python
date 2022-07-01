from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)

import functools
from werkzeug.exceptions import abort
from todo.auth import login_requiered
from todo.db import get_db

bp = Blueprint('todo', __name__ )

@bp.route('/')
@login_requiered
def index():
    db, c = get_db()
    c.execute(
        'select t.id,t.descripcion,u.username, t.completed, t.created_at from todo t '
        'join user u on t.created_by = u.id '
        ' where t.created_by = %s order by created_at desc ',
        (g.user['id'],)
    )
    todos = c.fetchall()

    return render_template('todo/index.html', todos=todos)

@bp.route('/create', methods=['GET','POST'])
@login_requiered
def create():

    if request.method == 'POST':
        description = request.form['description']
        error = None

        if not description :
            error = 'Descripcion es requerida'
        else:
            db, c = get_db()
            c.execute(
                'insert into todo (descripcion, completed, created_by) '
                ' values (%s,%s,%s)',
                (description, False, g.user['id'])
            )
            db.commit()
            return redirect(url_for('todo.index'))
            
    return  render_template('todo/create.html')

def get_task(id):
    db, c = get_db()
    c.execute(
        'select t.id, t.descripcion, t.completed, t.created_by ,t.created_at, u.username '
        ' from todo t join user u on t.created_by = u.id where t.id = %s',
        (id,)
    )
    task = c.fetchone()

    if task is None:
        abort(404," La tarea con id {0} no existe".format(id))

    return task


@bp.route('/<int:id>/update', methods=['GET','POST'])
@login_requiered
def update(id):
    
    task = get_task(id)
    if request.method == 'POST':
        description = request.form['description']
        completed = True if request.form.get('completed')== 'on' else False
        error = None

        if not description :
            error = 'Descripcion es requerida'
        
        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute(
                'update todo set descripcion = %s, completed=%s '
                ' where id = %s and created_by = %s',
                (description, completed, id,g.user['id'],)
            )
            db.commit()
            return redirect(url_for('todo.index'))

    return  render_template('todo/update.html', task=task)   


@bp.route('/<int:id>/delete', methods=['POST'])
@login_requiered
def delete(id):
   
    error = None

    if not id :
        error = 'No selecciono un ID'
    else:
        db, c = get_db()
        c.execute(
            'delete from todo where id = %s and created_by = %s',
            (id,g.user['id'],)
        )
        db.commit()
        return redirect(url_for('todo.index'))
         