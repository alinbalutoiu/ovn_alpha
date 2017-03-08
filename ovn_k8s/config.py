# Copyright 2017 Cloudbase Solutions Srl
# All Rights Reserved.
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

import ast
import ConfigParser


config = ConfigParser.RawConfigParser()
config_filename = 'ovn_k8s.conf'
config_read = config.read(config_filename)
if len(config_read) != 1:
    # config.read returns the list of filenames which were successfully parsed.
    # if we reach here it means the config could not be read
    raise Exception("Error when reading config file: %s" % config_filename)


def get_option(option_name, section_name='default'):
    # Raises ConfigParser.NoOptionError exception if the option_name could
    # not be found.
    config_string = config.get(section_name, option_name)
    try:
        # Try to evaluate the string which may contain a Python expression
        expr = ast.literal_eval(config_string)
        return expr
    except Exception:
        return config_string
