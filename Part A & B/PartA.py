# A2 #
class Staff:
    def __init__(self, name: str, DoB: str, sex: str, staffID: int, address: str):
        self.name = name
        self.DoB = DoB
        self.sex = sex
        self.staffID = staffID
        self.address = address

    # A3 #
    def display_details(self):
        print("Staff Details")
        print("Name:", self.name)
        print("DoB:", self.DoB)
        print("Sex:", self.sex)
        print("Staff-ID:", self.staffID)
        print("Address:", self.address)

    # A4 #
    def set_name(self, value):
        if isinstance(value, str):
            self.name = value

    def set_DoB(self, value):
        if isinstance(value, str):
            self.DoB = value

    def set_sex(self, value):
        if isinstance(value, str):
            self.sex = value

    def set_staffID(self, value):
        if isinstance(value, int):
            self.staffID = value

    def set_address(self, value):
        if isinstance(value, str):
            self.address = value


