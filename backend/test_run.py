import run
import json


def test_home():
    with open("test_responses/home.json") as f:
        expected = json.load(f)
    with run.app.app_context():
        real = run.home().json
    assert expected == real
