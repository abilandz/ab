def on_config(config):
    """
    Conditionally add CSS files depending on the active theme.
    """
    theme_name = config.theme.name

    # Example: only load this CSS when using the "Material" theme"
    if theme_name == "material":
        config.extra_css.append("stylesheets/material/bootstrap-like-tables.css")

    # Example: only load this CSS when using the "Bootstrap" theme (default):
    elif theme_name == "bootstrap":
        config.extra_css.append("stylesheets/bootstrap/some-settings.css")

    # Example: only load this CSS when using the "ReadTheDocs" theme:
    elif theme_name == "readthedocs":
        config.extra_css.append("stylesheets/readthedocs/spacing.css")
        config.extra_css.append("stylesheets/readthedocs/colors.css")

    return config
