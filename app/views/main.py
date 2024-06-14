from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import FileRecord
from werkzeug.utils import secure_filename
import os

main_bp = Blueprint('main', __name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'sdf', 'csv', 'pdb', 'pdbqt', 'mol2'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main_bp.route('/pyai_vs', methods=['GET', 'POST'])
@login_required
def pyai_vs():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传', function='pyai_vs')
            db.session.add(new_file)
            db.session.commit()
            flash('文件上传成功')
            # TODO: 发送文件给远程机器进行处理
            return redirect(url_for('main.pyai_vs'))
    return render_template('pyai_vs.html')

@main_bp.route('/psearch', methods=['GET', 'POST'])
@login_required
def psearch():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传', function='psearch')
            db.session.add(new_file)
            db.session.commit()
            flash('文件上传成功')
            # TODO: 发送文件给远程机器进行处理
            return redirect(url_for('main.psearch'))
    return render_template('psearch.html')

@main_bp.route('/docking_vs', methods=['GET', 'POST'])
@login_required
def docking_vs():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传', function='docking_vs')
            db.session.add(new_file)
            db.session.commit()
            flash('文件上传成功')
            # TODO: 发送文件给远程机器进行处理
            return redirect(url_for('main.docking_vs'))
    return render_template('docking_vs.html')

@main_bp.route('/l_score', methods=['GET', 'POST'])
@login_required
def l_score():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传', function='l_score')
            db.session.add(new_file)
            db.session.commit()
            flash('文件上传成功')
            # TODO: 发送文件给远程机器进行处理
            return redirect(url_for('main.l_score'))
    return render_template('l_score.html')

@main_bp.route('/user_profile')
@login_required
def user_profile():
    files = FileRecord.query.filter_by(user_id=current_user.id).all()
    return render_template('user_profile.html', files=files)
