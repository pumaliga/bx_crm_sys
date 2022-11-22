from flask import render_template
from flask_login import login_required, current_user

from app.profile import profile


@profile.route('/main')
@login_required
def main_profile():
    return render_template('profile/main_profile.html', email=current_user.email)
