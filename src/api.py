import requests
import random

BASE_URL = "https://rickandmortyapi.com/api"

def get_random_character():
    """
    Fetches a random Rick and Morty character.

    First finds the total number of characters, then requests a
    single character using a random ID in that range.

    Returns:
        str: A formatted string with the character's details or an error message.
    """
    try:
        # Get the total count of characters
        initial_response = requests.get(f"{BASE_URL}/character")
        initial_response.raise_for_status()
        count = initial_response.json()['info']['count']

        # Pick a random ID and fetch that character
        random_id = random.randint(1, count)
        return get_character_by_id(random_id)
    except requests.exceptions.RequestException as e:
        return f"Error: Could not retrieve a random character. {e}"

def get_character_by_id(character_id):
    """
    Fetches a specific character by their ID.

    Args:
        character_id (int): The ID of the character to fetch.

    Returns:
        str: A formatted string with the character's details or an error message.
    """
    try:
        response = requests.get(f"{BASE_URL}/character/{character_id}")
        response.raise_for_status()
        char_data = response.json()
        return (
            f"Name: {char_data['name']} (ID: {char_data['id']})\n"
            f"Status: {char_data['status']}\n"
            f"Species: {char_data['species']}\n"
            f"Origin: {char_data['origin']['name']}"
        )
    except requests.exceptions.RequestException as e:
        return f"Error: Could not retrieve character with ID {character_id}. {e}"

def get_characters_by_status(status):
    """
    Fetches characters by their status (alive, dead, or unknown).

    Args:
        status (str): The status to filter by.

    Returns:
        str: A formatted string listing character names or an error message.
    """
    if status.lower() not in ['alive', 'dead', 'unknown']:
        return "Error: Invalid status. Please use 'alive', 'dead', or 'unknown'."
    
    try:
        response = requests.get(f"{BASE_URL}/character/?status={status}")
        response.raise_for_status()
        data = response.json()
        
        # Format the names of the first 5 characters found
        names = [f"- {char['name']}" for char in data['results'][:5]]
        return f"Characters with status '{status}':\n" + "\n".join(names)

    except requests.exceptions.RequestException as e:
        return f"Error: Could not retrieve characters. {e}"