# Copyright (c) 2022 Miroslav Bauer
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from {{cookiecutter.app_package}} import config as config
from invenio_base.utils import obj_or_import_string
import re


class {{cookiecutter.ext_name}}:
    def __init__(self, app=None):
        if app:
            self.init_app(app)
            self.init_resource(app)

    def init_app(self, app):
        app.extensions["{{cookiecutter.app_package}}"] = self

    def init_resource(self, app):
        """Initialize vocabulary resources."""
        self.resource = obj_or_import_string(app.config["{{cookiecutter.app_package | upper}}_RESOURCE"])(
            api_config=obj_or_import_string(app.config["{{cookiecutter.app_package | upper}}_RESOURCE_API_CONFIG"])(),
            service=obj_or_import_string(app.config["{{cookiecutter.app_package | upper}}_RESOURCE_API_SERVICE"]),
            config=obj_or_import_string(app.config["{{cookiecutter.app_package | upper}}_RESOURCE_CONFIG"])(),
        )

    def init_config(self, app):
        """Initialize configuration."""
        for identifier in dir(config):
            if re.match("^[A-Z_]*$", identifier) and not identifier.startswith("_"):
                app.config.setdefault(identifier, getattr(config, identifier))

