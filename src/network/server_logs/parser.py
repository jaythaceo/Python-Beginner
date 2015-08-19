#!/usr/bin/env python

import re

log_files = open('access_log-20131117', 'r')

# print the result
for part in log_files:
  line = re.findall(r'^([0-9.]+)', part)
  print line
