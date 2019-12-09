from marshmallow import Schema, fields
from werkzeug.datastructures import FileStorage
from typing import Any, Mapping, Union


class FileStorageField(fields.Field):
    default_error_messages = {
        "invalid": "Not a valid image."
    }

    def deserialize(
        self,
        value: Any,
        attr: str = None,
        data: Mapping[str, Any] = None,
        **kwargs
    ) -> Union[FileStorage, None]:
        if value is None:
            return None

        if not isinstance(value, FileStorage):
            self.fail("invalid")

        return value


class ImageSchema(Schema):
    image = FileStorageField(required=True)
