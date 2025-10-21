import pytest
import requests
from src import api
from unittest.mock import Mock

def test_get_random_character(mocker):
    """Tests the get_random_character function with mocked API calls."""
    # Mock for the first API call to get the character count
    mock_info_response = Mock()
    mock_info_response.json.return_value = {"info": {"count": 826}}
    mock_info_response.raise_for_status.return_value = None

    # Mock for the second API call to get the actual character
    mock_char_response = Mock()
    mock_char_response.json.return_value = {
        "id": 1, "name": "Rick Sanchez", "status": "Alive",
        "species": "Human", "origin": {"name": "Earth (C-137)"}
    }
    mock_char_response.raise_for_status.return_value = None

    # Use side_effect to provide a different mock for each call
    mocker.patch("requests.get", side_effect=[mock_info_response, mock_char_response])
    mocker.patch("random.randint", return_value=1) # Force the random ID

    character_info = api.get_random_character()
    assert "Name: Rick Sanchez (ID: 1)" in character_info
    assert "Status: Alive" in character_info

def test_get_character_by_id(mocker):
    """Tests fetching a specific character by ID."""
    mock_response = Mock()
    mock_response.json.return_value = {
        "id": 2, "name": "Morty Smith", "status": "Alive",
        "species": "Human", "origin": {"name": "Earth (C-137)"}
    }
    mock_response.raise_for_status.return_value = None
    mocker.patch("requests.get", return_value=mock_response)

    character_info = api.get_character_by_id(2)
    assert "Name: Morty Smith (ID: 2)" in character_info
    requests.get.assert_called_once_with("https://rickandmortyapi.com/api/character/2")

def test_get_characters_by_status(mocker):
    """Tests getting a list of characters by their status."""
    mock_response = Mock()
    mock_response.json.return_value = {
        "results": [{"name": "Abradolf Lincler"}, {"name": "Adjudicator Rick"}]
    }
    mock_response.raise_for_status.return_value = None
    mocker.patch("requests.get", return_value=mock_response)

    characters_list = api.get_characters_by_status("dead")
    assert "Characters with status 'dead':" in characters_list
    assert "- Abradolf Lincler" in characters_list
    requests.get.assert_called_once_with("https://rickandmortyapi.com/api/character/?status=dead")