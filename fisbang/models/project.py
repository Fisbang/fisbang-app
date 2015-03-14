from fisbang import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    description = db.Column(db.String(80))
    budget = db.Column(db.String(80))

    def view(self):
        project = {}
        project["id"] = self.id
        project["name"] = self.name
        project["email"] = self.email
        project["description"] = self.description
        project["budget"] = self.budget

        return project
