from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import FileRecord
from app.forms import UploadForm
import os
from werkzeug.utils import secure_filename

main_bp = Blueprint('main', __name__)  # 确保这里没有设置静态文件夹路径

UPLOAD_FOLDER = 'path/to/upload/folder'

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main_bp.route('/function1', methods=['GET', 'POST'])
@login_required
def function1():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传')
        db.session.add(new_file)
        db.session.commit()
        flash('文件上传成功')
        # TODO: 启动文件处理脚本
        return redirect(url_for('main.function1'))
    return render_template('function1.html', form=form)

@main_bp.route('/function2', methods=['GET', 'POST'])
@login_required
def function2():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传')
        db.session.add(new_file)
        db.session.commit()
        flash('文件上传成功')
        # TODO: 启动文件处理脚本
        return redirect(url_for('main.function2'))
    return render_template('function2.html', form=form)

@main_bp.route('/function3', methods=['GET', 'POST'])
@login_required
def function3():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传')
        db.session.add(new_file)
        db.session.commit()
        flash('文件上传成功')
        # TODO: 启动文件处理脚本
        return redirect(url_for('main.function3'))
    return render_template('function3.html', form=form)

@main_bp.route('/function4', methods=['GET', 'POST'])
@login_required
def function4():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传')
        db.session.add(new_file)
        db.session.commit()
        flash('文件上传成功')
        # TODO: 启动文件处理脚本
        return redirect(url_for('main.function4'))
    return render_template('function4.html', form=form)
