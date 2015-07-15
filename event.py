import threading
import graphics
import time

def askForKeys(stack, screen):
		"""
			function to manage real time keys
		"""
		cond = True
		while  True:
			time.sleep(0.1)
			screen.printInput()





class keysManager:
	def __init__(self, Gengine ):
		self.stack = []#thread safe data structure no locks needed
		self.screen = Gengine.screen


	def launchThread(self):
		t = threading.Thread( target = askForKeys , args=(self.stack , self.screen))
		t.setDaemon(True)
		self.screen.addstr( 0 , 0 , "putixQQQQQQQQQQQQQQQQQQQQQ")
		time.sleep(3)
		t.start()

