import json
import pytest

@pytest.fixture
def get_player_data():
	with open('players.json') as file:
		data = json.load(file)

	return data

def test_file1_method1(get_player_data):
	country = "India"

	assert check_foreign_players(get_player_data,country) == 4

def test_file2_method(get_player_data):
	role= "Wicket-keeper"

	assert check_wicket_keeper(get_player_data,role) == True

def check_foreign_players(data,country):
	count = 0
	for i in data['players']:
		if i['country'] != country:
			count += 1
	return count

def check_wicket_keeper(data,role):
	for i in data['players']:
		if i['role'] == role:
			return True
