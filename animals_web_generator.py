import json

JSON_DATA = "animals_data.json"
TEMPLATE_FILE = "animals_template.html"
NEW_FILE = "animals.html"
PLACEHOLDER = "            __REPLACE_ANIMALS_INFO__"
INDENTATION = "    "


def load_data(file_path):
    """Load a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def initialize_animal_obj():
    """Initialize and return preprocessed animal object."""
    animal_obj = {"name": "",
                  "diet": "",
                  "location": "",
                  "type": ""
                  }
    return animal_obj


def populate_animal_obj(animal):
    """Return populated animal object."""
    animal_obj = initialize_animal_obj()
    animal_obj["name"] = animal["name"]
    animal_obj["diet"] = animal["characteristics"].get("diet", "")
    animal_obj["type"] = animal["characteristics"].get("type", "")
    if animal["locations"]:
        animal_obj["location"] = animal["locations"][0]
    return animal_obj


def get_animal(animal):
    """Return name and details for a given animal."""
    animal_obj = populate_animal_obj(animal)
    return animal_obj


def get_formated_animal(animal_obj):
    """Return formatted animal basics."""
    output = "\n".join(f"{key.title()}: {value}"
                       for key, value
                       in animal_obj.items()
                       if value)
    return output


def indent(n):
    """Return n indentations."""
    return INDENTATION * n


def serialize_animal_to_html(animal_obj):
    """Return animal information serialized as HTML.

    Simplified version using strings with plain HTML.
    """
    output = ''
    output += f'{indent(3)}<li class="cards__item">'
    output += f'\n{indent(4)}<div class="card__title">{animal_obj["name"]}</div>'
    output += f'\n{indent(4)}<div class="card__text">'
    output += f'\n{indent(5)}<ul class="cards">'
    output += f'\n{indent(6)}'
    output += f'\n{indent(6)}'.join(f'<li><strong>{key.title()}:</strong> {value}</li>'
                                    for key, value
                                    in animal_obj.items()
                                    if not key == "name" and value)
    output += f'\n{indent(5)}</ul>'
    output += f'\n{indent(4)}</div>'
    output += f'\n{indent(3)}</li>'

    return output


def serialize_all_animals_to_html(animals):
    """Return basic information for each animal
    for the given json animal data serialized as HTML."""
    output = ""
    for animal in animals:
        animal_obj = get_animal(animal)
        # output += serialize_animal_to_html_old(animal_obj) + "\n"
        output += serialize_animal_to_html(animal_obj) + "\n"
    return output


def load_template(template_file):
    """Load and return html template."""
    with open(template_file, "r", encoding="utf-8") as file_obj:
        html_template = file_obj.read()
    return html_template


def write_file(file_name, content):
    """Write a file with the given content."""
    with open(file_name, "w", encoding="utf-8") as file_obj:
        file_obj.write(content)


def write_html_file(template_file, new_file, content):
    """Write a new html file for the given content."""
    html_template = load_template(template_file)
    html_new = html_template.replace(PLACEHOLDER, content)
    write_file(new_file, html_new)


def main():
    """Generate our HTML file here."""
    animals_data = load_data(JSON_DATA)
    content = serialize_all_animals_to_html(animals_data)
    write_html_file(TEMPLATE_FILE, NEW_FILE, content)


if __name__ == "__main__":
    main()