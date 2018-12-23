import subprocess

class gpr:
	def __init__(self, path_to_gpr_tools="gpr_tools"):
		self.gpr = path_to_gpr_tools
	def __convert(self, command):
		p = subprocess.Popen(command, shell=True)
		out, err = p.communicate()
	def convert(self, input_image, output_image=None):
		if input_image != None and output_image != None:
			self.__convert(self.gpr + " -i " + input_image + " -o " + output_image)
		if input_image != None and output_image == None:
			self.__convert(self.gpr + " -i " + input_image + " -o " + input_image.replace("GPR","DNG"))
	def analyze(self, input_image, output_file=None):
		if output_file == None:
			self.__convert(self.gpr + " -i " + input_image + " -d 1", shell=True)
		else:
			self.__convert(self.gpr + " -i " + input_image + " -d 1 > " + output_file)
