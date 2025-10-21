import pytest
from unittest.mock import patch
from src import main

@patch('src.api.get_random_character', return_value="Random Character Info")
def test_main_random_command(mock_api_call, capsys):
    """Tests the 'random' CLI command."""
    with patch('sys.argv', ['main.py', 'random']):
        main.main()
    captured = capsys.readouterr()
    assert "Random Character Info" in captured.out

@patch('src.api.get_character_by_id', return_value="Character ID Info")
def test_main_id_command(mock_api_call, capsys):
    """Tests the 'id' CLI command."""
    with patch('sys.argv', ['main.py', 'id', '5']):
        main.main()
    captured = capsys.readouterr()
    mock_api_call.assert_called_once_with(5)
    assert "Character ID Info" in captured.out

@patch('src.api.get_characters_by_status', return_value="Character Status Info")
def test_main_status_command(mock_api_call, capsys):
    """Tests the 'status' CLI command."""
    with patch('sys.argv', ['main.py', 'status', 'alive']):
        main.main()
    captured = capsys.readouterr()
    mock_api_call.assert_called_once_with('alive')
    assert "Character Status Info" in captured.out