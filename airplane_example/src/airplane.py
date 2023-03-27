class Airplane:
    def __init__(self, type, crew, destination):
        self.type = type
        self.crew = crew
        self.destination = destination

    def add_member(self, new_member):
        self.crew.append(new_member)
        return self.crew
    
    def check_glue(self):
        return "This is the wrong day to stop sniffing glue"
    
    def hasShirley(self):
        for member in self.crew:
            if member == "Shirley":
                return "Please, call me Shirley"
            
        return "Don't call me Shirley"
