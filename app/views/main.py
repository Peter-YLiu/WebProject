from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import FileRecord
from app.forms import UploadForm
import os
from werkzeug.utils import secure_filename

main_bp = Blueprint('main', __name__)

UPLOAD_FOLDER = 'path/to/upload/folder'

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
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传', function='PyaiVS')
        db.session.add(new_file)
        db.session.commit()
        flash('文件上传成功')
        # TODO: 启动文件处理脚本
        return redirect(url_for('main.pyai_vs'))
    return render_template('pyai_vs.html', form=form)

@main_bp.route('/psearch', methods=['GET', 'POST'])
@login_required
def psearch():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传', function='Psearch')
        db.session.add(new_file)
        db.session.commit()
        flash('文件上传成功')
        # TODO: 启动文件处理脚本
        return redirect(url_for('main.psearch'))
    return render_template('psearch.html', form=form)

@main_bp.route('/docking_vs', methods=['GET', 'POST'])
@login_required
def docking_vs():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传', function='DockingVS')
        db.session.add(new_file)
        db.session.commit()
        flash('文件上传成功')
        # TODO: 启动文件处理脚本
        return redirect(url_for('main.docking_vs'))
    return render_template('docking_vs.html', form=form)

@main_bp.route('/l_score', methods=['GET', 'POST'])
@login_required
def l_score():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传', function='L-Score')
        db.session.add(new_file)
        db.session.commit()
        flash('文件上传成功')
        # TODO: 启动文件处理脚本
        return redirect(url_for('main.l_score'))
    return render_template('l_score.html', form=form)

@main_bp.route('/user_profile')
@login_required
def user_profile():
    files = FileRecord.query.filter_by(user_id=current_user.id).all()
    return render_template('user_profile.html', files=files)

