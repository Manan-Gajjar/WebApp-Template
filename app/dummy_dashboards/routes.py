from flask import render_template
from app.dummy_dashboards import blueprint


@blueprint.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html')


@blueprint.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')


@blueprint.route('/dashboard3')
def dashboard3():
    return render_template('dashboard3.html')

