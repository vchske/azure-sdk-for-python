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


class EntityHierarchyItem(Model):
    """The management group details for the hierarchy view.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified ID for the management group.  For example,
     /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
    :vartype id: str
    :ivar type: The type of the resource.  For example,
     /providers/Microsoft.Management/managementGroups
    :vartype type: str
    :ivar name: The name of the management group. For example,
     00000000-0000-0000-0000-000000000000
    :vartype name: str
    :param display_name: The friendly name of the management group.
    :type display_name: str
    :param permissions: Permissions. Possible values include: 'noaccess',
     'view', 'edit', 'delete'
    :type permissions: str or ~azure.mgmt.managementgroups.models.enum
    :param children: The list of children.
    :type children:
     list[~azure.mgmt.managementgroups.models.EntityHierarchyItem]
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'permissions': {'key': 'properties.permissions', 'type': 'str'},
        'children': {'key': 'properties.children', 'type': '[EntityHierarchyItem]'},
    }

    def __init__(self, *, display_name: str=None, permissions=None, children=None, **kwargs) -> None:
        super(EntityHierarchyItem, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.display_name = display_name
        self.permissions = permissions
        self.children = children
