# Copyright (c) 2022 CESNET
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""JS/CSS bundles for {{cookiecutter.app_name}}.

You include one of the bundles in a page like the example below (using
``base`` bundle as an example):

 .. code-block:: html

    {{ '{{' }} webpack['base.js'] {{ '}}' }}

"""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                'nr-documents-search': './js/{{cookiecutter.app_package}}/search/index.js'
            },
            dependencies={
            },
            aliases={
                '@js/{{cookiecutter.app_package}}': 'js/{{cookiecutter.app_package}}',
                '@uijs/{{cookiecutter.app_package}}': 'js/{{cookiecutter.app_package}}/ui_components',
            }
        )
    },
)
