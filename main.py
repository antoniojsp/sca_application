from flask import Flask, render_template, request, jsonify
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


@app.route('/_submit')
def _submit():
    package = request.args.get("data")
    import json
    out = json.loads(package)
    print(out[0])
    return jsonify(result={"response": "hola"})


if __name__ == "__main__":
    app.run()