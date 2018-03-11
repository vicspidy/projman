import argparse
import projman
import time

# create -p D:\ashish\Hackathon\projman\projects

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", help='Type of the project')
    parser.add_argument("-p", "--path", help='Where to create the new projects')
    # parser.add_argument("create", action='store_true')
    # parser.add_argument("name", help='Name of new project')
    # parser.add_argument("list", help='Lists all projects')
    # parser.add_argument("-t", "--type", help='Lists all projects')
    args = parser.parse_args()
    print args
    return args

if __name__ == '__main__':
    for i in projman.get_yaml_config():
        for k, v in i.iteritems():
            print k, v
    new_project = projman.create_project('The Dark Knight')
    # projman.create_dir_structre('houdini', new_project)
    projman.create_dir_structre('maya', new_project)

    projman.list_projects('houdini')


    # args = get_args()
    # if args.type:
    #     if args.create:
    #         if args.path:
    #             new_project = projman.create_project(args.name, args.path)
    #         else:
    #             new_project = projman.create_project(args.name)