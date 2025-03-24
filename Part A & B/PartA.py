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


# A5 #
class Manager(Staff):
    def __init__(self, name, DoB, sex, staffID, address, department, level):
        super().__init__(name, DoB, sex, staffID, address)
        self.department = department
        self.level = level

    # A6 #
    def show_profile(self):
        self.display_details()
        print("Department:", self.department)
        print("Level:", self.level)

    # A7 #
    def set_department(self, value):
        if isinstance(value, str):
            self.department = value

    def set_level(self, value):
        if isinstance(value, int):
            self.level = value


# A8 #
basic_staff = Staff("Michael Babatunde", "2000-10-10", "Male", 3001, "123 Africa Road")
senior_manager = Manager("Jesutobiloba Robertson", "2024-11-14", "Male", 3002, "17 Benin Avenue", "Operations", 5)

# A9 #
print("\nStaff Member")
basic_staff.display_details()

print("\nManager Profile")
senior_manager.show_profile()

# A10 #
print("\nUpdating Staff")
basic_staff.set_name("Najeeb Adeniran")
basic_staff.set_address("88 Libyan Crossing")
basic_staff.display_details()

print("\nUpdating Manager")
senior_manager.set_department("Logistics")
senior_manager.set_level(6)
senior_manager.show_profile()
