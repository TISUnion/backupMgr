# -*- coding: utf-8 -*-

from savelib import mcsave
import time

helpmsg = '''
wtf is this shit
'''

autoBackupEnabled = True
autoBackupInterval = 24 #in hours
skipIfSave = True

def onServerStartup(server):
  while autoBackupEnabled:
    time.sleep(autoBackupInterval * 3600)
    if not hasSaved:
      makebackup('backupmgr', 'Plugin auto backup')
      hasSaved = False

def onServerInfo(server, info):
  if (info.isPlayer == 0) and (info.content.startswith('!!bm')):
    if (args = info.content.split(' '))[0] == '!!bm'):
      if (len(args) == 1):
        for line in helpmsg.splitlines:
          server.tell(info.player, line)
      if (len)
