#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 NTT Communications Corporation
from st2tests.base import BaseActionTestCase
from mock import MagicMock, patch
import json
import yaml
import os
import sys
import re
sys.path.append('/opt/stackstorm/packs/ecl2_auto_dep/actions/scripts')
sys.path.append('/opt/stackstorm/virtualenvs/ecl2_auto_dep/lib/python2.7/site-packages')
sys.path.append('/opt/stackstorm/st2/lib/python2.7/site-packages')

BASE_DIR = "/home/gakuji.tamaki/work_tamaki/st2-sample/stackstrom/packs/examples"
sys.path.append(BASE_DIR)

input_file = "default_input.yml"

from get_current_datetime import(
   GetCurrentDatetime
)

class TestGetCurrentDatetime(BaseActionTestCase):
    action_cls = GetCurrentDatetime

    #def test00_no_mock_st2(self):
    #    input = yaml.load(self.get_fixture_content(input_file))
    #    input.update({
    #        "expected_hour": 20,
    #    })
#
    #    action = self.get_action_instance()
    #    results = action.run(**input)
#
    #    print('results: {}'.format(results))
#
    #    self.assertEquals(len(results), 1)
    #    self.assertEqual(results[0]["bool"], True)
    #    ptn = re.compile(
    #        #                             4               
    #        # '    09    /  02   / 2019 - 15    :  29   :39'
    #        r'\s*(\d{2})/(\d{2})/(\d{4})-(\d{2}):(\d{2}):(\d{2})\s*'
    #    ) 
    #    self.assertEqual(
    #        int(ptn.search(results[0]["datetime"]).group(4)), 
    #        int(input["expected_hour"])
    #    )
    
    @patch("get_current_datetime.GetCurrentDatetime.get_datetime")
    def test00_mock_st2(self, get):
        input = yaml.load(self.get_fixture_content(input_file))
        input.update({
            "expected_hour": 20,
        })

        def _get_datetime():
            _datetime = "09/02/2019-20:29:39"
            ptn = re.compile(
                #                               2          
                #        09 /  02   / 2019   - 20   :  29   :39
                r'\s*(\d{2})/(\d{2})/(\d{4})-(\d{2}):(\d{2}):(\d{2})\s*'
            ) 
            _hour = int(ptn.search(_datetime).group(4))

            return _datetime, _hour

        get.side_effect = _get_datetime

        action = self.get_action_instance()
        results = action.run(**input)

        print('results: {}'.format(results))

        self.assertEquals(len(results), 1)
        self.assertEqual(results[0]["bool"], True)
        ptn = re.compile(
            #                             4               
            # '    09    /  02   / 2019 - 20    :  29   :39'
            r'\s*(\d{2})/(\d{2})/(\d{4})-(\d{2}):(\d{2}):(\d{2})\s*'
        ) 
        self.assertEqual(
            int(ptn.search(results[0]["datetime"]).group(4)), 
            int(input["expected_hour"])
        )