#!/usr/bin/env python
import os
import sys
import re
from sh import ip

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yads.settings")

    primary_ip = re.sub(r'(?s).*? src\s(.*?)\s.*', r'\1',
                        str(ip("route", "get", "8.8.8.8")))
    if not primary_ip:
        primary_ip = "127.0.0.1"
    os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = primary_ip + ':15000-16000'

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
