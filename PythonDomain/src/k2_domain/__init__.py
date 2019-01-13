from utilities import strUtil


class DomainConfig(object):
    def __init__(self, name, **kw):
        if not kw.get('dict'):
            self.name = strUtil.underscoreCase(name.lower())
            self.title = kw.get('title', strUtil.titleCase(name))
            self.data = kw.get('data', '${k2_HOME}/data/'+self.name)
        else:
            self._populate_from_data(kw.get('dict'))
            
    def _populate_from_data(self, data):
        self.name = data.get('name')
        self.title = data.get('title', strUtil.titleCase(self.name))
        self.data = data.get('data', '${k2_HOME}/data/'+self.name)
        
class DomainError(Exception):
    pass
        
class DomainManager(object):
    def __init__(self, app, module, config):
        self.app = app
        self.module = module
        self.config = config
        module.manager = self
        self.service = module.get_service_class()(self)
        module.service = self.service
        module.config = config
        
    def name(self):
        return self.module.__name__
    
    def title(self):
        return self.module.title
    
    def description(self):
        return self.module.description
        
        
class DomainService(object):
    manager = None
    def __init__(self, manager):
        self.manager = manager