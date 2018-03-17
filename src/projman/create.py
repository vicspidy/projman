import os
import common

__all__ = ['create_project', 'create_dir_structre']
yaml_data = common.get_yaml_config()

def create_project(args):
    new_project = os.path.join(common.PROJECT_LOCATION, args.name)
    if args.type:
        new_project_type = os.path.join(new_project, args.type)
        if os.path.exists(new_project_type):
            print "Project {0} already exists for {1}.".format(args.type, args.name)
            return
    else:
        if os.path.exists(new_project):
            print "Project {0} already exists.".format(args.name)
            return

    if not os.path.exists(new_project):
        os.makedirs(new_project)

    if args.type:
        if not args.type in common.AVAILABLE_TYPES:
            print 'No configuration found for type: {0}'.format(args.type)
            return
        else:
            create_dir_structre(args.type, new_project)
    else:
        create_dir_structre(None, new_project)



def create_dir_structre(type, project):
    """dict_to_dir expects yaml_dict to be a dictionary with one top-level key."""
    if os.path.exists(project):
        if type:
            _create_structre(common.AVAILABLE_CONFIGS[type], project)
        else:
            for type in common.AVAILABLE_TYPES:
                _create_structre(common.AVAILABLE_CONFIGS[type], project)

def _create_structre(yaml_data, dest, permission=None):
    if isinstance(yaml_data, dict):
        if yaml_data.get('permission'):
            permission = int(yaml_data['permission'], 8)

    if isinstance(yaml_data, dict):
        for k, v in yaml_data.iteritems():
            if k == 'value' and isinstance(v, str):
                if v.find('.') > 0:
                    file = open(os.path.join(dest, v), 'w')
                    if permission:
                        os.chmod(file.name, permission)
                    file.close()
                else:
                    new_folder = os.path.join(dest, v)
                    if permission:
                        os.mkdir(new_folder, permission)
                    else:
                        os.mkdir(new_folder)
            elif k == "value" and not isinstance(v, str):
                _create_structre(v, dest, permission)
            elif k != 'value' and not isinstance(v, str):
                new_folder = os.path.join(dest, k)
                if permission:
                    os.mkdir(new_folder, permission)
                else:
                    os.mkdir(new_folder)
                os.chdir(new_folder)
                _create_structre(v, new_folder, permission)

    if isinstance(yaml_data, list):
        for item in yaml_data:
            if isinstance(item, dict):
                _create_structre(item, dest, permission)




