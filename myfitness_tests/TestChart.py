
# coding: utf-8

# In[1]:


import unittest
import pandas as pd
import pygal 
from IPython.display import SVG, display


from myfitness.healthdata import chart

class TestChart (unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Initializing testing environment")

    def setUp(self):
        unittest.TestCase.setUp(self)
        ## do set up work here ##
        columnX = ['A','B','C','D','E']
        columnY = [1,2,3,4,5]
        self.testchart = chart.chart(columnX, columnY, 'letters', 'numbers')

    def test_chart(self): 
        #do chart tests here 
        
        #Check pygal chart
        self.assertIsInstance(self.testchart, pygal.Bar)
        
        #Check title
        self.assertEqual(self.testchart.title, 'My Fitness Chart')
        
        #Check x_title
        self.assertEqual(self.testchart.x_title, 'letters')
        
        #Check y_title
        self.assertEqual(self.testchart.y_title, 'numbers')
        
        #Check x_labels
        self.assertEqual(self.testchart.x_labels, ['A','B','C','D','E'])

    def tearDown(self):
        del(self.testchart)
            
    @classmethod
    def tearDownClass(cls):
        print("Tearing Down Testing Environment")
        

