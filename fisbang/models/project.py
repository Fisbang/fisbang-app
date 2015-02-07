from fisbang import db

class ProjectCategory(db.Model):
    __tablename__ = 'project_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    projects = db.relationship('Project', backref='project_category', lazy='dynamic')

class ProjectBudget(db.Model):
    __tablename__ = 'project_budget'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    projects = db.relationship('Project', backref='project_budget', lazy='dynamic')

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_category_id = db.Column(db.Integer, db.ForeignKey('project_category.id'))
    name = db.Column(db.String(80))
    skills = db.Column(db.String(80))
    description = db.Column(db.String(80))
    project_budget_id = db.Column(db.Integer, db.ForeignKey('project_budget.id'))

    def view(self):
        project = {}
        project["id"] = self.id
        project["user_id"] = self.id
        project["category"] = self.project_category.name
        project["name"] = self.location
        project["skills"] = self.merk
        project["description"] = self.type
        project["budget"] = self.project_budget.name

        return project
