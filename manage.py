#!/usr/bin/env python
import os
import site
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

# Add vendor so we can import 3rd-party libs.
site.addsitedir(ROOT)
site.addsitedir(path('vendor'))

import argparse

import log_settings
import glow
import po2js


def shell():
    try:
        import IPython
        IPython.Shell.IPShell(argv=[], user_ns={'g': glow}).mainloop()
    except ImportError:
        import code
        code.interact()


COMMANDS = {
    'shell': shell,
    'glow': glow.main,
    'cleanup': glow.cleanup,
    'po': po2js.main,
}


parser = argparse.ArgumentParser()
parser.add_argument('command', choices=sorted(COMMANDS),
                    help='what should I do?')


if __name__ == '__main__':
    args = parser.parse_args(sys.argv[1:2])
    try:
        COMMANDS[args.command](*sys.argv[2:])
    except KeyboardInterrupt:
        raise
        pass  # Die quietly.
