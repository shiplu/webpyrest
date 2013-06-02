##Abstract

The project shows how webpy can be used to implement a REST server. 


##Installation

1. Get [Web.Py](http://webpy.org/install)
2. Create a database with your favorite mysql admin console (phpmyadmin, mysql workbench etc)
3. Load the sql file `schema.sql` on the database created on last step.
4. Load the sql file `data.sql` same way
5. Run the application by invoking

        python server.py  8080

    This will run the server on 8080 port
6. Your REST server is ready. 




##Usage

There are 5 operation it supports. 

1. `/lang/create`: Creates a new language. 
2. `/lang/view/{id}`: Gets an existing language with a given `id`
3. `/lang/search/{name}`: Gets a list of existing languages that has `name` in its name
4. `/lang/update/{id}`: Updates a language given `id`.
5. `/lang/delete/{id}`: Deletes a language given `id`.


###Request

We use `POST`, `GET`, `DELETE` request methods in following way.

1. `create` and `update` requires `POST` request
2. `search` and `view` requires `GET` request
3. `delete` requires `DELETE` request

The request body must be `application/x-www-form-urlencoded` formatted for POST.
For `GET`, its the url format on [usage](#usage) above.

###Response

Response is always in `JSON` formatted string. 

For error response the format is like

    {
        "data": [], 
        "error": "ERROR MESSAGE", 
        "success": false
    }

For successful request it should look like this

    {
        "data": {
            "data": "{\"appeard in\": \"2013\", \"name\": \"PHP5.5\", \"Developer\": \"Zend\"}", 
            "lang_id": 11, 
            "name": "PHP5.5"
        }, 
        "success": true
    }
Here the `data` property (sibling of `success`) can contain either `array` or `object`
depending on the resource you are fetching.



###Examples

Here are some examples that will get you started. Note JSON output is not pretty formatted 
as shown bellow. Rather its a single line.

1. Create a language

        $ curl -i  "http://localhost:8080/lang/create" -d "name=PHP5.5&appeard+in=2013&Developer=Zend"
        {
            "data": {
                "data": "{\"appeard in\": \"2013\", \"name\": \"PHP5.5\", \"Developer\": \"Zend\"}", 
                "lang_id": 11, 
                "name": "PHP5.5"
            }, 
            "success": true
        }

2. Search a language

        $ curl  "http://localhost:8080/lang/search/php" 
        {
            "data": [
                {
                    "data": "{\"Paradigm[]\": \"functional\", \"Type\": \"Scripting\", \"name\": \"PHP\"}", 
                    "lang_id": 10, 
                    "name": "PHP"
                }, 
                {
                    "data": "{\"appeard in\": \"2013\", \"name\": \"PHP5.5\", \"Developer\": \"Zend\"}", 
                    "lang_id": 11, 
                    "name": "PHP5.5"
                }
            ], 
            "success": true
        }

3. Updates a language

        $ curl -i  "http://localhost:8080/lang/update/11" -d "name=PHP5.4&appeard+in=2012"
        {
            "data": {
                "data": "{\"appeard in\": \"2012\", \"name\": \"PHP5.4\", \"Developer\": \"Zend\"}", 
                "lang_id": 11, 
                "name": "PHP5.4"
            }, 
            "success": true
        }



##Contribution

If you like to contribute go ahead and fork.

The source tree has different files.

- `README.md` is this file
- `config.py` contains application configuration. Currently it holds database connection information
- `schema.py` contains mysql table definition
- `server.py` the main server file. You need to run this file to start the server
- `lang/controller.py` contains all the controller logic for the rest api. It retrieves data from model 
    and shows it json format. 
- `lang/model.py` contains the database access layer. Just read, write on language table