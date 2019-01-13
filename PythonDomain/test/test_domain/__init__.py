from test_domain.service import TestDomainService
from k2_domain import DomainError

title = 'A Test Domain'
description = 'A test domain'
manager = None
service = None
config = None
    
def get_service_class():
    return TestDomainService