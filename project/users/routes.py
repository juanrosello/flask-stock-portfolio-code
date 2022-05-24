from . import users_blueprint
from flask import render_template, flash, abort


# --------------
# Error Handlers
# --------------

@users_blueprint.errorhandler(403)
def page_forbidden(e):
    return render_template('users/403.html'), 403


# ------
# Routes
# ------

@users_blueprint.route('/about')
def about():
    flash('Thanks for learning about this site!', 'info')
    return render_template('users/about.html', company_name='Juan Rosello')


@users_blueprint.route('/admin')
def admin():
    abort(403)