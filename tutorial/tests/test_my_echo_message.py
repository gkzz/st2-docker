#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 NTT Communications Corporation
from st2tests.base import BaseActionTestCase
from mock import MagicMock, patch
import json
import yaml
import os
import sys
sys.path.append('/opt/stackstorm/packs/ecl2_auto_dep/actions/scripts')
sys.path.append('/opt/stackstorm/virtualenvs/ecl2_auto_dep/lib/python2.7/site-packages')
sys.path.append('/opt/stackstorm/st2/lib/python2.7/site-packages')

BASE_DIR = "/home/gakuji.tamaki/work_tamaki/st2-sample/stackstrom/packs/examples"
sys.path.append(BASE_DIR)

input_file = "default_input.yml"

from my_echo_message import(
    MyEchoMessage
)

class TestMyEchoMessage(BaseActionTestCase):
    action_cls = MyEchoMessage

    def test00_no_mock_st2(self):
        input = yaml.load(self.get_fixture_content(input_file))
        input.update({
            "message" : "working",
        })

        action = self.get_action_instance()
        results = action.run(**input)

        print('results: {}'.format(results))

        self.assertEquals(len(results), 1)
        self.assertEqual(results[0]["bool"], True) 
        self.assertEqual(results[0]["message"], input["message"])