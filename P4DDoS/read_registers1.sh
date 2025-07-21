#!/bin/bash

# Copyright 2013-present Barefoot Networks, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

echo "Switch 10.0.1.1"

echo "===== Displaying statusReg contents ====="

for i in 0 1 2 3 4; do
    case $i in
        0) label="pkt_counter" ;;
        1) label="alarm" ;;
        2) label="Hnorm" ;;
        3) label="ewma" ;;
        4) label="threshold" ;;
    esac

    echo
    echo "[$label]"
    echo "register_read statusReg $i" | docker exec -i hh simple_switch_CLI --thrift-port 22222
done

