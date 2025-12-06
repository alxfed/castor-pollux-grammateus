# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from yaml import safe_load as yl
from grammateus import Grammateus
from castor_pollux import rest as cp

location = '/home/alxfed/Documents/Fairytales/one/'


def main():
    recorder = Grammateus(location)
    kwargs = """  # this is a string in YAML format
      model:        gemini-2.5-flash-preview-04-17 # 'gemini-2.5-pro-preview-05-06'
      mime_type:    text/plain
      modalities:
        - TEXT
      max_tokens:   32000
      n: 1
      stop_sequences:
        - STOP
        - "\nTitle"
      temperature:  0.5
      top_k:        10
      top_p:        0.5
      thinking:     24576  # thinking tokens budget. 24576
    """

    instruction = 'I am Joseph Jacobs. I retell folk tales'

    text_to_continue = 'And what happened next?'

    machine_text = cp.continuation(
        text=text_to_continue,
        instruction=instruction,
        recorder=recorder,
        **yl(kwargs)
    )

    return machine_text


if __name__ == "__main__":
    result = main()
    ...
