# Copyright (c) 2022 CESNET
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from .ext import {{ cookiecutter.ext_name }}
from .version import __version__

__all__ = ('__version__', '{{cookiecutter.ext_name}}')
