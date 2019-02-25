#!/usr/bin/env python
# coding: utf-8

import os.path
import log2seq

import message
l_messages = message.messages

if __name__ == "__main__":
    rules = log2seq.load_from_script(
        os.path.abspath("../log2seq/default_script.py"))
    p = log2seq.LogParser(rules)

    for mes in l_messages:
        print(mes)
        d = p.process_line(mes)
        print("-> {0} {1} {2}".format(d["timestamp"], d["host"], d["words"]))

