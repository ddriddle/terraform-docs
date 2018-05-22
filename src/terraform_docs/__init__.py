from __future__ import print_function
from builtins import str

import os
import sys

from glob import iglob

import hcl

def open_tf_files():  # type: () -> Dict
    code = ""
    
    for tf in iglob('*.tf'):
        with open(tf, 'r') as fp:
            code += fp.read()

    return hcl.loads(code)


def error(code, mesg):  # type: (int, str) -> None
    print(str(mesg), file=sys.stderr)
    exit(code)

VAR = "[%s]() - %s."
OPT = "[%s]() - (Optional) %s."

def main():  # type: () -> None
    hcl = open_tf_files()

    for var, data in hcl['variable'].items():
        desc = data.get('description', None)
        vtype = data.get('type', 'string')

        if desc is not None:
            default = data.get('default', None)

            if default is not None:
                print(VAR % (var, desc))
            else:
                print(OPT % (var, desc))

    exit(0)
