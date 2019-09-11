#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2018 NTT Communications Corporation

import sys
from datetime import datetime

from st2common.runners.base_action import Action
class GetCurrentDatetime(Action):
    def get_datetime(self):
        current_datetime = datetime.now()
        current_hour = int(current_datetime.strftime("%H"))
        current_datetime = current_datetime.strftime("%m/%d/%Y-%H:%M:%S")
        return current_datetime, current_hour


    def check_datetime(self, current_datetime, current_hour, expected_hour):
        result = {
            "bool": False,
            "datetime": current_datetime
        }
        if current_hour == expected_hour:
            result.update({
                "bool": True,
            })
        else:
            pass
        
        return result

    def run(self, max_try_cnts, expected_hour):
        results = []
        current_datetime = None
        cnts = 0
        import pdb; pdb.set_trace()

        while cnts < max_try_cnts:
            current_datetime, current_hour = self.get_datetime()
            result = self.check_datetime(current_datetime, current_hour, expected_hour)
            if result["bool"]:
                break
            else:
                cnts += 1
                continue
            
        results.append(result)
        return results