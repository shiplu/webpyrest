import web
import config
import json
import model



"""
CRUD based REST API for 'lang' resource
"""


class crudbase:
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


class create(crudbase):
    """
    Creates language. Supports only POST method.
    """

    def POST(self, op):
        inp = web.input(name='_')
        if inp.name == '_':
            return self.error("name not provided")
        try:
            ret = self.output(self.model.create(inp.name, dict(inp)))
        except:
            ret = self.error("Creation Failed")
        return ret

class delete(crudbase):
    """
    Deletes language. Supports only DELETE method.
    """

    def DELETE(self, op, lang_id):
        #try:
        ret = self.output(self.model.delete(lang_id))
        #except:
            #ret = self.error("Delete Failed")
        return ret


class update(crudbase):
    """
    Updates language. Supports only POST method.
    """

    def POST(self, op, lang_id):
        inp = web.input()
        try:
            ret = self.output(self.model.update(lang_id, dict(inp)))
        except:
            ret = self.error("Update Failed")
        return ret



class view(crudbase):
    """
    Gets a language informaiton by its id. Supports only GET method.
    """

    def GET(self, op, lang_id):
        try:
            ret = self.output(self.model.find_by_id(lang_id))
        except:
            ret = self.error("Search Failed")
        return ret


class search(crudbase):
    """
    Searches for a language by name. Supports only GET method.
    """

    def GET(self, op, name):
        #try:
        ret = self.output(self.model.find_by_name(name))
        #except:
            #ret = self.error("Search Failed")
        return ret

