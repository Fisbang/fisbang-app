from flask import render_template, session, redirect, request, url_for, flash
from flask.ext.security import login_required, RegisterForm
from flask.ext.security.core import current_user
from flask.ext.security.registerable import register_user
from flask.ext.security.utils import login_user

from fisbang.market import market
from fisbang.services import mailing
from fisbang import db

@market.route('/', methods=['GET'])
def index():
    return render_template('market/index.html')

@market.route('/create_project', methods=['GET','POST'])
def project_create():
    from fisbang.market.forms import CreateProjectForm
    form = CreateProjectForm()
    if form.validate_on_submit():
        from fisbang.models.project import Project

        project = Project(name=form.name.data,
                          email=form.email.data,
                          description=form.description.data,
                          budget=form.budget.data)
        db.session.add(project)
        db.session.commit()
        #mailing.send_created_project(project.id)
        return redirect(url_for('market.index'))

    if current_user.is_authenticated():
        form.name.data = current_user.name
        form.email.data = current_user.email

    return render_template('market/get-project.html', form=form)

def get_category():
    from fisbang.models.project import ProjectCategory
    project_categories = ProjectCategory.query.all()
    return project_categories

def get_budget():
    from fisbang.models.project import ProjectBudget
    project_budgets = ProjectBudget.query.all()
    return project_budgets

@market.route('/projects', methods=['GET'])
def projects_list():
    from fisbang.models.project import Project
    projects = Project.query.all()
    return render_template('market/projects_list.html', projects=projects)

@market.route('/projects/<project_id>', methods=['GET'])
def project_details(project_id):
    from fisbang.models.project import Project
    project = Project.query.get(project_id)
    return render_template('market/project_details.html', project=project)
