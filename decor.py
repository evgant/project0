import json


def creator(file_name):
    def decor(func):
            to_json= func()
            with open(file_name, "w") as f:
                    f.write(json.dumps(to_json, indent = 4))
            return func
    return decor



"""def creator(file_name):
        def decor(func):
                to_json= func()
                with open(file_name, "w") as f:
                        json.dump(to_json, f)
                return func
        return decor
    """