import os
import common

__all__ = ['list_projects']

def list_projects(type=None):
    for project in os.listdir(common.PROJECT_LOCATION):
        current_project = os.path.join(common.PROJECT_LOCATION, project)
        if os.path.isdir(current_project):
            if type:
                if type in common.AVAILABLE_TYPES:
                    if os.path.exists(os.path.join(current_project, type)):
                        print project
            else:
                print project