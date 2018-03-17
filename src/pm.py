#! /usr/bin/env python

import argparse
import projman
import sys

default_project_location = projman.PROJECT_LOCATION

def get_args():
    pm_parser = argparse.ArgumentParser()
    pm_parser.add_argument('-t', '--type', metavar='type', help='Project type', required=False)
    pm_parser.add_argument('-p', '--path', metavar='path', help='Project creation path', required=False, default=default_project_location)

    sub_parser = pm_parser.add_subparsers()

    create_parser = sub_parser.add_parser('create', help='Manage Creation of projects')
    create_parser.add_argument('name', metavar='name', help='Project name')
    create_parser.set_defaults(func=projman.create_project)

    list_parser = sub_parser.add_parser('list', help='Manage listing of projects')
    list_parser.set_defaults(func=projman.list_projects)

    delete_parser = sub_parser.add_parser('delete', help='Delete project')
    delete_parser.add_argument('name', metavar='name', help='Project name to delete')
    delete_parser.set_defaults(func=projman.delete_projects)

    types_parser = sub_parser.add_parser('types', help='lists type of project you can create')
    types_parser.set_defaults(func=projman.show_types)

    describe_parser = sub_parser.add_parser('describe', help='Display folder structres of type of projects')
    describe_parser.set_defaults(func=projman.display_structre)

    args = pm_parser.parse_args()
    print args
    projman.get_project_location(args)
    args.func(args)

if __name__ == '__main__':
    # try:
    args = get_args()
    # except:
    #     sys.stderr.write('Error in command. Please refer to help of command.')
    #     sys.exit(4)


