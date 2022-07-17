from flask import Flask, render_template
from form import CoverForm, AgreementForm, \
                 ChecklistForm, PersonalInformationForm, \
                 ShortEssayForm, AutobiographicalForm, \
                 References, Range
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
    scale = Range()
    reference = References()

    form = {"cover":cover,
            "agreement": agreement,
            "checklist": checklist,
            "personal": personal,
            "short": short,
            "auto": auto,
            "range": scale,
            "reference": reference}

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run()