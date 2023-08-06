import subprocess

class Key:
	def __init__(self):
		self.kontol = []
	def get(self,name):
		return str(subprocess.check_output(f"getprop ro.{name}",shell=True).decode("utf-8").split()[0])
	def generate(self):
		data = ["product.model", "build.version.release", "build.id", "hwui.text_large_cache_height","product.brand"]
		result_list = []
		for z in data:
			result_list.append(self.get(z))
		return "".join(f.replace(".","") for f in result_list)
	def check(self,key):
		default = self.generate()
		if key == default.lower():
			print("key benar")
		else:
			print("key salah")
	
Key().check("rmx337013tp1a2209050011024realme")