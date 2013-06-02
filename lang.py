"""
CRUD based REST API for 'lang' resource
"""


class create:
    """Creates language. Supports only POST method."""
    def POST(self):
        return "Create POST"

class delete:
    """Deletes language. Supports only DELETE method."""
    def DELETE(self):
        return "delete  DELETE"

class update:
    """Updates language. Supports only POST method."""
    def POST(self):
        return "update POST"

class view:
    """Gets a language informaiton by its id. Supports only GET method."""
    def GET(self, id):
        return "view GET"

class search:
    """Searches for a language by name. Supports only GET method."""
    def GET(self, name):
        return "view GET"

