from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, validators
from wtforms.validators import InputRequired, URL, Optional, ValidationError

species_choice = ['cat', 'dog', 'llama', 'duck', 'water buffalo', 'pig']


def validate_age(form, field):
    """Custom age validator to ensure age is between 0 and 30"""
    if field.data < 0 or field.data > 30:
        raise ValidationError("Age must be between 0 and 30")

class PetForm(FlaskForm): 
    """Form class for creating a Pet"""
        
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[(pet,pet) for pet in species_choice], validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[URL(),Optional()])
    age = IntegerField("Age", validators=[validate_age])
    notes = StringField("Notes")
    available = BooleanField("Available")

    # For some reason i attempted to make a custom form validator for updating Pet instead of just making a new form so if you want to see my attempt at that here it is (the only field that i really needed validated (photo_URL) doesnt even correctly validate): 


    # def validate(self, extra_validators=None):
    #     pet = getattr(self, 'pet', None)
    #     print(pet)
    #     if pet and self.name.data == pet.name and self.species.data == pet.species and self.age.data == pet.age:
    #         print('VALIDATED NAME SPECIES AND AGE')
    #         if self.photo_url:
    #             print("SELF.PHOTO_URL EXISTS")
    #             url_validator = URL()
    #             if not url_validator(self, self.photo_url):
    #                 print("URL NOT VALID")
    #                 raise ValidationError(['Invalid Photo URL'])
    #                 return False
    #         print("RETURNING TRUE")
    #         return True
    #     print("NAME SPECIES AND AGE DID NOT MATCH OR SOMETHING LIKE THAT")
    #     if not super().validate():
    #         return False

    #     return True

class EditPetForm(FlaskForm):
    """Form class for editing a Pet"""
    photo_url = StringField("Photo URL", validators=[URL(),Optional()])
    notes = StringField("Notes")
    available = BooleanField("Available")