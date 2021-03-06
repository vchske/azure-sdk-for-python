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


class AbnormalTimePeriod(Model):
    """Class representing Abnormal Time Period identified in diagnosis.

    :param start_time: Start time of the downtime
    :type start_time: datetime
    :param end_time: End time of the downtime
    :type end_time: datetime
    :param events: List of Possible Cause of downtime
    :type events: list[~azure.mgmt.web.models.DetectorAbnormalTimePeriod]
    :param solutions: List of proposed solutions
    :type solutions: list[~azure.mgmt.web.models.Solution]
    """

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'events': {'key': 'events', 'type': '[DetectorAbnormalTimePeriod]'},
        'solutions': {'key': 'solutions', 'type': '[Solution]'},
    }

    def __init__(self, **kwargs):
        super(AbnormalTimePeriod, self).__init__(**kwargs)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.events = kwargs.get('events', None)
        self.solutions = kwargs.get('solutions', None)
