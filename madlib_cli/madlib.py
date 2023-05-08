import re

def read_template(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content.strip()
    except FileNotFoundError:
        raise FileNotFoundError("Invalid file path")

def parse_template(template):
    parts = tuple(re.findall(r'{(.*?)}', template))
    stripped_template = re.sub(r'{.*?}', '{}', template)
    return stripped_template, parts

def merge(template, user_inputs):
    return template.format(*user_inputs)

def collect_user_inputs(parts):
    return [input(f"Enter a value for {part}: ") for part in parts]

def write_to_file(content):
    with open("assets/Completed_Madlib.txt", 'w') as file:
        file.write(content)

def main():
    print("""
****************************************************
* Welcome to the Madlib game!                      *
*                                                  *
* In this game, you will be prompted to enter      *
* various types of words (e.g., nouns, adjectives, *
* verbs, etc.). These words will be used to fill   *
* in the blanks of a pre-written story, creating   *
* a fun and unique Madlib!                         *
*                                                  *
* Let's get started!                               *
****************************************************
""")
    template_path = "assets/Example.txt"
    template = read_template(template_path)
    stripped_template, parts = parse_template(template)

    user_inputs = collect_user_inputs(parts)
    completed_madlib = merge(stripped_template, user_inputs)

    print("\nCompleted Madlib:")
    print(completed_madlib)

    write_to_file(completed_madlib)

if __name__ == "__main__":
    main()