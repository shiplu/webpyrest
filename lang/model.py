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
        sq = self.db.insert(self.table, name=name, data=json.dumps(data))
        return self.find_by_id(sq)

    def update(self, _id, data):
        row = self.find_by_id(_id)
        if row:
            # Update the existing data with new one 
            data1 = json.loads(row['data'])
            data2 = json.loads(data)
            data1.update(data2)
            
            # make sure we dont change the id in json text
            # though it does not matter. but for the sake of consistency
            data1['id'] = _id
            
            
            var = dict(id=_id)
            self.db.update(self.table, var, where="lang_id=$id", data=data1)
            return self.find_by_id(_id)
        else:
            return {}


    def delete(self, _id):

        var = dict(id=_id)
        return self.db.delete(self.table, var, limit=1, where="lang_id = $id")


    def find_by_name(self, name):

        var = dict(name=name)
        results = self.db.select(self.table, var, limit=1, where="name = $name")
        if results: 
            return results[0]
        else:
            return {}


    def find_by_id(self, _id):

        var = dict(id=_id)
        results = self.db.select(self.table, var, limit=1, where="lang_id = $id")
        
        if results: 
            return results[0]
        else:
            return {}


