import os
import common

__all__ = ['list_projects']

def list_projects(args):
    if args.type:
        if args.type not in common.AVAILABLE_TYPES:
            print 'Invalid type of project given: {0}'.format(args.type)
            return
    for project in os.listdir(common.PROJECT_LOCATION):
        current_project = os.path.join(common.PROJECT_LOCATION, project)
        if os.path.isdir(current_project):
            if args.type:
                if os.path.exists(os.path.join(current_project, args.type)):
                    print project
            else:
                print project