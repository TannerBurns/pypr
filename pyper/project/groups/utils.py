import json
import os

class PyperManifest(object):
    def __init__(self):
        self.manifest_path = './manifest.json'
        if not os.path.exists(self.manifest_path):
            raise Exception('Failed to find manifest.json in cwd')
        self.manifest = json.load(open(self.manifest_path, 'r'))

    def save(self):
        open(self.manifest_path, 'w').write(json.dumps(self.manifest, indent=4))


class PyperVersion(PyperManifest):

    def __init__(self):
        super().__init__()
        if not self.manifest.get('name') and not self.manifest.get('version'):
            raise Exception('Failed to load name and version from manifest.json')
        self.major, self.minor, self.patch = self.version_parse(self.manifest.get('version'))
    
    def version_parse(self, version: str):
        version_split = version.split('.')
        if len(version_split) != 3:
            raise TypeError('version is not proper format, looking for major.minor.patch (0.0.0)')
        return int(version_split[0]), int(version_split[1]), int(version_split[2])
    
    def set_version(self, new_version: str):
        self.major, self.minor, self.patch = self.version_parse(new_version)
        self.manifest['version'] = self.get_version()
    
    def get_version(self):
        return f'{self.major}.{self.minor}.{self.patch}'

    def print_version(self):
        return f'{self.manifest.get("name")} version: {self.major}.{self.minor}.{self.patch}'
    
    def increment_patch(self, increaseBy: int):
        self.patch += increaseBy
        self.manifest['version'] = self.get_version()
    
    def increment_minor(self, increaseBy: int):
        self.minor += increaseBy
        self.manifest['version'] = self.get_version()
    
    def increase_major(self, increaseBy: int):
        self.major += increaseBy
        self.manifest['version'] = self.get_version()
    
    
class PyperMetadata(PyperManifest):

    def __init__(self):
        super().__init__()
    
    def get_description(self):
        return f'{self.manifest.get("description")}'
    
    def set_description(self, description):
        self.manifest['description'] = description
    
    def get_author(self):
        return f'{self.manifest.get("author")}'
    
    def set_author(self, author):
        self.manifest['author'] = author
    
    def get_author_email(self):
        return f'{self.manifest.get("author_email")}'
    
    def set_author_email(self, author_email):
        self.manifest['author_email'] = author_email
    
    def get_url(self):
        return f'{self.manifest.get("url")}'
    
    def set_url(self, url):
        self.manifest['url'] = url
    

class PyperRequirements(PyperManifest):

    def __init__(self):
        super().__init__()
    
    def get_requirements(self):
        return self.manifest.get('requirements', [])
    
    def add_requirement(self, requirement):
        self.manifest['requirements'].append(requirement)
    
    def remove_requirement(self, requirement):
        self.manifest['requirements'].remove(requirement)
    

class PyperPackages(PyperManifest):

    def __init__(self):
        super().__init__()
    
    def get_included_packages(self):
        return self.manifest.get('package_include', [])
    
    def get_excluded_packages(self):
        return self.manifest.get('package_exclude', [])
    
    def add_included_packages(self, package):
        self.manifest['package_include'].append(package)
    
    def remove_included_packages(self, package):
        self.manifest['package_include'].remove(package)
    
    def add_excluded_packages(self, package):
        self.manifest['package_exclude'].append(package)
    
    def remove_excluded_packages(self, package):
        self.manifest['package_exclude'].remove(package)

