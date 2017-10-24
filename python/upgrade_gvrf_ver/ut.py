import glob
import os
import shutil


def get_curr_path():
    return os.path.dirname(os.path.realpath(__file__))


def which(program):
    def is_exe(cmd_path):
        return os.path.exists(cmd_path) and os.access(cmd_path, os.X_OK)

    def ext_candidates(cmd_path):
        yield cmd_path
        for ext in os.environ.get("PATHEXT", "").split(os.pathsep):
            yield cmd_path + ext

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            for candidate in ext_candidates(exe_file):
                if is_exe(candidate):
                    return candidate

    return None


def copy_all(src, dst):
    for filename in glob.glob(os.path.join(src, '*.*')):
        shutil.copy(filename, dst)


def copy_tree(src, dst):
    if os.path.isdir(src):
        shutil.copytree(src, dst)
    elif os.path.exists(src):
        shutil.copy(src, dst)


def del_tree(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.isfile(path):
        os.remove(path)
    else:
        print 'Invalid path: ' + path
