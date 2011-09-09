## 99glitches -- a codex toy


import Tkinter as tk
import os, random, copy, OSC, StringIO, time
from PIL import Image, ImageTk

class nnGlitches:

	index = 0
	images = []
	master = []

	def __init__(self,path,root):
		
		self.path = path
		self.root = root
		
		self.panel = tk.Label(root)
		self.image_list = os.listdir(path)

		# build the images array
		for image in self.image_list:
			f = open(path + "/" + image,"rb")
			self.images.append(bytearray(f.read()))
			self.master = copy.deepcopy(self.images)	
	
	def glitch(self):
		
		# randomly apply 1 to 3 levels of glitch
		for _ in range(random.randint(1,3)):
			
			byte_array = self.images[self.index]		
			rand = random.randint(500,len(byte_array)-1)
			byte_array[rand] = random.randint(0,255)			
			
			try:
				image1 = ImageTk.PhotoImage(Image.open(StringIO.StringIO(byte_array)))
				
				panel = tk.Label(root, image=image1)
				panel.pack()
				panel.image = image1
				
				self.panel.destroy()
				self.panel = panel
				
				# image glitch is successful, rewrite to the array for reglitchin'
				self.images[self.index] = byte_array
			except:
				# the image is effd. refresh it. 
				self.images[self.index] = self.master[self.index]
				print "readd @ " + str(self.index)
				pass
		
		# 50/50 chance of reprocessing the same image
		if(random.randint(0,1)):
			if self.index >= len(self.image_list)-1: self.index=0
			else: self.index+=1
			root.after(100, self.glitch)
			print self.index
		else: 
			root.after(20, self.glitch)

## init
root = tk.Tk()
root.title('99glitches')
root.geometry("%dx%d+%d+%d" % (800,600, 0, 0))

glitch_obj = nnGlitches('img',root)

root.after(100, glitch_obj.glitch)
root.mainloop()