# Copyright 2015 0xc0170
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
from os.path import exists

def argparse_filestring_type(string):
    if not exists(string):
        raise argparse.ArgumentTypeError("%s is not a file." % string)
    else:
        return string

def argparse_string_type(case_converter, prefer_hyphen=False):
    if prefer_hyphen:
        return lambda string: case_converter(string).replace("_","-")
    else:
        return lambda string: case_converter(string).replace("-","_")

def split_options(opts):
    options = {}
    if opts is None:
        return options
    for o in opts:
        r = o.split('=', 1)
        options[r[0]] = None if len(r) == 1 else r[1]
    return options
