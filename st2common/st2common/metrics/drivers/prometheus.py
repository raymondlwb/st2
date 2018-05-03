# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from prometheus_client import Histogram, Gauge

from st2common.metrics.metrics import BaseMetricsDriver, check_key


class PrometheusDriver(BaseMetricsDriver):
    """ Base class for driver implementations for metric collection
    """
    def __init__(self):
        pass

    def time(self, key, time):
        """ Timer metric
        """
        prometheus_histogram = Histogram(  # pylint: disable=no-value-for-parameter
            key
        )
        prometheus_histogram.observe(time)

    def inc_counter(self, key, amount=1):
        """ Increment counter
        """
        prometheus_counter = Gauge(  # pylint: disable=no-value-for-parameter
            key
        )
        prometheus_counter.inc(amount)

    def dec_counter(self, key, amount=1):
        """ Decrement metric
        """
        prometheus_counter = Gauge(  # pylint: disable=no-value-for-parameter
            key
        )
        prometheus_counter.dec(amount)
