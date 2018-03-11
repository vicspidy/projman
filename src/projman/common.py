import os
import yaml
import glob
import shutil

__all__ = ['get_yaml_config', 'get_available_configs', 'get_available_types', 'get_project_location', 'AVAILABLE_TYPES',
           'AVAILABLE_CONFIGS', 'PROJECT_LOCATION']

KNOWN_TYPES = ['maya', 'houdini', 'nuke', 'photoshop', 'blender']
AVAILABLE_TYPES = set()
AVAILABLE_CONFIGS = dict()
PROJECT_LOCATION = None

def get_yaml_config():
    yaml_configs = list()
    if os.environ.get('PROJMAN_TEMPLATES'):
        yaml_paths = os.environ['PROJMAN_TEMPLATES'].split(';')
        for path in yaml_paths:
            if os.path.exists(path):
                for type in ('*.yml', '*.yaml'):
                    files_found = glob.glob(type)
                    for file in files_found:
                        file_desc = open(file, 'r')
                        data = yaml.load(file_desc)
                        file_desc.close()
                        yaml_configs.extend(data)

        return yaml_configs
    else:
        return None

def _get_available_config():
    for config in get_yaml_config():
            for v in config.values():
                if isinstance(v, dict):
                    for type, config in v.iteritems():
                        if type in KNOWN_TYPES:
                            AVAILABLE_TYPES.add(type)
                            temp_dict = dict()
                            temp_dict[type] = config
                            AVAILABLE_CONFIGS[type] = temp_dict

def get_available_configs():
    if not AVAILABLE_CONFIGS:
        _get_available_config()
        return AVAILABLE_CONFIGS

def get_available_types():
    if not AVAILABLE_TYPES:
        _get_available_config()
        return AVAILABLE_TYPES

def get_project_location():
    if os.environ.get('PROJMAN_LOCATION'):
        return os.environ['PROJMAN_LOCATION']



PROJECT_LOCATION = get_project_location()
get_available_configs()