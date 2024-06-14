from flask import Blueprint, render_template
from flask_login import login_required, current_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile')
@login_required
def profile():
    return render_template('user.html', user=current_user)

@user_bp.route('/user_management')
@login_required
def user_management():
    # 从数据库获取用户文件信息
    files = [
        {"filename": "example_file.txt", "status": "Processed"}
    ]
    return render_template('user_profile.html', files=files)
