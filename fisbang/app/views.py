from flask import render_template, redirect

from fisbang.services import mailing
from fisbang.app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    from fisbang.app.forms import GetUpdateForm
    form = GetUpdateForm()
    if form.validate_on_submit():
        mailing.send_get_update(form.email.data)
        return redirect(url_for('app.index'))

    return render_template('app/index.html', form=form)
