import unittest
from PartA import Staff, Manager


class TestStaffAndManager(unittest.TestCase):

    def setUp(self):
        self.staff = Staff("Onas Michael", "1994-04-04", "Female", 1001, "12 Congo Road")
        self.manager = Manager("Benson Benjamin", "2012-12-12", "Male", 1002, "46 Mali Grove", "HR", 3)

    # B2 #
    def test_staff_instance(self):
        self.assertIsInstance(self.staff, Staff)

    def test_manager_instance(self):
        self.assertIsInstance(self.manager, Manager)
        self.assertIsInstance(self.manager, Staff)

    # B3 #
    def test_staff_not_manager(self):
        self.assertNotIsInstance(self.staff, Manager)

    # B4 #
    def test_objects_identical(self):
        same_ref = self.staff
        self.assertIs(self.staff, same_ref)

    def test_objects_not_identical(self):
        another_staff = Staff("Onas Michael", "1999-04-04", "Female", 1001, "12 Congo Road")
        self.assertIsNot(self.staff, another_staff)

    # B5 #
    def test_set_name(self):
        self.staff.set_name("Benson")
        self.assertEqual(self.staff.name, "Benson")

    def test_set_DoB(self):
        self.staff.set_DoB("2010-12-12")
        self.assertEqual(self.staff.DoB, "2010-12-12")

    def test_set_sex(self):
        self.staff.set_sex("Non-Affirming Genderfluid")
        self.assertEqual(self.staff.sex, "Non-Affirming Genderfluid")

    def test_set_staffID(self):
        self.staff.set_staffID(2002)
        self.assertEqual(self.staff.staffID, 2002)

    def test_set_address(self):
        self.staff.set_address("64 Zoo Lane")
        self.assertEqual(self.staff.address, "64 Zoo Lane")

    def test_set_department(self):
        self.manager.set_department("Agriculture")
        self.assertEqual(self.manager.department, "Agriculture")

    def test_set_level(self):
        self.manager.set_level(5)
        self.assertEqual(self.manager.level, 5)


# B6 #
def main():
    unittest.main()


if __name__ == "__main__":
    main()
