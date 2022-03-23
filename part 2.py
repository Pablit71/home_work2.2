from utils import get_candidate
from utils import load_candidates_from_json
from utils import get_candidates_by_skill
from utils import get_candidates_by_name
from utils import list_skill_name
from utils import num_user_skill
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def all_candidates():
    candidates = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<x>')
def individual_candidate(x):
    name = get_candidates_by_name(x)
    number_id = get_candidate(x)
    skills = get_candidates_by_skill(x)
    return render_template('single.html', name=name, number_id=number_id, skills=skills)


@app.route("/skill/<skill_name>")
def skill(skill_name):
    candidates = list_skill_name(skill_name)
    numbers = num_user_skill(skill_name)
    return render_template('skill.html', candidates=candidates, numbers=numbers)


app.run(debug=True)
