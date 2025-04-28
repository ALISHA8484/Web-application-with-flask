from flask import Blueprint, render_template , request, flash , jsonify,redirect,url_for
from flask_login import login_required, current_user
from .models import Note , User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    token = request.cookies.get('token')

    user = User.query.filter_by(token=token).first()
    if not user:
        flash('Session expired or invalid token.', category='error')
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html",user=current_user)

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/admin')
def admin_panel():
    token = request.cookies.get('token')
    user = User.query.filter_by(token=token).first()

    if not user or not user.is_admin:
        flash('Access denied.', category='error')
        return redirect(url_for('views.home'))
    
    users = User.query.all()
    return render_template('admin.html', users=users, user=user)