from flask import Flask, render_template
from form import CoverForm, AgreementForm, ChecklistForm, PersonalInformationForm, ShortEssayForm, AutobiographicalForm, ScaleOMatic
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
    form = {"cover":cover,
            "agreement":agreement,
            "checklist":checklist,
            "personal":personal,
            "short":short,
            "auto":auto,
            "range": range}
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run()