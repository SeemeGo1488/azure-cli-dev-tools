# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from knack.config import CLIConfig

def get_azdev_config():
    return CLIConfig(config_dir=get_azdev_config_dir(), config_env_var_prefix='AZDEV')


def get_azure_config():
    return CLIConfig(config_dir=get_azure_config_dir(), config_env_var_prefix='AZURE')


def get_azdev_config_dir():
    """ Returns the user's .azdev directory. """
    return os.getenv('AZDEV_CONFIG_DIR', None) or os.path.expanduser(os.path.join('~', '.azdev'))


def get_azure_config_dir():
    """ Returns the user's Azure directory. """
    return os.getenv('AZURE_CONFIG_DIR', None) or os.path.expanduser(os.path.join('~', '.azure'))
