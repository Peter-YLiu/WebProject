from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import FileRecord
from werkzeug.utils import secure_filename
import os
import pandas as pd

main_bp = Blueprint('main', __name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'sdf', 'csv', 'pdb', 'pdbqt', 'mol2'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@main_bp.route('/showcase')
@login_required
def showcase():
    return render_template('showcase.html')


@main_bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


def handle_file_upload(request, function_name):
    if 'file' not in request.files:
        flash('No file part')
        return None
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return None
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        new_file = FileRecord(filename=filename, user_id=current_user.id, status='已上传', function=function_name)
        db.session.add(new_file)
        db.session.commit()
        # 使用 Pinggy 域名生成下载URL
        public_url = 'http://rnlkp-101-44-83-196.a.free.pinggy.link'  # 替换为你的 Pinggy 域名
        download_url = f'{public_url}/uploads/{filename}'
        flash(f'文件上传成功，下载链接：{download_url}')
        return download_url
    return None


@main_bp.route('/pyai_vs', methods=['GET', 'POST'])
@login_required
def pyai_vs():
    if request.method == 'POST':
        if 'target_button' in request.form:
            target = request.form.get('target')
            if target == 'A3AR':
                return redirect(url_for('main.show_csv', function='pyai_vs'))
            flash(f'选定的靶点是：{target}')
            return redirect(url_for('main.pyai_vs'))
        else:
            handle_file_upload(request, 'pyai_vs')
            return redirect(url_for('main.pyai_vs'))
    return render_template('pyai_vs.html')


@main_bp.route('/psearch', methods=['GET', 'POST'])
@login_required
def psearch():
    if request.method == 'POST':
        if 'target_button' in request.form:
            target = request.form.get('target')
            if target == 'A3AR':
                return redirect(url_for('main.show_csv', function='psearch'))
            flash(f'选定的靶点是：{target}')
            return redirect(url_for('main.psearch'))
        else:
            handle_file_upload(request, 'psearch')
            return redirect(url_for('main.psearch'))
    return render_template('psearch.html')


@main_bp.route('/docking_vs', methods=['GET', 'POST'])
@login_required
def docking_vs():
    if request.method == 'POST':
        if 'target_button' in request.form:
            target = request.form.get('target')
            if target == 'A3AR':
                return redirect(url_for('main.show_csv', function='docking_vs'))
            flash(f'选定的靶点是：{target}')
            return redirect(url_for('main.docking_vs'))
        else:
            handle_file_upload(request, 'docking_vs')
            return redirect(url_for('main.docking_vs'))
    return render_template('docking_vs.html')


@main_bp.route('/l_score', methods=['GET', 'POST'])
@login_required
def l_score():
    if request.method == 'POST':
        if 'target_button' in request.form:
            target = request.form.get('target')
            if target == 'A3AR':
                return redirect(url_for('main.show_csv', function='l_score'))
            flash(f'选定的靶点是：{target}')
            return redirect(url_for('main.l_score'))
        else:
            handle_file_upload(request, 'l_score')
            return redirect(url_for('main.l_score'))
    return render_template('l_score.html')

@main_bp.route('/user_profile')
@login_required
def user_profile():
    files = FileRecord.query.filter_by(user_id=current_user.id).all()
    return render_template('user_profile.html', files=files)

# 新添加的文件列表路由
@main_bp.route('/file_list')
def file_list():
    files = FileRecord.query.all()
    file_list = [{"filename": file.filename} for file in files]
    return jsonify(file_list)

@main_bp.route('/show_csv/<function>')
@login_required
def show_csv(function):
    csv_file_map = {
        'psearch': 'pharm_screen.csv',
        'docking_vs': 'docking_screen.csv',
        'l_score': 'redock_screen.csv',
        'pyai_vs': 'pyaivs_screen.csv'
    }
    csv_file_name = csv_file_map.get(function)
    if not csv_file_name:
        flash('Invalid function')
        return redirect(url_for('main.dashboard'))

    csv_file_path = os.path.join('app', 'uploads', csv_file_name)
    try:
        df = pd.read_csv(csv_file_path, sep=',', encoding='utf-8')
    except Exception as e:
        flash(f'Error reading CSV file: {e}')
        return redirect(url_for('main.dashboard'))

    data = df.to_dict(orient='records')
    return render_template('show_csv.html', data=data)

@main_bp.route('/database_preview')
@login_required
def database_preview():
    # 读取数据库文件
    file_path = os.path.join('app', 'uploads', '虚拟筛选数据库.xlsx')
    df = pd.read_excel(file_path)
    data = df.to_dict(orient='records')
    return render_template('database_preview.html', data=data)

