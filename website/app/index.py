from app import leagues
from flask import (
    Blueprint, json, jsonify, redirect, render_template,
    request, url_for
)
from jinja2 import exceptions
import pymongo

# Creates Blueprint
bp = Blueprint('index', __name__)


# Index Setup
@bp.route('/')
def index():
    """
    Site Index.
    Keyword arguments:
    None
    """
    return "Page Index"


# Gets Current Golfer Skills
@bp.route('/scores')
def scores():
    """
    Displays scores from the live PGA tournament.
    Keyword arguments:
    None
    """
    # Pymongo Connection
    client = pymongo.MongoClient("mongodb://database:27017")

    db = client['scores']
    collection = db['actual']

    current_scores = collection.find()

    client.close()

    try:

        return render_template('scores.html', data=current_scores[0])

    except IndexError:

        return "Please wait for scores to update."


# League Setup
@bp.route(
    '/league/',
    defaults={"league_id": None, "admin_key": None},
    methods=('GET', 'POST')
)
@bp.route(
    '/league/<string:league_id>/',
    defaults={"admin_key": None},
    methods=('GET', 'POST')
)
@bp.route(
    '/league/<string:league_id>/<string:admin_key>',
    methods=('GET', 'POST')
)
def league_index(league_id, admin_key):
    """
    Displays specific league page.
    Keyword arguments:
    league_id -- ID for a specific league
    admin_key -- Key allowing admin access to league
    """
    # Pymongo Connection
    client = pymongo.MongoClient("mongodb://database:27017")

    db = client['scores']
    league_collection, scores_collection = db['leagues'], db['actual']

    selected_league = league_collection.find_one({"_id": league_id})

    current_scores = scores_collection.find()

    client.close()

    if selected_league is not None:

        if admin_key is not None:

            if selected_league["admin_key"] == admin_key:

                if request.method == 'POST':

                    client = pymongo.MongoClient("mongodb://database:27017")

                    db = client['scores']

                    league_collection = db['leagues']

                    selected_league = league_collection.find_one(
                        {"_id": league_id}
                    )

                    # Adds all items from a selection into array
                    new_groups = {"$set": {"groups": [
                        {"group1": request.form.getlist('group1')},
                        {"group2": request.form.getlist('group2')},
                        {"group3": request.form.getlist('group3')},
                        {"group4": request.form.getlist('group4')},
                        {"group5": request.form.getlist('group5')},
                        {"group6": request.form.getlist('group6')}
                    ]}}

                    league_collection.update_one(selected_league, new_groups)

                    client.close()

                try:

                    return render_template(
                        'admin.html',
                        data=current_scores[0],
                        league_id=league_id,
                        admin_key=admin_key,
                        groups=["1", "2", "3", "4", "5", "6"]
                    )

                except IndexError:

                    return "Please wait for scores to update."

        return leagues.get_info(selected_league)

    return "Please Enter Valid League ID."


# League Creation
@bp.route('/league/new')
def create_league():
    """
    Endpoint that creates a new league
    Keyword arguments:
    None
    """
    return leagues.create()
