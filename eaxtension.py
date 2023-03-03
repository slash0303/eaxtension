import time
import json

# Log Class
class LogE:
	
	tim = time.localtime(time.time())
	time_format = "%Y-%m-%d %H:%M:%S"
	Log_time = str(time.strftime(time_format, tim))
	
	# normal log
	@staticmethod
	def d(Log_name, Log_text):
		tim = time.localtime(time.time())
		time_format = "%Y-%m-%d %H:%M:%S"
		Log_time = str(time.strftime(time_format, tim))
		print(f"{Log_time} | {Log_name} : {Log_text}")
	
	# text red (Error Log)
	@staticmethod
	def e(Log_name, Log_text):
		tim = time.localtime(time.time())
		time_format = "%Y-%m-%d %H:%M:%S"
		Log_time = str(time.strftime(time_format, tim))
		text_red = "\033[31m"
		print(text_red + f"{Log_time} | [Error] {Log_name} : {Log_text}" + "\033[0m")
	
	# text green
	@staticmethod
	def g(Log_name, Log_text):
		tim = time.localtime(time.time())
		time_format = "%Y-%m-%d %H:%M:%S"
		Log_time = str(time.strftime(time_format, tim))
		text_green = "\033[32m"
		print(text_green + f"{Log_time} | {Log_name} : {Log_text}" + "\033[0m")
		
	# bg red (Error log)
	@staticmethod
	def E(Log_name, Log_text):
		tim = time.localtime(time.time())
		time_format = "%Y-%m-%d %H:%M:%S"
		Log_time = str(time.strftime(time_format, tim))
		bg_red = "\033[41m"
		print(bg_red + f"{Log_time} | [Error] {Log_name} : {Log_text}" + "\033[0m")

	# type check method
	def t(Log_name, Log_text):
		tim = time.localtime(time.time())
		time_format = "%Y-%m-%d %H:%M:%S"
		Log_time = str(time.strftime(time_format, tim))
		print(f"{Log_time} | {Log_name} : {type(Log_text)} | {Log_text}")

	@staticmethod
	def T(Log_name, Log_text):
		tim = time.localtime(time.time())
		time_format = "%Y-%m-%d %H:%M:%S"
		Log_time = str(time.strftime(time_format, tim))
		print(f"{Log_time} | {Log_name} : {type(Log_text)}")
		
# json Class
class jsonE:
	
	#json dumps
	def dumps(file_name: str, content, **kwargs):
		json_ext = file_name[-5:]
		
		if json_ext == ".json":
			pass
		else:
			file_name = file_name + ".json"
			
		with open(file_name, "w", encoding="utf-8") as json_file:
			json.dump(content, json_file, ensure_ascii = False, indent=4)
		LogE.g("dumps json", f"'{file_name}' is dumped")
	
	#json load
	def load(file_name):
		json_ext = file_name[-5:]
		
		if json_ext == ".json":
			pass
		else:
			file_name = file_name + ".json"
			
		LogE.g("load json", f"'{file_name}' is loaded")
		with open(file_name, "r") as json_file:
			content = json.load(json_file)
			return content
			
class timeE:
	
	# formated time text
	@staticmethod
	def geta():
		tim = time.localtime(time.time())
		time_format = "%Y-%m-%d %H:%M:%S"
		str_time = str(time.strftime(time_format, tim))

		return str_time
	
	# custom time text
	@staticmethod
	def getc(*time_type):
			tim = time.localtime(time.time())
			format_dict = {"dow": "%a", "DOW": "%A", "dowN": "%w", "day": "%d",
						   "mon": "%b", "MON": "%B", "monN": "%m", "year": "%y",
						   "YEAR": "%Y", "24hr": "%H", "12hr": "%I", "ampm": "%p",
						   "min": "%M", "sec": "%S", "week of year": "%U", "time all": "%X",
						   "date all": "%x", "time and date": "%c", }

			form = ""
			for x in (time_type):
				form = form + "-" + format_dict[x]
			form = form[1:]

			LogE.t("text", form)

			output = str(time.strftime(form, tim))\

			return output