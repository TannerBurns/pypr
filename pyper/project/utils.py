
class PyperVersion(object):

    def __init__(self, projectName:str, version: str):
        self.projectName = projectName
        self.major, self.minor, self.patch = self.version_parse(version)
    
    def version_parse(self, version: str):
        version_split = version.split('.')
        if len(version_split) != 3:
            raise TypeError('version is not proper format, looking for major.minor.patch (0.0.0)')
        return int(version_split[0]), int(version_split[1]), int(version_split[2])
    
    def set_version(self, new_version: str):
        self.major, self.minor, self.patch = self.version_parse(new_version)
    
    def get_version(self):
        return f'{self.major}.{self.minor}.{self.patch}'

    def print_version(self):
        return f'{self.projectName} version: {self.major}.{self.minor}.{self.patch}'
    
    def increment_patch(self, increaseBy: int):
        self.patch += increaseBy
    
    def increment_minor(self, increaseBy: int):
        self.minor += increaseBy
    
    def increase_major(self, increaseBy: int):
        self.major += increaseBy
    
    
