from oarepo_ui.resources.config import RecordsUIResourceConfig

class {{cookiecutter.resource_config}}(RecordsUIResourceConfig):
    template_folder = "../theme/templates"
    detail_template = "{{cookiecutter.app_package}}/detail.html"
    search_template = "{{cookiecutter.app_package}}/search.html"
    url_prefix = "{{cookiecutter.url_prefix}}"
