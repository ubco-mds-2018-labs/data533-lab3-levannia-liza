import unittest
from maxMinTestModule import TestmaxMin
from tableTestModule import Testtable

def myFitness_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestmaxMin))
    suite.addTest(unittest.makeSuite(Testtable))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

myFitness_suite()
