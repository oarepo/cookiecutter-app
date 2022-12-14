from {{cookiecutter.app_package}}.proxies import current_ui

def create_blueprint(app):
    """Blueprint for the routes and resources provided by current ui's resource."""
    return current_ui.resource.as_blueprint()
