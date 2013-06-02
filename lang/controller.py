import web
import config
import json
import model
import traceback
import re

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



class language(controller_base):
    """
    Create, Delete and Read language with PUT, DELETE, GET method
    """
    
    def DELETE(self, lang_id):
        try:
            ret = self.output(self.model.delete(lang_id))
            return ret
        except:
            print traceback.format_exc()
            return self.default_error()
            raise


    def PUT(self, name):
        
        inp = web.input()
        try:
            ret = self.output(self.model.create(name, dict(inp)))
            return ret
        except:
            print traceback.format_exc()
            return self.default_error()
            raise   


    def GET(self, idorname):
        """
        Gets a language informaiton by its id or name. Supports only GET method.
        """

        try:
            if re.match(r'^\d+$', idorname):
                ret = self.output(self.model.find_by_id(idorname))
            else:
                ret = self.output(self.model.find_by_name(idorname))
                
            return ret
        except:
            print traceback.format_exc()
            return self.default_error()
            raise


class update(controller_base):
    """
    Updates language. Supports only POST method.
    """

    def POST(self, lang_id):
        inp = web.input()
        try:
            ret = self.output(self.model.update(lang_id, dict(inp)))
            return ret
        except:
            print traceback.format_exc()
            return self.default_error()
            raise





class search(controller_base):
    """
    Searches for a language by name. Supports only GET method.
    """

    def GET(self, name):
        try:
            ret = self.output(self.model.find_all_by_name(name))
            return ret
        except:
            print traceback.format_exc()
            return self.default_error()
            raise


