import web
import config
import json


class lang:
    """
    Provides operations on language
    """
 
 
    
    def __init__(self):
        self.db = web.database(
            dbn=config.DBDRIVER, 
            user=config.DBUSER, 
            pw=config.DBPASS, 
            db=config.DBNAME
        )
        self.table = 'langs'
 
 
 
 
    
    def create(self, name, data):
        """
        Creates a new lang instance and returns it
        Args:
            name: name of the language
            data: dictionary of column and and values to be updated 
        """
        
        # make sure the name is consistence every where
        data['name'] = name;
        
        sq = self.db.insert(self.table, name=name, data=json.dumps(data))
        return self.find_by_id(sq)





    def update(self, lang_id, data):
        """
        Updated a language with a given langugae id.
        Args:
            lang_id language id
            data: dictionary of column and and values to be updated 
        
        Returns:
            updated language
        """
        
        row = self.find_by_id(lang_id)
        if row:
            # Update the existing data with new one 
            updated_data = json.loads(row['data'])
            updated_data.update(data)
            
            # make sure we dont change the id in json text
            # though it does not matter. but for the sake of consistency
            updated_data['lang_id'] = lang_id
            updated_json = json.dumps(updated_data)

            
            self.db.update(self.table, where="lang_id=$id", vars={'id': lang_id}, data=updated_json, name=updated_data['name'])

            return self.find_by_id(lang_id)
        else:
            return {}







    def delete(self, _id):
        """
        Deletes a language for given id
        """
        
        self.db.delete(self.table, vars={'id': _id}, where="lang_id = $id")
        return {}






    def find_by_name(self, name):
        """
        Finds a language with a given name
        Returns: 
            language instance data
        """
        
        results = self.db.select(self.table, vars={'name': name}, where="name LIKE CONCAT('%', $name, '%')")
        if results: 
            ar = []
            for row in results:
                ar.append(dict(row))
            return ar
        else:
            return []





    def find_by_id(self, _id):
        """
        Finds a language with a give unique id
        
        """
        
        results = self.db.select(self.table, vars={'id': _id}, limit=1, where="lang_id = $id")
        
        if results: 
            return results[0]
        else:
            return {}


