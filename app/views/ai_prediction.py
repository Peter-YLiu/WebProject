from flask import Blueprint, render_template
from flask_login import login_required

ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ai_prediction')
@login_required
def ai_prediction():
    return render_template('ai_prediction.html')
