
# coding: utf-8

# In[10]:


import unittest
import pandas as pd

from myfitness.healthdata import data

class TestDataPerson(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Initializing testing environment")
        
    def setUp(self):
        self.p1 = data.Person('Liza', 30, 'F')
        self.healthdata_p1 = data.healthdata('Liza', 30, 'F', "Health Data.csv")

    def test_data(self): 
        #Tests for data module
        
        #Check that the name is Liza
        self.assertEqual(self.p1.name, 'Liza')
        
        #Check age is 30
        self.assertEqual(self.p1.age, 30)
        
        #Check gender is F
        self.assertEqual(self.p1.gender, 'F')
        
        #Check display
        self.assertEqual(self.p1.display(), 'Name: Liza, Age: 30, Gender: F')
        
        #Check healthdata file
        self.assertEqual(self.healthdata_p1.file, 'Health Data.csv')
        
        #Check data import 
        self.assertIsInstance(self.healthdata_p1.data(), pd.DataFrame)
        
        
    def tearDown(self):
            del(self.p1)
            del(self.healthdata_p1)
            
    @classmethod
    def tearDownClass(cls):
        print("Tearing Down Testing Environment")

