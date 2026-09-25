def on_config(config):
    """
    Conditionally change the navigation depending on the theme.
    Remark: Each time I change something here, I have to restart: mkdocs serve (it won't update automatically)
    """
    theme_name = config.theme.name

    if theme_name == "mkdocs": # Navigation for "bootstrap" theme (the default theme, but I have to use "mkdocs", not "bootstrap" as the name here)
        config.nav = [
            {"Introduction": "index.md"}, # this file "index.md" must be in docs/
            {"Lectures": [  
                {"Lecture 1: Trivia": "Lecture_1.md"},
                {"Lecture 2: Commands and variables": "Lecture_2.md"},
                {"Lecture 3: Linux file system. Positional parameters. Your first Linux/Bash command. Command precedence": "Lecture_3.md"},
                {"Lecture 4: Loops and few other thingies": "Lecture_4.md"},
            ]},
            {"Homeworks": [  
                {"Scoresheet": "Homeworks/Scoresheet.md"},
                {"Homework 1: Using shell aliases as your simplest commands" : "Homeworks/Homework_1.md"},
                {"Homework 2: User-made executables as Linux/Bash commands": "Homeworks/Homework_2.md"},
            ]},
        ]

    elif theme_name == "material": # Navigation for "Material" theme
        config.nav = [
            {"Introduction": "index.md"}, # this file "index.md" must be in docs/
            {"Lectures": [  
                {"Lecture 1: Trivia": "Lecture_1.md"},
                {"Lecture 2: Commands and variables": "Lecture_2.md"},
                {"Lecture 3: Linux file system. Positional parameters. Your first Linux/Bash command. Command precedence": "Lecture_3.md"},
                {"Lecture 4: Loops and few other thingies": "Lecture_4.md"},
            ]},
            {"Homeworks": [  
                {"Scoresheet": "Homeworks/Scoresheet.md"},
                {"Homework 1: Using shell aliases as your simplest commands" : "Homeworks/Homework_1.md"},
                {"Homework 2: User-made executables as Linux/Bash commands": "Homeworks/Homework_2.md"},
            ]},
        ]

    elif theme_name == "readthedocs": # Different structure for "ReadTheDocs" theme
        config.nav = [
            {"Introduction": "index.md"}, # this file "index.md" must be in docs/
            {"Lectures": [  
                {"Lecture 1: Trivia": "Lecture_1.md"},
                {"Lecture 2: Commands and variables": "Lecture_2.md"},
                {"Lecture 3: Linux file system. Positional parameters. Your first Linux/Bash command. Command precedence": "Lecture_3.md"},
                {"Lecture 4: Loops and few other thingies": "Lecture_4.md"},
            ]},
            {"Homeworks": [  
                {"Scoresheet": "Homeworks/Scoresheet.md"},
                {"Homework 1: Using shell aliases as your simplest commands" : "Homeworks/Homework_1.md"},
                {"Homework 2: User-made executables as Linux/Bash commands": "Homeworks/Homework_2.md"},
            ]},
        ]

    else: # Optional: fallback for unknown themes
        config.nav = [
            {"Home": "index.md"},
        ]

    return config
