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

from .proxy_only_resource_py3 import ProxyOnlyResource


class User(ProxyOnlyResource):
    """User credentials used for publishing activity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param publishing_user_name: Required. Username used for publishing.
    :type publishing_user_name: str
    :param publishing_password: Password used for publishing.
    :type publishing_password: str
    :param publishing_password_hash: Password hash used for publishing.
    :type publishing_password_hash: str
    :param publishing_password_hash_salt: Password hash salt used for
     publishing.
    :type publishing_password_hash_salt: str
    :param scm_uri: Url of SCM site.
    :type scm_uri: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'publishing_user_name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'publishing_user_name': {'key': 'properties.publishingUserName', 'type': 'str'},
        'publishing_password': {'key': 'properties.publishingPassword', 'type': 'str'},
        'publishing_password_hash': {'key': 'properties.publishingPasswordHash', 'type': 'str'},
        'publishing_password_hash_salt': {'key': 'properties.publishingPasswordHashSalt', 'type': 'str'},
        'scm_uri': {'key': 'properties.scmUri', 'type': 'str'},
    }

    def __init__(self, *, publishing_user_name: str, kind: str=None, publishing_password: str=None, publishing_password_hash: str=None, publishing_password_hash_salt: str=None, scm_uri: str=None, **kwargs) -> None:
        super(User, self).__init__(kind=kind, **kwargs)
        self.publishing_user_name = publishing_user_name
        self.publishing_password = publishing_password
        self.publishing_password_hash = publishing_password_hash
        self.publishing_password_hash_salt = publishing_password_hash_salt
        self.scm_uri = scm_uri
