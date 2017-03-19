q#!/usr/bin/env python

import re

log_files = open('access_log-20131117', 'r')

# Print IP addresses
for part in log_files:
  line = re.findall(r'^([0-9.]+)', part)
  print line
