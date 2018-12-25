'''
Created on 25 Dec 2018

@author: simon
'''
import unittest
from k2_domain import DomainConfig


class TestDomainConfig(unittest.TestCase):


    def test_new_domain_config(self):
        dc = DomainConfig('My domain')
        self.assertEqual('my_domain', dc.name)
        self.assertEqual('My Domain', dc.title)
        self.assertEqual('${k2_HOME}/data/my_domain', dc.data)

    def test_new_domain_config_details(self):
        dc = DomainConfig('My domain', title='My Title', data='/xxx/yyy/zzz')
        self.assertEqual('my_domain', dc.name)
        self.assertEqual('My Title', dc.title)
        self.assertEqual('/xxx/yyy/zzz', dc.data)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()