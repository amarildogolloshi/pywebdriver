#!/usr/bin/env python
# -*- encoding: utf-8 -*-
##############################################################################
#
#    PyWebDriver Software
#    Copyright (C) 2014-TODAY Akretion <http://www.akretion.com>.
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


# Core Imports
import gettext
import os

from ConfigParser import ConfigParser

# Librairies Imports
from flask import Flask
from flask.ext.babel import Babel

# Config Section
LOCAL_CONFIG_PATH = '%s/../config/config.ini' % os.path.dirname(
    os.path.realpath(__file__))
PACKAGE_CONFIG_PATH = '/etc/pywebdriver/config.ini'

config_file = PACKAGE_CONFIG_PATH
if not os.path.isfile(config_file):
    config_file = LOCAL_CONFIG_PATH
assert os.path.isfile(config_file), (
    'Could not find config file (looking at %s and then %s )' % (
        PACKAGE_CONFIG_PATH, LOCAL_CONFIG_PATH))
config = ConfigParser()
config.read(config_file)

drivers = {}

# Project Import
# Application
app = Flask(__name__)

from . import views
from . import plugins

# Localization
app.config['BABEL_DEFAULT_LOCALE'] = config.get('localization', 'locale')
babel = Babel(app)

path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'translations')
localization = config.get('localization', 'locale')
language = gettext.translation(
    'messages',
    path,
    [localization])
language.install(unicode=True)
