from flask import Flask, request, render_template, redirect, flash, session
import flask
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'chickenzarecool21837'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']  = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_list_pets():
    """Home page that lists all Pets in adoption database"""
    pets = Pet.query.all()
    return render_template('list_pets.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """GET request shows pet creation form, POST request validates form data and creates new Pet"""
    form = PetForm()

    if form.validate_on_submit():
        pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data, age=form.age.data, notes= form.notes.data)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_new_pet.html', form=form)
    
@app.route('/<int:id>', methods=["GET", "POST"])
def show_pet_details(id):
    """GET request shows Pet deails and edit form, POST request validates and edits Pet of id"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('details_edit.html', pet=pet, form=form)