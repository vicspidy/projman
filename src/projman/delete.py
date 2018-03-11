import os
import shutil

import common

__all__ = ['delete_projects']

def delete_projects(type=None):
    for project in os.listdir(common.PROJECT_LOCATION):
        current_project = os.path.join(common.PROJECT_LOCATION, project)
        if os.path.isdir(current_project):
            if type:
                if type in common.AVAILABLE_TYPES:
                    if os.path.exists(os.path.join(current_project, type)):
                        shutil.rmtree(current_project)
            else:
                shutil.rmtree(current_project)