#!/usr/bin/env python
#This thing just goes to main.py in the voiceServer folder
import sys
import voiceServer.main
if __name__ == '__main__':
    sys.exit(voiceServer.main.main())
