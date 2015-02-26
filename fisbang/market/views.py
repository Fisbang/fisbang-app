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
    from fisbang.models.project import Project
    projects = Project.query.order_by(Project.id.desc()).limit(3).all()
    return render_template('market/index.html', project_list=projects)

@market.route('/create_project', methods=['GET','POST'])
def project_create():
    from fisbang.market.forms import CreateProjectForm, CreateProjectWithRegister
    if current_user.is_authenticated():
        form = CreateProjectForm()
    else:
        form = CreateProjectWithRegister()
    form.project_category.choices = [(type.id, type.name) for type in get_category()]
    form.project_budget.choices = [(type.id, type.name) for type in get_budget()]
    print "category", form.project_category.data

    if form.validate_on_submit():
        if not current_user.is_authenticated():
            user = register_user(**form.to_dict())
            login_user(user)
        else:
            user = current_user
        from fisbang.models.project import Project, ProjectCategory, ProjectBudget
        print form.project_category.data
        project_category = ProjectCategory.query.get(form.project_category.data)
        print form.project_budget.data
        project_budget = ProjectBudget.query.get(form.project_budget.data)

        project = Project(user_id=user.id,
                          project_category_id = project_category.id,
                          name=form.name.data,
                          skills=form.skills.data,
                          description=form.description.data,
                          project_budget_id=project_budget.id)
        db.session.add(project)
        db.session.commit()
        mailing.send_created_project(project.id)
        return redirect(url_for('market.project_details', project_id=project.id))

    return render_template('market/create.html', form=form)

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
