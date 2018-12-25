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
        