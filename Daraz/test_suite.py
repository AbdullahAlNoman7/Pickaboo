import unittest
from Daraz.test_case1 import DarazLogin
from Daraz.test_case2 import AddToCard

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DarazLogin(''))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())