"""
CRUD based REST API for 'lang' resource
"""


class create:
    """Creates language. Supports only POST method."""
    def POST(self, mod, op):
        return "Create POST"

class delete:
    """Deletes language. Supports only DELETE method."""
    def DELETE(self, mod, op):
        return "delete  DELETE"

class update:
    """Updates language. Supports only POST method."""
    def POST(self, mod, op):
        return "update POST"

class view:
    """Gets a language informaiton by its id. Supports only GET method."""
    def GET(self, mod, op, lang_id):
        return "view GET with (%s)" % (lang_id)

class search:
    """Searches for a language by name. Supports only GET method."""
    def GET(self, mod, op, name):
        return "view GET with {0}".format(name)

