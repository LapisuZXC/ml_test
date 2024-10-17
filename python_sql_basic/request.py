import json


request = {
  "cookies": {"auth_key": "sDIUF23iS9-dhirH_R2-si-s", "key_2": "value_2"},
  "body": "a long time ago, in a Galaxy far, far away",
  "headers": {"content-type": "application/json", "Accept": "application/json"}
}



class Handler:
    def __init__(self, dict: dict):
        self.dict = dict


class ParsesCookies:
    def __init__(self, dict: dict):
        self.dict = dict
        
    
    
    def cookies(self):
        if self.dict["cookies"]:
            return str(self.dict["cookies"])
        else:
            raise ValueError("no cookies")
    
    
    def is_authed(self):
        if self.dict.get("cookies").get("auth_key"):
            return True
        else:
            return False

class ParsesBody:
    def __init__(self, dict: dict):
        self.dict = dict

    def body(self):
        if self.dict.get("body"):
            return str(self.dict["body"])
        else:
            raise ValueError("no body")


class ParsesHeaders:
    def __init__(self, dict: dict):
        self.dict = dict

    
    def headers(self):
        if self.dict.get("headers"):
            return str(self.dict["headers"])
        else:
            raise ValueError("no headers")

    def need_json(self):
        if self.dict.get("headers").get("Accept"):
            if self.dict.get("headers").get("Accept") == 'application/json':
                return True
            else:
                return False

class JSON_handler(ParsesBody, ParsesHeaders):
    def __init__(self,dict : dict):
        super().__init__(dict)
    
    def proccess(self):
        if not super().need_json():
            return None
        else:
            try:
                json.loads(super().body())
                return str(json.loads(super().body(self.dict)))
            except:
                return None

class SecureTextHandler(ParsesCookies,ParsesBody,ParsesHeaders):
    def __init__(self, dict: dict):
        super().__init__(dict)

    def proccess(self):
        if not super().is_authed():
            return None
        else:
            return len(super().body())



handler = Handler(request)
c = ParsesCookies(request)
b = ParsesBody(request)
h = ParsesHeaders(request)
j = JSON_handler(request)


print(c.cookies(), c.is_authed())
print(b.body())
print(h.headers(), h.need_json())
print(j.proccess())
print(SecureTextHandler(request).proccess())
