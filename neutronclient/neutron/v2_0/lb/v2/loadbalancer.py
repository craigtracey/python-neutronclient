# Copyright 2014 Blue Box Group, Inc.
# All Rights Reserved
#
# Author: Craig Tracey <craigtracey@gmail.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

import logging

from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.openstack.common.gettextutils import _


class ListLoadBalancer(neutronV20.ListCommand):
    """List loadbalancers that belong to a given tenant."""

    resource = 'loadbalancer'
    log = logging.getLogger(__name__ + '.ListLoadBalancer')
    list_columns = ['id', 'name', 'vip_subnet_id',
                    'admin_state_up', 'status']
    pagination_support = True
    sorting_support = True


class ShowLoadBalancer(neutronV20.ShowCommand):
    """Show information of a given loadbalancer."""

    resource = 'loadbalancer'
    log = logging.getLogger(__name__ + '.ShowLoadBalancer')


class CreateLoadBalancer(neutronV20.CreateCommand):
    """Create a loadbalancer."""

    resource = 'loadbalancer'
    log = logging.getLogger(__name__ + '.CreateLoadBalancer')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--description',
            help=_('Description of the load balancer'))
        parser.add_argument(
            '--admin-state-down',
            dest='admin_state', action='store_false',
            help=_('Set admin state up to false'))
        parser.add_argument(
            'name', metavar='NAME',
            help=_('Name of the load balancer'))
        parser.add_argument(
            'vip_subnet_id', metavar='VIP_SUBNET_ID',
            help=_('ID of the load balancer subnet'))

    def args2body(self, parsed_args):
        body = {
            self.resource: {
                'name': parsed_args.name,
                'vip_subnet_id': parsed_args.vip_subnet_id,
                'admin_state_up': parsed_args.admin_state,
            },
        }
        neutronV20.update_dict(parsed_args, body[self.resource],
                               ['description'])
        return body


class UpdateLoadBalancer(neutronV20.UpdateCommand):
    """Update a given loadbalancer."""

    resource = 'loadbalancer'
    log = logging.getLogger(__name__ + '.UpdateLoadBalancer')
    allow_names = False


class DeleteLoadBalancer(neutronV20.DeleteCommand):
    """Delete a given loadbalancer."""

    resource = 'loadbalancer'
    log = logging.getLogger(__name__ + '.DeleteLoadBalancer')
