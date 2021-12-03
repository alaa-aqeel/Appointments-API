from pydantic import parse_obj_as, BaseModel as Model
from typing import List
from pydantic.error_wrappers import ValidationError, ErrorWrapper


class BaseModel(Model):

    _rules = []

    _rules_errors = []

    def add_error(self, error: Exception, fieldname: str):
        self._rules_errors.append(
            ErrorWrapper(error, loc=fieldname)
        )

    @classmethod
    def validate(cls, value):
        if isinstance(value, dict):
            obj = cls(**value)
            cls._rules_errors = []
            for rule in obj._rules:
                rule(obj, value)

            if len(cls._rules_errors):
                raise ValidationError(cls._rules_errors, cls)
                
            return obj
        else:
            return cls.from_orm(value)


class BaseSchema():


    def parse(self, schema=None):
        schema = schema if schema else self.__schema__

        return schema.from_orm(self)

    @classmethod  
    def parse_all(cls, model: object=None, schema: object =None) -> object:
        """Parse model orm to Pydantic model """
        schema = schema if schema else cls.__schema__

        # if model:
        #     return parse_obj_as(List[schema], model)

        return parse_obj_as(List[schema], cls.query.all())
