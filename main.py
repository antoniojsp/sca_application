from flask import Flask, render_template, request, jsonify
from form import CoverForm, AgreementForm, \
                 ChecklistForm, PersonalInformationForm, \
                 ShortEssayForm, AutobiographicalForm, \
                 References, Range
from database import *
import os

app = Flask(__name__)

app.secret_key = os.environ['SECRET_WORD']
db = Database()

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


@app.route('/_submit')
def _submit():
    package = request.args.get("data")
    import json
    out = json.loads(package)
    print(out)
    # db.insert(out)
    return jsonify(result={"response": "200"})


if __name__ == "__main__":
    app.run()