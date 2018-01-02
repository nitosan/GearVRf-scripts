import argparse
import os
import ut


def test_demos(path):
    if os.path.isabs(path):
        work_path = path
    else:
        curr_path = ut.get_curr_path()
        work_path = os.path.join(curr_path, path)


def main_logic():
    parser = argparse.ArgumentParser(description='Test all the demos of GVRF')
    parser.add_argument('path', help="Where are the projects")

    args = parser.parse_args()

    test_demos(args.path)


if __name__ == '__main__':
    main_logic()