#! /usr/bin/env python
"""
    File name: utils.py
    Author: Dimitar Petrov
    Date created: 2018/05/25
    Python Version: 3.6
    Description: Common functions
"""

import os
import sys
import logging.config
import yaml


def setup_logging(default_path='./logconf/logging.yml',
                  default_level=logging.INFO,
                  env_key='LOG_CFG'):
    """Setup logging configuration."""

    def load_logging_from_yml(path):
        """Load logging configuration from yml file"""
        with open(path, 'rt') as filehan:
            config = yaml.load(filehan)
        logging.config.dictConfig(config)

    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    syspath = sys.prefix + '/etc/osiris-ext/' + os.path.split(path)[1]
    if os.path.exists(path):
        load_logging_from_yml(path)
    elif os.path.exists(syspath):
        load_logging_from_yml(syspath)
    else:
        logging.basicConfig(level=default_level)
