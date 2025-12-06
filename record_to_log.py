# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from grammateus import Grammateus, Scribe

location = '/home/alxfed/Documents/Fairytales/one/'


def main():
    recorder = Grammateus(location)
    scribe = Scribe(recorder)
    scribe.records_to_log(format='twins')


if __name__ == "__main__":
    main()
    ...