#!/usr/bin/python3
import sys
import common
from engine.handler import event_manager
from engine import main


if __name__ == '__main__':

#    sys.excepthook = common.new_hook
    main(event_manager)
