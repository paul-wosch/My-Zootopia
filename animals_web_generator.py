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


def get_animal_basics(animal):
    """Return name, diet, first location and type for a given animal"""
    # initialize dictionary
    animal_basics = {"name": "",
                     "diet": "",
                     "location": "",
                     "type": ""
                     }
    # populate dictionary
    animal_basics["name"] = animal["name"]
    animal_basics["diet"] = animal["characteristics"].get("diet", "")
    animal_basics["type"] = animal["characteristics"].get("type", "")
    if animal["locations"]:
        animal_basics["location"] = animal["locations"][0]

    return animal_basics


def get_formated_animal_basics(animal_basics):
    """Return formatted animal basics."""
    output = "\n".join(f"{key.title()}: {value}"
                       for key, value
                       in animal_basics.items()
                       if value)
    return output


def indent(n):
    """Return n indentations."""
    return INDENTATION * n


def serialize_animal_basics_to_html(animal_basics):
    """Return animal basics serialized as HTML."""
    html_tags = {"li": ["<li class='cards__item'>", "</li>"],
                     "br": "<br/>"}
    output = ""
    output += indent(3) + html_tags["li"][0]
    output += f"\n{indent(3)}"
    output += f"\n{indent(3)}".join(f"{key.title()}: {value}{html_tags['br']}"
                                     for key, value
                                     in animal_basics.items()
                                     if value)
    output += "\n" + indent(3) + html_tags["li"][1]
    return output


def print_all_animal_basics(animals):
    """Print basic information for each animal
    for the given json animal data."""
    for animal in animals:
        animal_basics = get_animal_basics(animal)
        print(get_formated_animal_basics(animal_basics) + "\n")


def get_all_animal_basics(animals):
    """Return basic information for each animal
    for the given json animal data as string."""
    output = ""
    for animal in animals:
        animal_basics = get_animal_basics(animal)
        output += get_formated_animal_basics(animal_basics) + "\n\n"
    return output


def serialize_all_animal_basics_to_html(animals):
    """Return basic information for each animal
    for the given json animal data serialized as HTML."""
    output = ""
    for animal in animals:
        animal_basics = get_animal_basics(animal)
        output += serialize_animal_basics_to_html(animal_basics) + "\n"
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


def render_html_file(template_file, new_file, content):
    """Render a new html file for the given content."""
    html_template = load_template(template_file)
    html_new = html_template.replace(PLACEHOLDER, content)
    write_file(new_file, html_new)


def main():
    """Generate our HTML file here."""
    animals_data = load_data(JSON_DATA)
    content = serialize_all_animal_basics_to_html(animals_data)
    render_html_file(TEMPLATE_FILE, NEW_FILE, content)


if __name__ == "__main__":
    main()