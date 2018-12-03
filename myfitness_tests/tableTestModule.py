import unittest
from myfitness.summary import table

class Testtable(unittest.TestCase):
    # Define a class variable that determines if setUp was ever run
    ClassIsSetup = False
    ClassIsTornDown = False

    def setUp(self):
        # If it was not setup yet, do it
        if not self.ClassIsSetup:
            print "Initializing testing environment"
            self.setupClass()
            self.__class__.ClassIsSetup = True

    @classmethod
    def setupClass(cls):
        unittest.TestCase.setUp(cls)
        ## do set up work here ##

    def test_table(self):
        ## do get table tests here ##

    def tearDown(self):
        # If it was not torn down yet, do it
        if not self.ClassIsTornDown:
            print "Tearing down testing environment"
            self.tearDownClass()
            self.__class__.ClassIsTornDown = True

    @classmethod
    def tearDownClass(cls):
        unittest.TestCase.tearDown(cls)
