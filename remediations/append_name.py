#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import sys
import json
import logging
import argparse


LOGFILE = '/tmp/names.log'

def append(name, surname):
    with open(LOGFILE, 'a+') as f:
        f.write(f'Name: {name}, Surname: {surname}\n')

    result= {
        "success":True,
        "passed": True,
        "result": f'Appended values {name}, {surname} to {LOGFILE}'
    }
    print(json.dumps(result))

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some arguments.')
    parser.add_argument('--name', type=str, help="Name of the hero")
    parser.add_argument('--surname', type=str, help="Surname of the hero")

    args = parser.parse_args()
    logging.warning("Got arguments: %s", args)
    append(args.name, args.surname)
