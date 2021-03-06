# file functions
# -*- coding: utf-8 -*-

from __future__ import print_function, division
import os as _os

__all__ = ['create_project_folder',
           'create_gitignore',
           'nb_stripout_filter',
           'session_info',
           'project_directory']


def create_project_folder(project_name, path=None, gitignore=True):
    """ Create a new project folder in the current working directory containing
    all subfolders.

    Args:
        project_name (string):
            the name for the project.
        path (string, optional):
            an optional path name for the directory containing the project.
            If not provided, project folder will be created in the current
            working directory.
        gitignore (boolean, defaults True):
            if True, create a .gitignore file with common options of files to
            ignore for the git version control system.

    Example:
        Make a directory for the project "awesome-science" in /home/usr/::
        create_project_folder('awesome-science', path='/home/usr/')

    """

    if path is None:
        root_dir = _os.getcwd()
    else:
        root_dir = path

    # check if project directory exists, create it (taken from
    # https://stackoverflow.com/questions/273192/
    # check-if-a-directory-exists-and-create-it-if-necessary)
    def ensure_dir(d):
        if not _os.path.exists(d):
            _os.makedirs(d)

    top_dir = _os.path.join(root_dir, project_name)
    ensure_dir(top_dir)

    # code subdirectories:
    ensure_dir(_os.path.join(top_dir, 'code', 'analysis'))
    ensure_dir(_os.path.join(top_dir, 'code', 'experiment'))
    ensure_dir(_os.path.join(top_dir, 'code', 'stimuli'))
    ensure_dir(_os.path.join(top_dir, 'code', 'unit-tests'))

    # other subdirectories:
    ensure_dir(_os.path.join(top_dir, 'documentation'))
    ensure_dir(_os.path.join(top_dir, 'figures'))
    ensure_dir(_os.path.join(top_dir, 'notebooks'))
    ensure_dir(_os.path.join(top_dir, 'publications'))
    ensure_dir(_os.path.join(top_dir, 'raw-data'))
    ensure_dir(_os.path.join(top_dir, 'results'))
    ensure_dir(_os.path.join(top_dir, 'stimuli'))

    if gitignore is True:
        create_gitignore(top_dir)


def create_gitignore(path=None):
    """Creates a `.gitignore` file with common options in the current working
    directory, or in `path`.

    Args:
    path (string, optional):
        an optional path name for the directory to place the file.
        If not provided, .gitignore will be created in the current
        working directory.

    Example:
        Make a .gitignore in /home/usr/::
        create_gitignore(path='/home/usr/')

    """

    if path is None:
        root_dir = _os.getcwd()
    else:
        root_dir = path

    fname = _os.path.join(root_dir, '.gitignore')

    f = open(fname, mode='x')

    f.write('.gitignore \n'
            '.Rhistory \n'
            '.Rproj* \n'
            '*.Rproj \n'
            '.DS_Store* \n'
            '*.odt \n'
            '*.aux \n'
            '*.log \n'
            '*.out \n'
            '*.gz \n'
            '*.sublime-project \n'
            '*.sublime-workspace \n'
            '*.pyc \n'
            '*.pdf \n'
            '*.png \n'
            '*.svg \n'
            '*.jpg \n'
            '*.jpeg \n'
            '*.doc \n'
            '*.docx\n'
            '*.m~\n'
            '.Rproj.user/*\n'
            '*.Rproj\n'
            '*.RData\n'
            '*.rdb\n'
            '*.rdx\n'
            '*__packages')
    f.close()


def nb_stripout_filter(path_to_nbstripout, path=None):
    """Call this function on a directory containing a .git repository in order
    to add a git filter that strips the output of an ipython notebook before
    committing.

    Adapted from https://gist.github.com/minrk/6176788

    Args:
        path_to_nbstripout (string):
            the absolute path to the nbstripout.py file on your system.
            See below for file contents.
        path (string, optional):
            an optional path name for the directory containing the hidden .git
            directory. If not provided, the current working directory is used.

    Example:
        Add filter to '/home/usr/my_repo/' from a file nbstripout.py
        stored in /usr/local/bin/::
        nb_stripout_filter('~/local/bin',
                           '/home/usr/my_repo/')


    Copy the following into a file nbstripout.py and put it somewhere on your
    system, outside the repository.  Adapted from
    https://gist.github.com/minrk/6176788 to work with git filter driver.

    Original function is from
    https://github.com/cfriedline/ipynb_template/blob/master/nbstripout


    nbstripout.py
    --------------

    #!/usr/bin/env python
    import sys

    from IPython.nbformat import current


    def strip_output(nb):
        for cell in nb.worksheets[0].cells:
            if 'outputs' in cell:
                cell['outputs'] = []
            if 'prompt_number' in cell:
                cell['prompt_number'] = ""
        return nb

    if __name__ == '__main__':
        nb = current.read(sys.stdin, 'json')
        nb = strip_output(nb)
        current.write(nb, sys.stdout, 'json')

    --------------
    end copy file.

    """

    if path is None:
        root_dir = _os.getcwd()
    else:
        root_dir = path

    git_dir = _os.path.join(root_dir, '.git')
    conf = _os.path.join(git_dir, 'config')
    attributes = _os.path.join(root_dir, '.gitattributes')

    nb_stripout_path = _os.path.join(path_to_nbstripout,
                                     'nbstripout.py')

    # open .git config in append mode:
    f = open(conf, mode='a')
    f.write('[filter "stripoutput"] \n'
            '    clean = "' + nb_stripout_path +
            '" ')
    f.close

    # create .gitattributes file:
    f = open(attributes, mode='a')
    f.write('*.ipynb filter=stripoutput')
    f.close

    # ignore the .gitattributes file:
    f = open(_os.path.join(root_dir, '.gitignore'), mode='a')
    f.write('.gitattributes \n')
    f.close


def session_info():
    """ Print an output file containing python versions, system
    information and installed packages. This function is to facilitate
    reproducible research using python.

    Example:
        You're running a script called `generate_my_awesome_stimuli.py`.
        Somewhere in the script, write::

            import psyutils as pu
            pu.files.session_info()


        When the script is called from the command line, like this::

            python generate_my_awesome_stimuli.py


        A text file called `generate_my_awesome_stimuli.py_log.txt`
        will be created (or appended, if it exists) in the current working
        directory.
    """

    import sys
    import subprocess
    from datetime import datetime

    root_dir = _os.getcwd()
    calling_script = sys.argv[0]
    fname = _os.path.join(root_dir, (calling_script + '_log.txt'))

    def horz_line(info):
        """Include a horizontal line with spaces"""
        info += ('\n------------------------------------------------------\n' +
                 '------------------------------------------------------\n')
        return(info)

    info = ''

    info += '\n\nScript: ' + calling_script + '\n\n'
    info += 'Called on: ' + str(datetime.now()) + '\n\n'

    info += 'OS: ' + sys.platform + '\n'
    info += 'Python version: ' + sys.version + '\n'

    info += '\n\nAvailable packages via pip:\n'

    # all packages and their versions from the current python env:
    info += subprocess.check_output('pip freeze', shell=True,
                                    universal_newlines=True)

    info += '\n\n (note, not all these packages are loaded by script).'
    info = horz_line(info)

    f = open(fname, mode='a')
    f.write(info)
    f.close


def project_directory(target_dir):
    """Returns the full path of the top level directory for this project,
    assuming that this function is being called from somewhere in the project
    (i.e., from a subdirectory of the target directory).

    Args:
        target_dir: a string containing the target directory name.
    Returns:
        the full path to the target directory.

    """

    orig_dir = _os.getcwd()
    parent = _os.path.split(orig_dir)[0]

    try:
        # go up directories, searching for target:
        while parent[-len(target_dir):] != target_dir:
            _os.chdir('..')
            parent = _os.path.split(_os.getcwd())[0]

        top_path = parent
        # set working directory back to original:
        _os.chdir(orig_dir)
    except:
        _os.chdir(orig_dir)
    return(top_path)

