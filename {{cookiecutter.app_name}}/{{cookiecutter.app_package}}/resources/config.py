from oarepo_ui.resources.config import RecordsUIResourceConfig

class {{cookiecutter.resource_config}}(RecordsUIResourceConfig):
    template_folder = "../templates"
    url_prefix = "{{cookiecutter.url_prefix}}"
    blueprint_name = "{{cookiecutter.app_name}}"
    ui_serializer_class = "{{cookiecutter.ui_serializer_class}}"
    api_service = "{{cookiecutter.api_service}}"
    layout = "{{cookiecutter.api_service}}"

    templates = {
        "detail": {
            "layout": "oarepo_ui/generic_detail.html.jinja2",
            "blocks": {"record_main_content": "{{cookiecutter.app_package}}/main.html"},
        },
        "search": {"layout": "oarepo_ui/search.html.jinja2"},
    }
