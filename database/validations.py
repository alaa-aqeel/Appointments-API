import importlib as imp 

def import_class(modul_path):
    modul_path = modul_path.split(".")
    class_name = modul_path.pop()
    modul = imp.import_module(".".join(modul_path))
    
    return getattr(modul, class_name)

def unique(_modul: any, id: int= None) -> callable:

    def rule(field: str, value: str):
        modul = _modul # cop modul 
        if isinstance(modul, str): # check type is str 
            modul = import_class(modul) # imoprt model by string path 
        _field = getattr(modul, field) # get field 
        # modul filter 
        _is = modul.query.filter(_field==value).first()

        if _is: # if find rturn message 
            return f"field {field} is unique"
            
    return rule 

# required vaidate: (field: str, value: str) -> stirng | None 
required = lambda field, value: f"Field {field} is required"  if value == "" else None


class Validate:
    """Validate Data"""
    
    __rules = {}
    __errors = {}

    def __init__(self, rules: dict, values):
        self.__rules = rules
        self.values = values

    def __imp(sel, path):
        pass  

    def __get_value(self, field):
        """Get value for field"""

        if isinstance(self.values, dict):
            return self.values.get(field)
        return getattr(self.values, field)

    def validate(self):
        """Validate rules"""

        # read all rule & field in __rules 
        for field, rules in self.__rules.items():
            errors = [] # errors for field
            for rule in rules: # get rules
                # call rule 
                # :param field: name for field 
                # :param value: value for field 
                err = rule(field, self.__get_value(field))
                if err: # if return msg append to error 
                    errors.append(err)

            # if have errors add to errors dict
            if len(errors):
                self.__errors.update({field: errors})

    @property
    def errors(self):
        """Get Errors"""
        
        return self.__errors 