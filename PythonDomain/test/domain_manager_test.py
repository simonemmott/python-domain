'''
Created on 25 Dec 2018

@author: simon
'''
import unittest
from k2_domain import DomainManager
import test_domain


class TestDomainManager(unittest.TestCase):


    def test_new_domain_manager(self):
        
        app = {}
        config = {}
        
        dm = DomainManager(app, test_domain, config)
        
        self.assertEqual('test_domain', dm.name())
        self.assertEqual('A Test Domain', dm.title())
        self.assertEqual('A test domain', dm.description())
        
        self.assertEquals(dm, test_domain.manager)
        
        self.assertEqual('test_domain', dm.service.domain_name())
        self.assertEqual('A Test Domain', dm.service.domain_title())
        self.assertEqual('A test domain', dm.service.domain_description())
        self.assertEqual(dm, dm.service.manager)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()