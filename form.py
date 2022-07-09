from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email
# from wtforms.fields import DateTimeLocalField



class Application(FlaskForm):
    full_name = StringField(label='Full Name', validators=[DataRequired()],
                      render_kw={"class": "form-control p-2s",
                                 'autocomplete': "off"})
    today_date = DateTimeField(label="Today's Date", format='%m/%d/%y', validators=[DataRequired()],render_kw={"class": "form-control p-2s",
                                 'autocomplete': "off"})

    initials1 = StringField(label="Initials", validators=[DataRequired()],render_kw={"class": "form-control p-2s",
                                 'autocomplete': "off"})
    initials2 = StringField(label="Initials", validators=[DataRequired()],render_kw={"class": "form-control p-2s",
                                 'autocomplete': "off"})
    initials3 = StringField(label="Initials", validators=[DataRequired()])
    initials4 = StringField(label="Initials", validators=[DataRequired()])
    initials5 = StringField(label="Initials", validators=[DataRequired()])
    initials6 = StringField(label="Initials", validators=[DataRequired()])

    check1 = BooleanField(label="check")
    check2 = BooleanField(label="check")
    check3 = BooleanField(label="check")
    check4 = BooleanField(label="check")
    check5 = BooleanField(label="check")
    check6 = BooleanField(label="check")


    full_legal_name = StringField(label="Full Legal Name", validators=[DataRequired()])
    preferred_name = StringField(label="Prefered Name")
    pronouns = StringField(label="Pronouns", validators=[DataRequired()])
    dob =  DateTimeField(label="Date of Birth", validators=[DataRequired()])
    email = StringField(label="Email",  validators=[DataRequired(), Email()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    permanent_address =StringField(label="Address", validators=[DataRequired()])
    current_address = StringField(label="Current Address", validators=[DataRequired()])


    term_move_in = SelectField(label="What term you plan to move in?", choices=["Fall", "Winter", "Spring", "Summer"])
    year = IntegerField(label="Year", validators=[DataRequired()])

    #Ajax
    was_boarder = BooleanField("Have you ever been a resident or boarder of the SCA?")
    years_boarder = IntegerField(label="Year")

    denied_membership = BooleanField("Have you ever been denied membership with the SCA? (Answering 'yes’ to this question does /"
                                     "not necessarily disqualify you from membership.)")

    #Ajax
    member_terminated = BooleanField(label="Have you ever had your membership or tenancy terminated by the SCA and/or another /" \
                        "housing organization (Answering ‘yes’ to this question does not necessarily disqualify " \
                        "you from membership.)")
    member_terminated_explanation = StringField(label="If yes, explain")

    #AJax
    type_student = SelectField(label="Type of Student", choices=["Non Student", "Undergrad", "Graduate", "Post-Baccalaureate"])
    school_year = IntegerField(label="School Year")
    credits = IntegerField(label="Credits")
    major = StringField(label="Major")

    house_preference = SelectField(label="Type of Student", choices=["JS", "Lorax", "Campbell Club"])
    if_not_available = BooleanField("If you have a strong preference for one house or will only consider living in one or two of the/"
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

    heer_about_us = SelectField(label="How did you hear about us?", choices=["Radio", "Fb", "Craiglist", "Friend"])


    submit = SubmitField(label="Shorten",
                     render_kw={"class": "btn btn-success"})
