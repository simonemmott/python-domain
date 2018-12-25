from utilities import strUtil

class DomainConfig(object):
    def __init__(self, name, **kw):
        self.name = strUtil.underscoreCase(name.lower())
        self.title = kw.get('title', strUtil.titleCase(name))
        self.data = kw.get('data', '${k2_HOME}/data/'+self.name)
        