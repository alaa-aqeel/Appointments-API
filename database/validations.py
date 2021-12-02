

def unique_valid(field: str, model: object) -> callable:

    def rule(obj, values):
        value = values.get(field, getattr(obj, field))
        _field = getattr(model, field)

        if model.query.filter(_field==value).first(): 
            obj.add_error(ValueError(f"Field {field} is uniqued"), field) 

    return rule