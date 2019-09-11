#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 NTT Communications Corporation

import sys

from st2common.runners.base_action import Action
class MyEchoMessage(Action):

    def read_message(self, message):
        result = {
            "bool": False,
            "message": message
        }
        if message == 'working':
            result.update({"bool": True})
        else:
            pass
        
        return result

    def run(self, max_try_cnts, message):
        results = []
        print(message)
        results.append(self.read_message(message))
        return results