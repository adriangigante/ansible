#!/usr/bin/env python
import argparse
import os
import sys

try:
        import json
except ImportError:
        import simplejson as json

class CustomInventory():
        def __init__(self):
                self.inventory = {}
                self.read_cli_args()

                if self.args.list:
                        self.inventory = self.our_inventory()
                else:
                        self.inventory = self.empty_inventory()
                print json.dumps(self.inventory)
        def empty_inventory(self):
                return {"_meta":{"hostvars":{}}}

        def our_inventory(self):
                return {
                        "group" : {
                                "hosts":['localhost'],
                                "vars":{ "ansible_connection":"local"}
                        },
                        "_meta":{
                                "hostvars": {"foo":"bar"}
                        }
                }
        def read_cli_args(self):
                parser = argparse.ArgumentParser()
                parser.add_argument('--list', action="store_true")
                self.args = parser.parse_args()
CustomInventory()
