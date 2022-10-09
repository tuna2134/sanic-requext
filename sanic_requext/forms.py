from unittest.mock import NonCallableMagicMock, NonCallableMock
from sanic import Request

from functools import wraps


class FormField:

    name: str | None
    value: str | None
    def __init__(self):
        self.name = None
        self.value = None

class Form:
    fields: dict[str, FormField]
    
    def __init_subclass__(cls):
        cls.fields = {}
        for name, value in cls.__dict__.items():
            if isinstance(value, FormField):
                value.name = name
                cls.fields[name] = value
    
    @classmethod
    def decorator(cls, func):
        self = cls()
        @wraps(func)
        async def wrapper(request, *args, **kwargs):
            for name, field in self.fields.items():
                field.value = request.form.get(name)
            return await func(request, self, *args, **kwargs)
        return wrapper
    
    def __getattr__(self, name: str) -> FormField:
        return self.fields[name]