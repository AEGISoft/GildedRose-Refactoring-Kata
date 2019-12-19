# -*- coding: utf-8 -*-
from __future__ import print_function
from test_golden_master import golden_master_test_run, persist_golden_master_testrun

if __name__ == "__main__":
    # persist_golden_master_testrun()
    for line in golden_master_test_run():
        print(line)
