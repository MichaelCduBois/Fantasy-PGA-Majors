from flask import redirect, render_template, url_for
import pymongo
from uuid import uuid4


def create():
    """
    Creates a new league.
    Keyword arguments:
    None
    """
    # Creates league an assigns an ID
    league_id = str(uuid4()).replace("-", "")
    admin_key = str(uuid4())[:8]

    # Creates blank JSON
    league_json = {
        "_id": league_id,
        "admin_key": admin_key,
        "entries": [],
        "groups": []
    }

    # Pymongo Connection
    client = pymongo.MongoClient("mongodb://database:27017")

    db = client['scores']
    collection = db['leagues']

    collection.insert(league_json)

    client.close()

    return redirect(
        url_for(
            ".league_index",
            league_id=league_id,
            admin_key=admin_key
        )
    )


def get_info(selected_league):
    """
    Send a chat message to the server.
    Keyword arguments:
    selected_league -- Generates scoreboard for desired league
    """
    return render_template('scoreboard.html', league=selected_league)
