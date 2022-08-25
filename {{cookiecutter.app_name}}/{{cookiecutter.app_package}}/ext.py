# Copyright (c) 2022 Miroslav Bauer
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

class {{cookiecutter.ext_name}}:
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.extensions["{{cookiecutter.app_package}}"] = self
