# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import re
from azure.cli.core.azclierror import InvalidArgumentValueError


# Parameter-Level Validation
def validate_configuration_type(configuration_type):
    if configuration_type.lower() != 'sourcecontrolconfiguration':
        raise InvalidArgumentValueError(
            'Invalid configuration-type',
            'Try specifying the valid value "sourceControlConfiguration"')


def validate_operator_namespace(namespace):
    if namespace.operator_namespace:
        __validate_k8s_name(namespace.operator_namespace, "--operator-namespace", 23)


def validate_operator_instance_name(namespace):
    if namespace.operator_instance_name:
        __validate_k8s_name(namespace.operator_instance_name, "--operator-instance-name", 23)


# Create Parameter Validation
def validate_configuration_name(configuration_name):
    __validate_k8s_name(configuration_name, "--name", 63)


# Helper
def __validate_k8s_name(param_value, param_name, max_len):
    if len(param_value) > max_len:
        raise InvalidArgumentValueError(
            'Error! Invalid {0}'.format(param_name),
            'Parameter {0} can be a maximum of {1} characters'.format(param_name, max_len))
    if not re.match(r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$', param_value):
        if param_value[0] == "-" or param_value[-1] == "-":
            raise InvalidArgumentValueError(
                'Error! Invalid {0}'.format(param_name),
                'Parameter {0} cannot begin or end with a hyphen'.format(param_name))
        raise InvalidArgumentValueError(
            'Error! Invalid {0}'.format(param_name),
            'Parameter {0} can only contain lowercase alphanumeric characters and hyphens'.format(param_name))
