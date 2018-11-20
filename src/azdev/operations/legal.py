# -----------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -----------------------------------------------------------------------------

import sys
import os

from azdev.utilities import (
    display, heading, subheading, get_cli_repo_path)

from knack.util import CLIError


LICENSE_HEADER = """# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
"""


def check_license_headers():

    heading('Verify License Headers')

    # TODO: The env could be somewhere else
    env_path = os.path.join(get_cli_repo_path(), 'env')

    files_without_header = []
    for current_dir, _, files in os.walk(get_cli_repo_path()):
        if current_dir.startswith(env_path):
            continue

        file_itr = (os.path.join(current_dir, p) for p in files if p.endswith('.py') and p != 'azure_bdist_wheel.py')
        for python_file in file_itr:
            with open(python_file, 'r') as f:
                file_text = f.read()

                if file_text and LICENSE_HEADER not in file_text:
                    files_without_header.append(os.path.join(current_dir, python_file))

    subheading('Results')
    if files_without_header:
        raise CLIError("{}\nError: {} files don't have the required license headers.".format('\n'.join(files_without_header), len(files_without_header)))
    display('License headers verified OK.')
