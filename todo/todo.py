from flask import (
    Blueprint,flash,g,redirect,render_template,request,url_for
) 

from werkzeug.exceptions import abort
from todo.auth import login_requiered
from todo.db import get_db

bp = Blueprint('todo', __name__ )

@bp.route('/')
def index():
    db, c = get_db()
    c.execute(
        'select t.id,t.descripcion,u.username, t.completed, t.created_at from todo t join user u on t.created_by = u.id order by created_at desc '
    )
    todos = c.fetchall()

    return render_template('todo/index.html', todos=todos)

@bp.route('/create')
def create():
    None

@bp.route('/update')
def update():
    None   