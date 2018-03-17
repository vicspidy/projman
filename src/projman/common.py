import os
import yaml
import glob
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

__all__ = ['get_yaml_config', 'get_available_configs', 'get_available_types', 'get_project_location', 'AVAILABLE_TYPES',
           'AVAILABLE_CONFIGS', 'PROJECT_LOCATION', 'show_types', 'display_structre']

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
                        try:
                            file_desc = open(os.path.join(path, file), 'r')
                            data = yaml.load(file_desc)
                            file_desc.close()
                            yaml_configs.extend(data)
                        except yaml.YAMLError, exc:
                            sys.stderr.write('Error found in file: {0}'.format(file_desc.name))
                            sys.exit(4)

        # pp.pprint(yaml_configs)
        return yaml_configs
    else:
        return None

def _get_available_config():
    for config in get_yaml_config():
        if isinstance(config, dict):
            if config.get('value'):
                for key, val in config['value'].iteritems():
                    if key not in AVAILABLE_TYPES:
                        AVAILABLE_TYPES.add(key)
                        AVAILABLE_CONFIGS[key] = config
                    break

def get_available_configs():
    if not AVAILABLE_CONFIGS:
        _get_available_config()
    return AVAILABLE_CONFIGS

def get_available_types():
    if not AVAILABLE_TYPES:
        _get_available_config()
        return AVAILABLE_TYPES

def get_project_location(args):
    global PROJECT_LOCATION
    if args.path:
        PROJECT_LOCATION = args.path
        return PROJECT_LOCATION
    elif os.environ.get('PROJMAN_LOCATION'):
        PROJECT_LOCATION = os.environ['PROJMAN_LOCATION']
        return PROJECT_LOCATION
    else:
        user_home = os.path.expanduser('~' + os.environ['USERNAME'])
        project_location = os.path.join(user_home, 'projman', 'projects')
        if not os.path.exists(project_location):
            os.makedirs(project_location)

        PROJECT_LOCATION = project_location
        return PROJECT_LOCATION

def show_types(args):
    print 'Types of projects you can create..'
    for type_of_project in AVAILABLE_TYPES:
        print '\t' + '-' + type_of_project

def display_structre(args):
    for type, config in AVAILABLE_CONFIGS.iteritems():
        pp.pprint(config)

get_available_configs()