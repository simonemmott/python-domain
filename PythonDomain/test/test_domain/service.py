'''
Created on 12 Jan 2019

@author: simon
'''
from k2_domain import DomainService

class TestDomainService(DomainService):
    
    def domain_name(self):
        return self.manager.name()
    
    def domain_title(self):
        return self.manager.title()
    
    def domain_description(self):
        return self.manager.description()
    
    