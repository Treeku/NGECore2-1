
from services.sui import SUIWindow
from services.sui.SUIWindow import Trigger
from java.util import Vector
import sys

def setup():
    return
    
def run(core, actor, target, commandString):
	core.chatService.broadcastGalaxy(commandString)
	actor.sendSystemMessage(' \\#FE2EF7 [GM] \\#FFFFFF broadcastGalaxy: Command completed successfully.', 0)
	return