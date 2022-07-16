from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, SubmitField, \
                    BooleanField, DateTimeField, \
                    IntegerField, SelectField, \
                    DateField, TextAreaField, IntegerRangeField, Form, FormField
from wtforms.validators import DataRequired, Length, Email
# from wtforms.fields import DateTimeLocalField

class CoverForm(Form):
    full_name = StringField(label='Full Name', validators=[DataRequired()],
                      render_kw={'autocomplete': "off"})
    today_date = DateField(label="Today's Date", format='%m/%d/%y', validators=[DataRequired()],render_kw={'autocomplete': "off"})

class AgreementForm(Form):
    initials1 = StringField(label="Initials", validators=[DataRequired()],render_kw={
                                 'autocomplete': "off"})
    initials2 = StringField(label="Initials", validators=[DataRequired()],render_kw={
                                 'autocomplete': "off"})
    initials3 = StringField(label="Initials", validators=[DataRequired()])
    initials4 = StringField(label="Initials", validators=[DataRequired()])
    initials5 = StringField(label="Initials", validators=[DataRequired()])
    initials6 = StringField(label="Initials", validators=[DataRequired()])

class ChecklistForm(FlaskForm):
    check1 = BooleanField(label="check")
    check2 = BooleanField(label="check")
    check3 = BooleanField(label="check")
    check4 = BooleanField(label="check")
    check5 = BooleanField(label="check")
    check6 = BooleanField(label="check")


class PersonalInformationForm(Form):
    full_legal_name = StringField(label="Full Legal Name", validators=[DataRequired()])
    preferred_name = StringField(label="Preferred Name")
    pronouns = StringField(label="Pronouns", validators=[DataRequired()])
    dob =  DateTimeField(label="Date of Birth", validators=[DataRequired()])
    email = StringField(label="Email",  validators=[DataRequired(), Email()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    permanent_address =StringField(label="Address", validators=[DataRequired()])
    current_address = StringField(label="Current Address", validators=[DataRequired()])
    term_move_in = SelectField(label="Check the term you wish to move in. If you’re flexible, mark multiple terms. If you intend to "\
                                     "move in during the middle of a term, please let us know<", choices=["Fall", "Winter", "Spring", "Summer"])
    year = IntegerField(label="Year", validators=[DataRequired()])
    #Ajax
    was_boarder = BooleanField("Have you ever been a resident or boarder of the SCA?")
    years_boarder = IntegerField(label="Year")
    denied_membership = BooleanField("Have you ever been denied membership with the SCA? (Answering 'yes’ to this question does"\
                                     "not necessarily disqualify you from membership.)")
    #Ajax
    member_terminated = BooleanField(label="Have you ever had your membership or tenancy terminated by the SCA and/or another" \
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


class ShortEssayForm(FlaskForm):

    question1 = TextAreaField(label="Why do you want to become a member-owner of a housing cooperative? What do you"
                                    " know about housing cooperative organizations (ours or others), and what about this model"
                                    " appeals to you?", render_kw={"rows":"12", "cols":"150"})

    question2 = TextAreaField(label="Tell us what you know about our community in particular, even if it’s not much. What is your"
                                    " general impression of the SCA (or SCA house you’re applying to), and why does it appeal "
                                    "to you? What values, morals, interests, hobbies, etc. do you think you might share with "
                                    "other members?", render_kw={"rows":"12", "cols":"150"})

    question3 = TextAreaField(label="Other than the basics of cooperative living (doing jobs, getting along with & working well "
                                    "with others, etc.), what unique and/or useful skills or knowledge do you bring to a group? "
                                    "Provide an example of how you have applied one or more of these skills in a past living, "
                                    "work, school, or cooperative group situation. How do you plan on applying some of these "
                                    "here?", render_kw={"rows":"12", "cols":"150"})

    question4 = TextAreaField(label=". Living and helping in a cooperative is a unique experience and cooperative living requires "
                                    "cooperative solutions. Describe at least one experience you’ve had with a difficult or "
                                    "stressful living, work, or organizing situation that involves a group of people. What was the "
                                    "situation, why did it come about, and how did you collaborate with others to deal with it? "
                                    "What was the outcome, and what did you learn from the experience? ", render_kw={"rows":"12", "cols":"150"})

    question5 = TextAreaField(label="Part 1: Our community consists of members from various backgrounds, differing in gender,"
                                    " orientation, age, income level, immigration status, and ethnicities. We aim to challenge"
                                    " oppression of all kinds and foster a culture of support and solidarity, as well as respectful"
                                    " interactions. Generally, how do you go about addressing or intervening when you witness"
                                    " someone being oppressive or discriminatory towards others? Part 2: In addition, many"
                                    " people have intersecting identities that may lead to them being both oppressed and the"
                                    " oppressor in different contexts. (IE: A White, queer person benefits from White Supremacy"
                                    " but is oppressed by homophobia and transphobia). Where do you see your own identities"
                                    " existing along these intersections? How do you challenge your own indoctrination into "
                                    "oppressive systems?", render_kw={"rows":"12", "cols":"150"})

    question6 = TextAreaField(label="Living with so many different types of people can be challenging, and we can occasionally"
                                    " clash with, hurt, or offend those around us without intending to. Describe a situation where"
                                    " you took responsibility for a mistake you made. (Think of a time you realized you were in"
                                    " the wrong.) What was your mistake and what led you to make it? What led you to recognize "
                                    "your responsibility in the matter, and what did you do to take accountability for your"
                                    " actions? What was the outcome, and what did you learn?", render_kw={"rows":"12", "cols":"150"})

    question7 = TextAreaField(label="Please describe any volunteer work, organizing, activism, or meaningful experiences in"
                                    " which you have participated in dismantling oppressive systems, especially Racism and "
                                    "White Supremacy. What issues matter to you? Do you see yourself continuing this work "
                                    "while living in the SCA?", render_kw={"rows":"12", "cols":"150"})

    question8 = TextAreaField(label="Please tell us how you wish to exist within a cooperative community. Feel free to ramble"
                                    "and be creative! For example; how do you relate or enjoy hanging out with your peers, or"
                                    "people you share a space with? What are your values, goals, frustrations, and aspirations"
                                    "for a community you would potentially live in? How would you plan to help create an"
                                    "intentional community, with the help of other members?", render_kw={"rows":"12", "cols":"150"})


class AutobiographicalForm(FlaskForm):
    question1 = TextAreaField(label="Please craft an autobiographical statement. Tell us about yourself in all your glory. Be creative! "
                                    "There are no right or wrong answers. Applicants may submit brief essays, poems, short stories, "
                                    " or drawings. "
                                    "If you are submitting a non-written autobiographical statement or if your statement does not fit "
                                    "below, please email it as a .doc, .Jpeg or .pdf file.", render_kw={"rows": "12", "cols": "150"})
    # print(question1)


class Range(Form):
    range = IntegerRangeField(label= "range", render_kw={"min": 0,
                                                         "max": 10,
                                                         "step": 1,
                                                         "style": "width:600px;",
                                                         })

    input = IntegerField(render_kw={"type": "number",
                                     "value": "5",
                                     "min": "0",
                                     "max": "10",
                                    })
    comment = StringField("Comments:", render_kw={"placeholder": "Comments"})




class ScaleOMatic(FlaskForm):

        range = FormField(Range)

        range1 = IntegerRangeField(label="range",render_kw={'id':"range1",
                                                "min": 0,
                                                "max": 10,
                                                "step": 1,
                                                "style": "width:600px;",
                                                "oninput": f"amount1.value=range1.value" })

        input1 = IntegerField(render_kw={"id": f"amount1",
                                         "type": "number",
                                         "value": "5",
                                         "min": "0",
                                         "max": "10",
                                         "oninput": f'range1.value=amount1.value'})
        comment1 = StringField("Comments:",render_kw={"placeholder":"Comments"})

        range2 = IntegerRangeField(label="range",render_kw={'id':"range2",
                                                "min": 0,
                                                "max": 10,
                                                "step": 1,
                                                "style": "width:600px;",
                                                "oninput": f"amount2.value=range2.value" })

        input2 = IntegerField(render_kw={"id": f"amount2",
                                         "type": "number",
                                         "value": "5",
                                         "min": "0",
                                         "max": "10",
                                         "oninput": f'range2.value=amount2.value'})
        comment2 = StringField("Comments:",render_kw={"placeholder":"Comments"})



        range3 = IntegerRangeField(label="range",render_kw={'id':"range3",
                                                "min": 0,
                                                "max": 10,
                                                "step": 1,
                                                "style": "width:600px;",
                                                "oninput": f"amount3.value=range3.value" })

        input3 = IntegerField(render_kw={"id": f"amount3",
                                         "type": "number",
                                         "value": "5",
                                         "min": "0",
                                         "max": "10",
                                         "oninput": f'range3.value=amount3.value'})
        comment3 = StringField("Comments:",render_kw={"placeholder":"Comments"})



        range4 = IntegerRangeField(label="range",render_kw={'id':"range4",
                                                "min": 0,
                                                "max": 10,
                                                "step": 1,
                                                "style": "width:600px;",
                                                "oninput": f"amount4.value=range4.value" })

        input4 = IntegerField(render_kw={"id": f"amount4",
                                         "type": "number",
                                         "value": "5",
                                         "min": "0",
                                         "max": "10",
                                         "oninput": f'range4.value=amount4.value'})
        comment4 = StringField("Comments:",render_kw={"placeholder":"Comments"})



        range5 = IntegerRangeField(label="range",render_kw={'id':"range5",
                                                "min": 0,
                                                "max": 10,
                                                "step": 1,
                                                "style": "width:600px;",
                                                "oninput": f"amount5.value=range5.value" })

        input5 = IntegerField(render_kw={"id": f"amount5",
                                         "type": "number",
                                         "value": "5",
                                         "min": "0",
                                         "max": "10",
                                         "oninput": f'range5.value=amount5.value'})
        comment5 = StringField("Comments:",render_kw={"placeholder":"Comments"})

        range6 = IntegerRangeField(label="range",render_kw={'id':"range6",
                                                "min": 0,
                                                "max": 10,
                                                "step": 1,
                                                "style": "width:600px;",
                                                "oninput": f"amount6.value=range6.value" })

        input6 = IntegerField(render_kw={"id": f"amount6",
                                         "type": "number",
                                         "value": "5",
                                         "min": "0",
                                         "max": "10",
                                         "oninput": f'range6.value=amount6.value'})
        comment6 = StringField("Comments:",render_kw={"placeholder":"Comments"})

        range7 = IntegerRangeField(label="range",render_kw={'id':"range7",
                                                "min": 0,
                                                "max": 10,
                                                "step": 1,
                                                "style": "width:600px;",
                                                "oninput": f"amount7.value=range7.value" })

        input7 = IntegerField(render_kw={"id": f"amount7",
                                         "type": "number",
                                         "value": "5",
                                         "min": "0",
                                         "max": "10",
                                         "oninput": f'range7.value=amount7.value'})
        comment7 = StringField("Comments:",render_kw={"placeholder":"Comments"})

        range8 = IntegerRangeField(label="range",render_kw={'id':"range8",
                                                "min": 0,
                                                "max": 10,
                                                "step": 1,
                                                "style": "width:600px;",
                                                "oninput": f"amount8.value=range8.value" })

        input8 = IntegerField(render_kw={"id": f"amount8",
                                         "type": "number",
                                         "value": "5",
                                         "min": "0",
                                         "max": "10",
                                         "oninput": f'range8.value=amount8.value'})
        comment8 = StringField("Comments:",render_kw={"placeholder":"Comments"})






class Contact(Form):
    name = StringField(label="Name")
    relationship = StringField(label="Relationship")
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])

class References(Form):

    contacts1 = FormField(Contact)
    contacts2 = FormField(Contact)
    contacts3 = FormField(Contact)


    # submit = SubmitField(label="Shorten",
    #                  render_kw={"class": "btn btn-success"})
