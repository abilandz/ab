def on_config(config):
    """
    Conditionally change the navigation depending on the theme.
    Remark: Each time I change something here, I have to restart: mkdocs serve (it won't update automatically)
    """
    theme = config.theme.name

    if theme == "mkdocs": # Navigation for "Material" theme (default)  "bootstrap"
        config.nav = [
            {"Home": "index.md"}, # this file "index.md" must be in docs/
            {"Lecture 1": "Lecture_1.md"}, 
            {"Lecture 2": "Lecture_2.md"},
            {"Lecture 3": "Lecture_3.md"},
            {"Lecture 4": "Lecture_4.md"},
#            {"Lecture 2": "SS2026/Lecture_2/Lecture_2.md"},
#            {"Lecture 3": "SS2026/Lecture_3/Lecture_3.md"},
#            {"Lecture 4": "SS2026/Lecture_4/Lecture_4.md"},
#            {"Homeworks": "SS2026/Homeworks/Trivia.md"},
#            {"Documentation": [
#                "guide/installation.md",
#                "guide/usage.md",
#            ]},
#            {"API": "api.md"},
        ]

    elif theme == "material": # Navigation for "Material" theme
        config.nav = [
            {"Home": "index.md"}, # this file "index.md" must be in docs/
            {"Lecture 1": "Lecture_1.md"},
            {"Lecture 2": "Lecture_2.md"},
            {"Lecture 3": "Lecture_3.md"},
            {"Lecture 4": "Lecture_4.md"},
#            {"User Guide": [
#                "guide/installation.md",
#                "guide/usage.md",
#                "guide/advanced.md",
#            ]},
#            {"API Reference": "api.md"},
#            {"About": "about.md"},
        ]

    elif theme == "readthedocs": # Different structure for "ReadTheDocs" theme
        config.nav = [
            {"Home": "index.md"}, # this file "index.md" must be in docs/
            {"Lecture 1": "Lecture_1.md"},
            {"Lecture 2": "Lecture_2.md"},
            {"Lecture 3": "Lecture_3.md"},
            {"Lecture 4": "Lecture_4.md"},
#            {"Getting Started": [
#                "guide/installation.md",
#                "guide/usage.md",
#            ]},
#            "api.md",
#            "about.md",
        ]

    else: # Optional: fallback for unknown themes
        config.nav = [
            {"Home": "index.md"},
        ]

    return config
