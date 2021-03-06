# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ImportLabVirtualMachineRequest(Model):
    """This represents the payload required to import a virtual machine from a
    different lab into the current one.

    :param source_virtual_machine_resource_id: The full resource ID of the
     virtual machine to be imported.
    :type source_virtual_machine_resource_id: str
    :param destination_virtual_machine_name: The name of the virtual machine
     in the destination lab
    :type destination_virtual_machine_name: str
    """

    _attribute_map = {
        'source_virtual_machine_resource_id': {'key': 'sourceVirtualMachineResourceId', 'type': 'str'},
        'destination_virtual_machine_name': {'key': 'destinationVirtualMachineName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImportLabVirtualMachineRequest, self).__init__(**kwargs)
        self.source_virtual_machine_resource_id = kwargs.get('source_virtual_machine_resource_id', None)
        self.destination_virtual_machine_name = kwargs.get('destination_virtual_machine_name', None)
