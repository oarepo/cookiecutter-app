from oarepo_ui.resources.config import RecordsUIResourceConfig

class {{cookiecutter.resource_config}}(RecordsUIResourceConfig):
    template_folder = "../theme/templates"
    detail_template = "{{cookiecutter.app_package}}/detail.html"
    search_template = "{{cookiecutter.app_package}}/search.html"
    url_prefix = "{{cookiecutter.url_prefix}}"
    blueprint_name = "{{cookiecutter.app_name}}"
    ui_serializer_class = "{{cookiecutter.ui_serializer_class}}"
    api_service = "{{cookiecutter.api_service}}"
