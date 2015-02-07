from flask import render_template, session, redirect, request, url_for, flash
from flask.ext.security import login_required
from flask.ext.security.core import current_user

from . import market
from .. import db

@market.route('/', methods=['GET'])
def index():
    from fisbang.models.project import Project
    projects = Project.query.limit(3).all()
    return render_template('market/index.html', project_list=projects)

@market.route('/create', methods=['GET','POST'])
@login_required
def project_create():
    from fisbang.market.forms import CreateProjectForm
    form = CreateProjectForm()
    form.project_category.choices = [(type.id, type.name) for type in get_category()]
    form.project_budget.choices = [(type.id, type.name) for type in get_budget()]
    print "category", form.project_category.data
    if form.validate_on_submit():
        from fisbang.models.project import Project, ProjectCategory, ProjectBudget
        print form.project_category.data
        project_category = ProjectCategory.query.get(form.project_category.data)
        print form.project_budget.data
        project_budget = ProjectBudget.query.get(form.project_budget.data)
        project = Project(user_id=current_user.id,
                          project_category_id = project_category.id,
                          name=form.name.data,
                          skills=form.skills.data,
                          description=form.description.data,
                          project_budget_id=project_budget.id)
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('market.index'))

    return render_template('market/create.html', form=form)

def get_category():
    from fisbang.models.project import ProjectCategory
    project_categories = ProjectCategory.query.all()
    return project_categories

def get_budget():
    from fisbang.models.project import ProjectBudget
    project_budgets = ProjectBudget.query.all()
    return project_budgets
