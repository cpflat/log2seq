# coding: utf-8

import unittest

import log2seq


class TestParser(unittest.TestCase):

    def test_readme(self):
        mes = ("Jan  1 12:34:56 host-device1 system[12345]: "
               "host 2001:0db8:1234::1 (interface:eth0) disconnected")
        parser = log2seq.init_parser()
        d = parser.process_line(mes)
        assert d["words"] == ['system', '12345', 'host', '2001:0db8:1234::1',
                              'interface', 'eth0', 'disconnected']
