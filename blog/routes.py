# blog/routes.py

from flask import render_template
from blog import app

@app.route("/")
def index():
   return render_template("base.html")



"""

from flask import render_template, request
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm

@app.route("/new-post/", methods=["GET", "POST"])
def create_entry():
   form = EntryForm()
   errors = None
   if request.method == 'POST':
       if form.validate_on_submit():
           entry = Entry(
               title=form.title.data,
               body=form.body.data
               is_published=form.is_published.data
           )
           db.session.add(entry)
           db.session.commit()
       else:
           errors = form.errors
   return render_template("entry_form.html", form=form, errors=errors)
   """