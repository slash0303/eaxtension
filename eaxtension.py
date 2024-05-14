import time
import json


def version():
    version = "1.1.0"
    last_edit = "add sav option in LogE"
    print(f"version: {version}. last edit: '{last_edit}'")


# Log Class
class LogE:
    tim = time.localtime(time.time())
    time_format = "%Y-%m-%d %H:%M:%S"
    Log_time = str(time.strftime(time_format, tim))

    # sav feature
    @staticmethod
    def sav(target_file:str, log_name:str, log_data:str):
        log_string = f"\n{timeE.geta()} | {log_name} | {log_data}"
        with open(target_file, "a", encoding="utf-8") as log_file:
            log_file.write(log_string)

    # normal log
    @staticmethod
    def d(Log_name, Log_text, **attr):
        tim = time.localtime(time.time())
        time_format = "%Y-%m-%d %H:%M:%S"
        Log_time = str(time.strftime(time_format, tim))
        print(f"{Log_time} | {Log_name} : {Log_text}")

        try:
            if attr["target_file"]:
                LogE.sav(attr["target_file"], Log_name, Log_text)
        except:
            pass


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
    @staticmethod
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

    # json dumps
    @staticmethod
    def dumps(file_name: str, content: dict, **attr):
        # file name filter: does string of file name have extension?
        json_ext = file_name[-5:]
        if json_ext == ".json":
            pass
        else:
            file_name = file_name + ".json"

        with open(file_name, "w", encoding="utf-8") as json_file:
            json.dump(content, json_file, ensure_ascii=False, indent=4)

        # kwargs - silent: if this attr was activated, it will not print log message. 
        try:
            if attr["silent"] != True:
                LogE.g("dumps json", f"'{file_name}' is dumped")
        except KeyError:
            LogE.g("dumps json", f"'{file_name}' is dumped")

    # json load
    @staticmethod
    def load(file_name, **attr):
        json_ext = file_name[-5:]
        if json_ext == ".json":
            pass
        else:
            file_name = file_name + ".json"
        try:
            if attr["silent"] != True:
                LogE.g("load json", f"'{file_name}' is loaded")
        except KeyError:
            LogE.g("load json", f"'{file_name}' is loaded")

        with open(file_name, "r") as json_file:
            content = json.load(json_file)
            return content

    # json merge
    @staticmethod
    def merge(file_name: str, content: dict, **attr):
        json_ext = file_name[-5:]
        if json_ext == ".json":
            pass
        else:
            file_name = file_name + ".json"

        with open(file_name, "r", encoding="utf-8") as json_file:
            try:
                json_data = json.load(json_file)
            except json.JSONDecodeError:
                LogE.e("error(JSONDecodeError)", f"'{file_name}' has problem. please re-dump '{file_name}'.")
            content_keys = content.keys()
            try:
                if attr["allY"] == True:
                    for key in content_keys:
                        json_data[key] = content[key]
                        LogE.g("merge json", f"'{file_name}' is dumped/merged by content.")
                else:
                    pass
            except KeyError:
                pass
            finally:
                for key in content_keys:
                    try:
                        if json_data[key] == None:
                            json_data[key] = content[key]
                        elif json_data[key] == content[key]:
                            pass
                        else:
                            yn = input(
                                f"key '{key}' is already exist.\n\n[{file_name}]\n\"{key}\" : {json_data[key]}\n\n[input data]\n\"{key}\" : {content[key]}\n\nwould you want to change this? [y/N] ")
                            print("---------")
                            if yn == "Y" or yn == "y":
                                json_data[key] = content[key]
                                LogE.g("merge json", "content changed completly.")
                            else:
                                LogE.g("merge json", "content doesn't changed.")
                    except KeyError:
                        json_data[key] = content[key]
                    with open(file_name, "w", encoding="utf-8") as json_file:
                        json.dump(json_data, json_file, ensure_ascii=False, indent=4)


# time class
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
        for x in time_type:
            form = form + "-" + format_dict[x]
        form = form[1:]

        LogE.t("text", form)

        output = str(time.strftime(form, tim))

        return output



if __name__ == "__main__":
    LogE.d("hello", "fuckyou", target_file="./data/test.txt")
