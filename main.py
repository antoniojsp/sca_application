from flask import Flask, render_template
from form import CoverForm, AgreementForm, \
                 ChecklistForm, PersonalInformationForm, \
                 ShortEssayForm, AutobiographicalForm, \
                 ScaleOMatic, References, Range
app = Flask(__name__)

app.secret_key = "maria"


@app.route('/')
def index():
    cover = CoverForm()
    agreement = AgreementForm()
    checklist = ChecklistForm()
    personal = PersonalInformationForm()
    short= ShortEssayForm()
    auto = AutobiographicalForm()
    range = ScaleOMatic()
    reference = References()

    form = {"cover":cover,
            "agreement": agreement,
            "checklist": checklist,
            "personal": personal,
            "short": short,
            "auto": auto,
            "range": range,
            "reference": reference}

    lala = Range()
    lala.range.label = "hoho"
    return render_template("index.html", form=form, range=lala)


if __name__ == "__main__":
    app.run()