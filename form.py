from flask_wtf import FlaskForm
from wtforms import StringField,\
                    BooleanField,\
                    IntegerField, SelectField,\
                    DateField, TextAreaField, IntegerRangeField, Form, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email


class CoverForm(FlaskForm):
    full_name = StringField(label='Full Name', validators=[DataRequired()],
                            render_kw={'autocomplete': "off"})
    today_date = DateField(label="Today's Date", format='%m/%d/%y',
                           render_kw={'autocomplete': "off"},
                           validators=[DataRequired()])


class AgreementForm(Form):
    initials = StringField(validators=[DataRequired()],
                           render_kw={'autocomplete': "off", "maxlength":"4", "style":"width: 50px;"})


class ChecklistForm(FlaskForm):
    check = BooleanField()


class PersonalInformationForm(Form):
    full_legal_name = StringField(label="Full Legal Name",
                                  validators=[DataRequired()],
                                  render_kw={"style":"width: 400px;"})
    preferred_name = StringField(label="Preferred Name")
    pronouns = StringField(label="Select your preferred pronoun or add it. ",
                           validators=[DataRequired()])
    dob = DateField(label="Date of Birth",
                    format='%m/%d/%y',
                    validators=[DataRequired()],
                    render_kw={'autocomplete': "off"})
    email = StringField(label="Email",
                        validators=[DataRequired()],
                        render_kw={"placeholder": "example@mail.com",
                                   "type": "email"})
    phone = IntegerField(label='Phone',
                         validators=[DataRequired()])
    permanent_address = StringField(label="Address",
                                    validators=[DataRequired()],
                                    render_kw={"style": "width: 500px;"})
    current_address = StringField(label="Current Address",
                                  validators=[DataRequired()],
                                  render_kw={"style": "width: 500px;"})

    my_choices = [('1', 'Fall'), ('2', 'Spring'), ('3', 'Summer'), ('4', "Winter")]
    term_move_in = SelectMultipleField(label="Check the term you wish to move in. "
                                             "If you’re flexible, mark multiple terms "
                                             "(Use command to select multiple). "
                                             "If you intend to move in during the middle of a term, please let us know",
                                       choices=my_choices)

    year = IntegerField(label="Year", validators=[DataRequired()], render_kw={ "min": "2022", "value": "2022"})

    was_boarder = BooleanField("Have you ever been a resident or boarder of the SCA?",
                               render_kw={'onclick':"showStuff('was_boarder_checked')"})
    years_boarder = IntegerField(label="Year", render_kw={"min": "1920", "max": "2022"})
    denied_membership = BooleanField("Have you ever been denied membership with the SCA? (Answering 'yes’ to this question does"\
                                     "not necessarily disqualify you from membership.)")

    member_terminated = BooleanField(label="Have you ever had your membership or tenancy terminated "
                                           "by the SCA and/or another housing organization (Answering "
                                           "‘yes’ to this question does not necessarily disqualify you "
                                           "from membership.)",
                                     render_kw={"onclick": "showStuff('was_boarder_terminated')"})

    member_terminated_explanation = StringField(label="If yes, explain")

    type_student = SelectField(label="Type of Student",
                               choices=["Non Student", "Undergrad", "Graduate", "Post-Baccalaureate"],
                               render_kw={"onchange": "hide_if_selected(this.value, 'is_student', 'Non Student')"})
    school_year = IntegerField(label="School Year")
    credits = IntegerField(label="Credits")
    major = StringField(label="Major")

    house_preference = SelectField(choices=["None", "JS", "Lorax", "Campbell Club"])
    room_preference = SelectField(choices=["None", "Single", "Small Single", "Double"])

    house_no_available = BooleanField("If your choice of room or household is not available, would you be willing to be assigned to "
                                      "another house and/or room?")
    if_not_available = BooleanField("If you have a strong preference for one house or will only consider living in one or two of the"
                                    "houses, please let us know:")
    waitlist = BooleanField("Are you willing to be placed on a waiting list for an open housing spot?")
    allergies = StringField("Allergies?")
    how_long = StringField(label="How long do you expect to live in these houses? If you don’t know /"
                                 "that’s okay.", validators=[DataRequired()])
    #Ajax
    pet = BooleanField("Do you have a pet you’d like to bring?")
    pet_description = StringField(label="Pet Description: ")
    pet_needs = StringField(label="What are your pet’s needs (outdoor/indoor/other) and how they tend to interact with other" +
                                  "animals?: ")
    hear_about_us = SelectMultipleField(label="How did you hear about us?", choices=["Radio", "Fb", "Craiglist", "Friend", "Other"],
                                    render_kw={"onclick": "show_if_selected(this.value, 'other_hear', 'Other')"})
    if_other_about_us = StringField(label="If other, please, specify.")


class ShortEssayForm(FlaskForm):
    question = TextAreaField(render_kw={"rows":"12", "cols":"150"})


class AutobiographicalForm(Form):
    question = TextAreaField(render_kw={"rows": "12", "cols": "150"})


class Range(Form):
    range = IntegerRangeField(label= "range", render_kw={"min": 0,
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
