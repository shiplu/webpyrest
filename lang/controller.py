import web
import config
import json
import model
import traceback

"""
CRUD based REST API for 'lang' resource
"""


class controller_base:
    """
    All the common tasks are performed here
    """

    def __init__(self):
        self.model = model.lang()
        # All the response will be in JSON by default
        web.header('Content-Type', 'application/json')
        # Storing any POST data found on the request
        self.data = web.data()

    def output(self, data):
        """
        Output data to browser
        """
        data = dict(
            success =True,
            data = data
        )
        return json.dumps(data)

    def error(self, str):
        """
        Shows an error to browser
        """
        data = dict(
            success = False,
            error = str,
            data = []
        )
        return json.dumps(data)


    def default_error(self):
        return self.error("Unknown error: Please wait or cotact who is responsible")




class create(controller_base):
    """
    Creates language. Supports only POST method.
    """

    def POST(self, op):
        inp = web.input(name='_')
        if inp.name == '_':
            return self.error("name not provided")
        try:
            ret = self.output(self.model.create(inp.name, dict(inp)))
            return ret
        except:
            print traceback.format_exc()
            return self.default_error()
            raise


class delete(controller_base):
    """
    Deletes language. Supports only DELETE method.
    """

    def DELETE(self, op, lang_id):
        try:
            ret = self.output(self.model.delete(lang_id))
            return ret
        except:
            print traceback.format_exc()
            return self.default_error()
            raise



class update(controller_base):
    """
    Updates language. Supports only POST method.
    """

    def POST(self, op, lang_id):
        inp = web.input()
        try:
            ret = self.output(self.model.update(lang_id, dict(inp)))
            return ret
        except:
            print traceback.format_exc()
            return self.default_error()
            raise




class view(controller_base):
    """
    Gets a language informaiton by its id. Supports only GET method.
    """

    def GET(self, op, lang_id):
        try:
            ret = self.output(self.model.find_by_id(lang_id))
            return ret
        except:
            print traceback.format_exc()
            return self.default_error()
            raise



class search(controller_base):
    """
    Searches for a language by name. Supports only GET method.
    """

    def GET(self, op, name):
        try:
            ret = self.output(self.model.find_by_name(name))
            return ret
        except:
            print traceback.format_exc()
            return self.default_error()
            raise


