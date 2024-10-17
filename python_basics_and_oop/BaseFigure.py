class BaseFigure:

    def __init__(self):
        self.validate()

    @classmethod
    def n_dots(cls):
        return None

    def area(self):
        raise NotImplementedError("Not implemented")

    def validate(self):
        raise NotImplementedError("Not implemented")



    
    
