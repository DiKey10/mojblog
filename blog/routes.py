# blog/routes.py


from flask import render_template, request, session, flash, redirect, url_for
from blog import app
from blog.models import Entry, LoginForm, db

@app.route("/")
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", all_posts=all_posts)


@app.route("/login/", methods=['GET', 'POST'])
def login():
   form = LoginForm()
   errors = None
   next_url = request.args.get('next')
   if request.method == 'POST':
       if form.validate_on_submit():
           session['logged_in'] = True
           session.permanent = True  # Use cookie to store session.
           flash('You are now logged in.', 'success')
           return redirect(next_url or url_for('index'))
       else:
           errors = form.errors
   return render_template("login_form.html", form=form, errors=errors)


def one_function(request):
    if entry_id == None:
        form = EntryForm()
        errors = None
        if request.method == 'POST':
            if form.validate_on_submit():
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data
                is_published = form.is_published.data
                )
                db.session.add(entry)
                db.session.commit()
            else:
                errors = form.errors
    else:
    return render_template("entry_form.html", form=form, errors=errors)

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    return one_function(request=request,entry_id=entry_id)

@app.route("/new-post/", methods=["GET", "POST"])
def create_entry():
    return one_function(request=request,entry_id=None)




@app.route('/logout/', methods=['GET', 'POST'])
def logout():
   if request.method == 'POST':
       session.clear()
       flash('You are now logged out.', 'success')
   return redirect(url_for('index'))



@app.route("/drafts/", methods=['GET'])
@login_required
def list_drafts():
   drafts = Entry.query.filter_by(is_published=False).order_by(Entry.pub_date.desc())
   return render_template("drafts.html", drafts=drafts)


#do dopracowania
def delete_entry(entry_id):
   entry = Entry.query.filter_by(id=entry_id).first_or_404()
   form = EntryForm(obj=entry)
   errors = None
   if request.method == 'POST':
       if form.validate_on_submit():
           form.populate_obj(entry)
           db.session.commit()
       else:
           errors = form.errors
   return render_template("entry_form.html", form=form, errors=errors)