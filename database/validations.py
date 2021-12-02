import importlib as imp 
def import_class(modul_path):
    modul_path = modul_path.split(".")
    class_name = modul_path.pop()
    modul = imp.import_module(".".join(modul_path))
    
    return getattr(modul, class_name)

def unique_valid(field: str, modul: object) -> callable:

    def rule(obj, values):
        module = import_class(modul)
        value = values.get(field, getattr(obj, field))
        _field = getattr(module, field)

        if module.query.filter(_field==value).first(): 
            obj.add_error(ValueError(f"Field {field} is uniqued"), field) 

    return rule