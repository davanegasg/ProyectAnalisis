import json

def convert_string_to_list(string):
    res = f"[{string}]".strip(" ")
    res_to_json = json.loads(res)
    return res_to_json