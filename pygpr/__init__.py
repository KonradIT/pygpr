import subprocess

class gpr:
	def __init__(self, path_to_gpr_tools):
		self.gpr = path_to_gpr_tools

	def convert(self, input_image, output_image):
		if input_image != None and output_image != None:
			subprocess.Popen(self.gpr + " -i " + input_image + " -o " + output_image, shell=True)
	def analyze(self, input_image, output_file=None):
		if output_file == None:
			subprocess.Popen(self.gpr + " -i " + input_image + " -d 1", shell=True)
		else:
			subprocess.Popen(self.gpr + " -i " + input_image + " -d 1 > " + output_file, shell=True)
