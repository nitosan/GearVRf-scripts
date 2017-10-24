import argparse
import fnmatch
import os
import re

import ut


def upgrade_gvrf_projects(proj_path, target_version, is_modify_file):
    curr_path = ut.get_curr_path()
    curr_path = os.path.join(curr_path, proj_path)
    for base_dir, dirs, files in os.walk(curr_path):

        for f in fnmatch.filter(files, "*"):
            ext = os.path.splitext(f)[1]
            if ext == '.gradle':
                file_path = os.path.join(base_dir, f)
                gradle_file = open(file_path, "r")
                file_content = gradle_file.read()
                gradle_file.close()

                regex = r"ext\.gearvrfVersion='(.*)'"

                version_search = re.search(regex, file_content)

                if version_search:
                    version_number = version_search.group(1)
                    if version_number != target_version:
                        if is_modify_file:
                            new_file_content = re.sub(regex, 'ext.gearvrfVersion=\'' + target_version + '\'', file_content)
                            w_file = open(file_path, "w")
                            w_file.write(new_file_content)
                            w_file.close()
                            print file_path
                            print version_number
                            print "File updated"
                        else:
                            print file_path
                            print version_number
                            print 'Need update'
                            print ""


def main_logic():

    parser = argparse.ArgumentParser(description='Update GVRF version for Android Studio projects.')
    parser.add_argument('path', help="Where are the projects")
    parser.add_argument('-v', '--version', help='GVRF version eg: 4.0.1-SNAPSHOT')
    parser.add_argument('-u', '--update', help='Modify the version to the specified version',
                        default=False, action='store_true')

    args = parser.parse_args()

    upgrade_gvrf_projects(args.path, args.version, args.update)


if __name__ == '__main__':
    main_logic()
