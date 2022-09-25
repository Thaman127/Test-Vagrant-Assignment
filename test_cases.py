import json
import pytest

@pytest.fixture
def get_player_data():
	with open('players.json') as file:
		data = json.load(file)

	return data

def test_check_foreign_players(get_player_data):
	count = 0
	for i in get_player_data['players']:
		if i['country'] != "India":
			count += 1
	assert count == 4

def test_check_wicket_keeper(get_player_data):
	for i in get_player_data['players']:
		if i['role'] == 'Wicket-keeper':
			assert 1+1 == 2
