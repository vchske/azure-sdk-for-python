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


class CreateLinkedIntegrationRuntimeRequest(Model):
    """The linked integration runtime information.

    :param name: The name of the linked integration runtime.
    :type name: str
    :param subscription_id: The ID of the subscription that the linked
     integration runtime belongs to.
    :type subscription_id: str
    :param data_factory_name: The name of the data factory that the linked
     integration runtime belongs to.
    :type data_factory_name: str
    :param data_factory_location: The location of the data factory that the
     linked integration runtime belongs to.
    :type data_factory_location: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'data_factory_name': {'key': 'dataFactoryName', 'type': 'str'},
        'data_factory_location': {'key': 'dataFactoryLocation', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CreateLinkedIntegrationRuntimeRequest, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.subscription_id = kwargs.get('subscription_id', None)
        self.data_factory_name = kwargs.get('data_factory_name', None)
        self.data_factory_location = kwargs.get('data_factory_location', None)
