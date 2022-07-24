from flask_wtf import FlaskForm
from wtforms import StringField,\
                    BooleanField,\
                    IntegerField, SelectField,\
                    DateField, TextAreaField, IntegerRangeField, Form, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email


class CoverForm(FlaskForm):
    full_name = StringField(validators=[DataRequired()],
                            render_kw={'class':"cover", 'autocomplete': "off", "style":"width: 400px;"})
    today_date = DateField(format='%m/%d/%y',
                           render_kw={'autocomplete': "off", 'class': "cover"},
                           validators=[DataRequired()])


class AgreementForm(Form):
    initials = StringField(validators=[DataRequired()],
                           render_kw={'autocomplete': "off",
                                      "maxlength": "4",
                                      "style": "width: 60px;",
                                      "placeholder": "initials",
                                      'class': 'agreement'})


class ChecklistForm(Form):
    check = BooleanField(render_kw={'class':'agreement'}, validators=[DataRequired()])


class PersonalInformationForm(Form):
    full_legal_name = StringField(validators=[DataRequired()],
                                  render_kw={"style":"width: 400px;"})
    preferred_name = StringField()
    pronouns = StringField()
    dob = DateField(format='%m/%d/%y',
                    validators=[DataRequired()],
                    render_kw={'autocomplete': "off"})
    email = StringField(validators=[DataRequired(), Email("This field requires a valid email address")],
                        render_kw={"placeholder": "example@mail.com",
                                   "type": "email"})
    phone = IntegerField(validators=[DataRequired()])
    permanent_address = StringField(validators=[DataRequired()],
                                    render_kw={"style": "width: 500px;"})
    current_address = StringField(validators=[DataRequired()],
                                  render_kw={"style": "width: 500px;"})


    my_choices = [('1', 'Fall'), ('2', 'Spring'), ('3', 'Summer'), ('4', "Winter")]
    move_in_term = SelectMultipleField(choices=my_choices,
                                       validators=[DataRequired()])

    move_in_year= IntegerField(validators= [DataRequired()])

    # JS Magic
    was_boarder = BooleanField(render_kw={'onclick': "showStuff('was_boarder_checked')"})
    years_boarder = IntegerField(render_kw={"min": "1920", "max": "2022"})

    denied_membership = BooleanField()

    member_terminated = BooleanField(render_kw={"onclick": "showStuff('was_boarder_terminated')"})
    member_terminated_explanation = TextAreaField(render_kw={"rows": "12", "cols": "150"})

    type_student = SelectField(choices=["Non Student", "Undergrad", "Graduate", "Post-Baccalaureate"], render_kw={"onchange": "hide_if_selected(this.value, 'is_student', 'Non Student')"})
    which_school = StringField(render_kw={"style":"width: 400px;"})
    school_year = IntegerField()
    credits = IntegerField()
    major = StringField()

    house_preference = SelectField(choices=["None", "JS", "Lorax", "Campbell Club"])
    room_preference = SelectField(choices=["None", "Single", "Small Single", "Double"])

    house_no_available = BooleanField()
    if_not_available = BooleanField()
    waitlist = BooleanField()
    allergies = StringField()
    how_long = StringField(validators=[DataRequired()])
    #JS Magic
    pet = BooleanField(render_kw={'onclick': "showStuff('has_pet')"})
    pet_description = StringField()
    pet_needs = StringField()
    hear_about_us = SelectMultipleField(choices=["Radio", "Fb", "Craiglist", "Friend", "Other"],
                                        render_kw={"onclick": "show_if_selected(this.value, 'other_hear', 'Other')"})
    if_other_about_us = StringField()


class ShortEssayForm(Form):
    question = TextAreaField(render_kw={"rows": "12", "cols": "150"})


class AutobiographicalForm(Form):
    question = TextAreaField(render_kw={"rows": "12", "cols": "150"})


class Range(Form):
    range = IntegerRangeField(label="range", render_kw={"min": 0,
                                                        "max": 10,
                                                        "step": 1,
                                                        "style": "width:500px;"})
    input = IntegerField(render_kw={"type": "number",
                                    "value": "5",
                                    "min": "0",
                                    "max": "10"})
    comment = StringField("Comments:", render_kw={"placeholder": "Comments"})


class References(Form):
    name = StringField(label="Name")
    relationship = StringField(label="Relationship")
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])


    # submit = SubmitField(label="Shorten",
    #                  render_kw={"class": "btn btn-success"})
