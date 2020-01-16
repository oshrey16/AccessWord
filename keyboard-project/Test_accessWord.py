import _tkinter
import unittest
import tkinter
import accessWord

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.root = tkinter.Tk()
        self.pump_events()

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pump_events()

    def pump_events(self):
        while self.root.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
            pass


class test_accessWord(MyTestCase):
    def test_user_Register(self):
        self.assertTrue(self.root)

    def test_login_blind(self):
        self.assertTrue(self.root)

    def user_login_deaf(self):
        self.assertTrue(self.root)

    def test_admin_login(self):
        self.assertTrue(self.root)

    def test_Main(self):








if __name__ == '__main__':
    unittest.main()
