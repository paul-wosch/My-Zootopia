import json


def load_data(file_path):
    """Load a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animal_basics(animal):
    """Return name, diet, first location and type for a given animal"""
    # initialize dictionary
    animal_basics = {"name": "",
                     "diet": "",
                     "first_location": "",
                     "type": ""
                     }
    # populate dictionary
    animal_basics["name"] = animal["name"]
    animal_basics["diet"] = animal["characteristics"].get("diet", "")
    animal_basics["type"] = animal["characteristics"].get("type", "")
    if animal["locations"]:
        animal_basics["locations"] = animal["locations"][0]

    return animal_basics


def get_formated_animal_basics(animal_basics):
    """Create formatted output for animal basics."""
    output = "\n".join(f"{key.title()}: {value}"
                       for key, value
                       in animal_basics.items()
                       if value)
    return output


def print_all_animal_basics(animals):
    """Print basic information for each animal
    for the given json animal data."""
    for animal in animals:
        animal_basics = get_animal_basics(animal)
        print(get_formated_animal_basics(animal_basics) + "\n")


def main():
    """Generate our HTML file here."""
    animals_data = load_data('animals_data.json')
    print_all_animal_basics(animals_data)


if __name__ == "__main__":
    main()