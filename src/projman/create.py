import os
import common

__all__ = ['create_project', 'create_dir_structre']
yaml_data = common.get_yaml_config()



def create_project(project_name, path=None):
    if path is None:
        path = common.get_project_location()

    new_project = os.path.join(path, project_name)
    if not os.path.exists(new_project):
        os.mkdir(new_project)
    return new_project


def create_dir_structre(type, project):
    """dict_to_dir expects yaml_dict to be a dictionary with one top-level key."""
    if os.path.exists(project):
        _create_structre(common.AVAILABLE_CONFIGS[type], project)

def _create_structre(yaml_data, dest, permission=None):
    try:
        if not permission:
            if yaml_data.get('permission'):
                current_permission = yaml_data['permission']

        if isinstance(yaml_data, dict):
            for k, v in yaml_data.items():
                if k == 'value' and isinstance(v, str):
                    if v.find('.') > 0:
                        file = open(os.path.join(dest, v), 'w')
                        os.chmod(file.name, 0444)
                        file.close()
                    else:
                        os.mkdir(os.path.join(dest, v), current_permission)
                elif k == "value" and not isinstance(v, str):
                    _create_structre(v, dest)
                elif k != 'value' and not isinstance(v, str):
                    os.mkdir(os.path.join(dest, k))
                    os.chdir(os.path.join(dest, k))
                    _create_structre(v, os.path.join(dest, k))

        if isinstance(yaml_data, list):
            for item in yaml_data:
                if isinstance(item, dict):
                    _create_structre(item, dest)
    except:
        pass




