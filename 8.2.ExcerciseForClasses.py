# define the vehicle class
class Vehicle:
    name = ""
    kind = "car"
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%f.2f." % (
            self.name, self.color, self.kind, self.value)
        return desc_str
    # My code goes here
