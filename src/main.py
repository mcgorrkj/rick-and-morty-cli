import argparse
from src import api

def main():
    """
    Defines the CLI commands and executes the corresponding functions.
    """
    parser = argparse.ArgumentParser(
        description="Get Rick and Morty character info from your terminal."
    )
    subparsers = parser.add_subparsers(
        dest="command", 
        help="Available commands", 
        required=True
    )

    # Command: random
    parser_random = subparsers.add_parser(
        "random", 
        help="Get a random character."
    )
    parser_random.set_defaults(func=lambda args: print(api.get_random_character()))

    # Command: id <character_id>
    parser_id = subparsers.add_parser(
        "id", 
        help="Get a specific character by their ID."
    )
    parser_id.add_argument(
        "character_id", 
        type=int, 
        help="The ID of the character."
    )
    parser_id.set_defaults(func=lambda args: print(api.get_character_by_id(args.character_id)))
    
    # Command: status <status_name>
    parser_status = subparsers.add_parser(
        "status", 
        help="List characters by status (alive, dead, or unknown)."
    )
    parser_status.add_argument(
        "name", 
        type=str, 
        help="The status to filter by."
    )
    parser_status.set_defaults(func=lambda args: print(api.get_characters_by_status(args.name)))

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()