# Copyright (c) 2015 Catalyst IT Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from oslo_log import log as logging
import requests
from taskflow import task

LOG = logging.getLogger(__name__)


class WebhookTask(task.Task):
    def __init__(self, name, show_name=True, inject=None):
        super(WebhookTask, self).__init__(name, inject=inject)
        self._show_name = show_name

    def execute(self, uri, message, **kwargs):
        try:
            requests.post(uri, data=message)
        except Exception as e:
            LOG.error(e)
