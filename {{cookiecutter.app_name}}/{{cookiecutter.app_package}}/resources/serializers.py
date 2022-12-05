from flask_resources import BaseListSchema, MarshmallowSerializer
from flask_resources.serializers import JSONSerializer
from flask_resources import BaseObjectSchema
from flask_resources import ResponseHandler


class UIRecordSchema(BaseObjectSchema):
    pass


class UIJSONSerializer(MarshmallowSerializer):
    """UI JSON serializer."""

    def __init__(self):
        """Initialise Serializer."""
        super().__init__(
            format_serializer_cls=JSONSerializer,
            object_schema_cls=UIRecordSchema,
            list_schema_cls=BaseListSchema,
            schema_context={"object_key": "ui"},
        )


ui_serializers = {
    "application/vnd.inveniordm.v1+json": ResponseHandler(UIJSONSerializer()),
}
