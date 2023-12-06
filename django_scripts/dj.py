#!/usr/bin/env python

# Copyright (C) Raffaele Salmaso <raffaele@salmaso.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
from os.path import dirname
import sys

import readenv.loads  # noqa: F401
from stua.commands import BaseCommand
from stua.os import system


COMMAND = os.environ.get("DJANGO_COMMAND", "manage.py")
PYTHON = os.environ.get("PYTHON", "python3")


class Command(BaseCommand):
    def find_manage_py(self, path=None):
        path = path or os.getcwd()

        while path != "/":
            manage = os.path.join(path, COMMAND)
            if os.path.exists(manage):
                return path
            path = dirname(path)
        return False

    def build_cmd(self, args):
        cmd = []

        try:
            cmd.append(PYTHON)
        except:
            pass
        cmd.append(f"./{COMMAND}")

        if len(args) > 0:
            if args[0] == "test":
                # test are always verbose if not tell otherwise
                verbosity = [True for arg in args if arg.startswith("--verbosity")]
                if not verbosity:
                    args.append("--verbosity=2")
        cmd.extend(args)

        return cmd

    def handle(self, command, args):
        path = self.find_manage_py()

        status = 0
        if path:
            os.chdir(path)
            cmd = self.build_cmd(args)
            status = system(cmd, env=os.environ).returncode
        return status


def main():
    dj = Command()
    status = dj.run(sys.argv)
    sys.exit(status)


def _check_command(module):
    sh = system(
        [
            PYTHON,
            "-c",
            f"import importlib.util; import sys; sys.exit(not bool(importlib.util.find_spec('{module}')))",
        ],
        env=os.environ,
        capture_output=True,
    )
    return sh.returncode
def main_shell():
    dj = Command()
    has_command = _check_command("django_extensions.management.commands.shell_plus")
    sys.argv.insert(1, "shell" if has_command else "shell_plus")
    status = dj.run(sys.argv)
    sys.exit(status)


def main_runserver():
    dj = Command()
    has_command = _check_command("django_extensions.management.commands.runserver_plus")
    sys.argv.insert(1, "runserver" if has_command else "runserver_plus")
    status = dj.run(sys.argv)
    sys.exit(status)
