import os
import shutil

import common

__all__ = ['delete_projects']

def delete_projects(args):
    current_project = os.path.join(common.PROJECT_LOCATION, args.name)
    if os.path.isdir(current_project):
        if args.type:
            if args.type in common.AVAILABLE_TYPES:
                current_project = os.path.join(current_project, args.type)
                if os.path.exists(current_project):
                    if os.path.exists(current_project):
                        shutil.rmtree(current_project)
                else:
                    print 'No project found of type: {0}'.format(args.type)
            else:
                print 'Invalid type of project given to delete: {0}'.format(args.type)
        else:
            print 'delete project', current_project
            if os.path.exists(current_project):
                shutil.rmtree(current_project)
            else:
                print 'No such project found: {0}'.format(args.name)
    else:
        print 'No such project found: {0}'.format(args.name)