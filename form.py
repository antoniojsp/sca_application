from flask_wtf import FlaskForm
from wtforms import StringField,\
                    BooleanField,\
                    IntegerField, SelectField,\
                    DateField, TextAreaField, IntegerRangeField, Form, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email


onclick_clear = "clear_highlight(this)"

class CoverForm(FlaskForm):
    full_name = StringField(validators=[DataRequired()],
                            render_kw={'class': "cover", 'autocomplete': "off", "style": "width: 400px;", "onclick": "clear_highlight(this)"})
    today_date = DateField(format='%m/%d/%y',
                           render_kw={'autocomplete': "off", 'class': "cover", "onclick": onclick_clear},
                           validators=[DataRequired()])


class AgreementForm(Form):
    initials = StringField(validators=[DataRequired()],
                           render_kw={'autocomplete': "off",
                                      "maxlength": "4",
                                      "style": "width: 60px;",
                                      "placeholder": "initials",
                                      'class': 'agreement', "onclick": onclick_clear})


class ChecklistForm(Form):
    check = BooleanField(render_kw={'class': 'checklist', "onclick": onclick_clear})


class PersonalInformationForm(Form):

    style_short = "width: 150px;"
    style_medium = "width: 400px;"
    style_long = "width: 500px;"
    style_check = "width:15px;"

    full_legal_name = StringField(validators=[DataRequired()],
                                  render_kw={"style": style_medium, "onclick": onclick_clear})
    preferred_name = StringField(render_kw={"style": style_medium, "onclick": onclick_clear})
    pronouns = StringField(render_kw={"style": style_short, "onclick": onclick_clear})

    dob = DateField(format='%m/%d/%y',
                    validators=[DataRequired()],
                    render_kw={'autocomplete': "off",
                               "style": style_short,
                               "onchange": onclick_clear + ",if_not_underage(this, '#is_underage')",
                               })
    email = StringField(render_kw={"placeholder": "example@mail.com",
                                   "type": "email",
                                   "style": style_long,
                                   "onclick": onclick_clear,
                                   "onkeyup": "if_email_valid(this, '#valid_email')"
                              },
                        validators=[DataRequired()])

    phone = IntegerField(validators=[DataRequired()], render_kw={"style": style_medium, "onclick": onclick_clear})

    #TODO
    #Make easy to copy permanent address to current address if the user choose that.
    permanent_address = StringField(validators=[DataRequired()],
                                    render_kw={"style": style_long, "onclick": onclick_clear})
    current_address = StringField(validators=[DataRequired()],
                                  render_kw={"style": style_long, "onclick": onclick_clear})

    my_choices = [('1', 'Fall'), ('2', 'Spring'), ('3', 'Summer'), ('4', "Winter")]
    move_in_term = SelectMultipleField(choices=my_choices,
                                       validators=[DataRequired()],
                                       render_kw={"style": style_short, "onclick": onclick_clear})

    move_in_year=IntegerField(validators=[DataRequired()], render_kw={"style": style_short, "onclick": onclick_clear})

    # SHOW AND HIDE
    was_boarder = BooleanField(render_kw={"style": style_check,
                                          'onclick': "show_hide_extra_inputs('was_boarder_checked',['was_boarder_years'])",})
    was_boarder_years = IntegerField(render_kw={"min": "1920", "max": "2022", "style": style_short, "onclick": onclick_clear})

    denied_membership = BooleanField(render_kw={"style": style_check})

    # SHOW AND HIDE
    member_terminated = BooleanField(render_kw={"onclick": "show_hide_extra_inputs('was_boarder_terminated', "
                                                           "['member_terminated_explanation'])",
                                                "style": style_check})
    member_terminated_explanation = TextAreaField(render_kw={"rows": "12", "cols": "150", "onclick": onclick_clear})

    # type of student
    type_student = SelectField(choices=["Non Student", "Undergrad", "Graduate", "Post-Baccalaureate"],
                               render_kw={"onchange": "hide_if_selected(this.value,"
                                                      "'is_student', 'Non Student', "
                                                      "['which_school', 'school_year', 'credits', 'major'])",
                                          "style": style_short},
                               validators=[DataRequired()])
    which_school = StringField(render_kw={"style": style_medium, "onclick": onclick_clear})
    school_year = IntegerField(render_kw={"style": style_short, "onclick": onclick_clear})
    credits = IntegerField(render_kw={"style": style_short, "onclick": onclick_clear})
    major = StringField(render_kw={"style": "width: 200px;", "onclick": onclick_clear})

    house_preference = SelectField(choices=["None", "JS", "Lorax", "Campbell Club"],
                                   render_kw={"style": style_short})
    room_preference = SelectField(choices=["None", "Single", "Small Single", "Double"],
                                  render_kw={"style": style_short})

    house_no_available = BooleanField(render_kw={"style": style_check})
    if_not_available = BooleanField(render_kw={"style": style_check})
    waitlist = BooleanField(render_kw={"style": style_check})
    allergies = StringField(render_kw={"style": style_medium})
    how_long = StringField(render_kw={"style": style_medium, "onclick": onclick_clear},
                           validators=[DataRequired()])

    # SHOW AND HIDE
    pet = BooleanField(render_kw={'onclick': "show_hide_extra_inputs('has_pet', ['pet_description', 'pet_needs'])",
                                  "style": style_check})
    pet_description = StringField(render_kw={"style": style_long, "onclick": onclick_clear})
    pet_needs = StringField(render_kw={"style": style_long, "onclick": onclick_clear})
    hear_about_us = SelectMultipleField(choices=["Radio", "Fb", "Craiglist", "Friend", "Other"],
                                        render_kw={"onclick": "show_if_selected(this.value, 'other_hear', 'Other', ['if_other_about_us']), clear_highlight(this)",
                                         "style": style_medium})

    if_other_about_us = StringField(render_kw={"style": style_long, "onclick": onclick_clear})


class ShortEssayForm(Form):
    question = TextAreaField(render_kw={"class": "essay", "rows": "12", "cols": "150", "onclick": onclick_clear},
                             validators=[DataRequired()])


class AutobiographicalForm(Form):
    question = TextAreaField(render_kw={"class": "auto", "rows": "12", "cols": "150", "onclick": onclick_clear},
                             validators=[DataRequired()])


class Range(Form):
    range = IntegerRangeField(label="range", render_kw={"min": 0,
                                                        "max": 10,
                                                        "step": 1,
                                                        "style": "width:500px;"})
    input = IntegerField(render_kw={"class": "range", "type": "number",
                                    "value": "5",
                                    "min": "0",
                                    "max": "10"})
    comment = StringField("Comments:", render_kw={"class": "range",
                                                  "placeholder": "Comments"})


class References(Form):
    name = StringField(label="Name",
                       render_kw={"class": "reference", "onclick": onclick_clear},
                       validators=[DataRequired()])
    relationship = StringField(label="Relationship",
                               render_kw={"class": "reference", "onclick": onclick_clear},
                               validators=[DataRequired()])
    email = StringField(label="Email",
                        render_kw={"class": "reference", "onclick": onclick_clear},
                        validators=[DataRequired()])
    phone = StringField(label='Phone',
                        render_kw={"class": "reference", "onclick": onclick_clear},
                        validators=[DataRequired()])


