import os
import sys


def main():
    cmd = (
        sys.executable, '-m', 'gitlint.cli',
        '--config', os.path.join(os.path.dirname(__file__), 'conf.ini'),
        *sys.argv[1:],
    )
    os.execvp(cmd[0], cmd)