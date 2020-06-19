#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# pylint: skip-file

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the junos_l2_interfaces module
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type


class L2_interfacesArgs(object):
    """The arg spec for the junos_l2_interfaces module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "access": {
                    "type": "dict",
                    "options": {"vlan": {"type": "str"}},
                },
                "name": {"required": True, "type": "str"},
                "trunk": {
                    "type": "dict",
                    "options": {
                        "allowed_vlans": {"type": "list"},
                        "native_vlan": {"type": "str"},
                    },
                },
                "unit": {"type": "int"},
                "enhanced_layer": {"type": "bool"},
            },
            "type": "list",
        },
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
            ],
            "default": "merged",
            "type": "str",
        },
    }
