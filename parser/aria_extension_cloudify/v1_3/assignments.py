#
# Copyright (c) 2016 GigaSpaces Technologies Ltd. All rights reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

from ..v1_0 import PropertyAssignment
from aria.parser import dsl_specification
from aria.parser.presentation import Presentation, has_fields, object_dict_field

@has_fields
@dsl_specification('node-templates-2', 'cloudify-1.3')
class CapabilityAssignment(Presentation):
    """
    The :code:`capabilities.scalable.properties` key is used for configuring the deployment characteristics of the node template.
    """

    @object_dict_field(PropertyAssignment)
    def properties(self):
        """
        :rtype: dict of str, :class:`PropertyAssignment`
        """
