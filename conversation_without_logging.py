# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from yaml import safe_load as yl
from grammateus import Grammateus
from castor_pollux import rest as cp


def main():
    kwargs = """  # this is a string in YAML format
      model:        gemini-2.0-pro-exp-02-05 # gemini-2.5-flash-preview-05-20 # gemini-2.5-flash-preview-04-17 # gemini-2.5-pro-preview-05-06 
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

    instruction = 'You are Joseph Jacobs. You retell folk tales'

    text_to_continue = 'Once upon a time when pigs drank wine'

    machine_text = cp.continuation(
        text=text_to_continue,
        instruction=instruction,
        **yl(kwargs)
    )

    return machine_text


if __name__ == "__main__":
    result = main()
    ...
