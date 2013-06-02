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

1. `PUT /lang/{name}`: Creates a new language. 
2. `GET /lang/{id|name}`: Gets an existing language with a given `id` or `name`
3. `GET /lang/search/{term}`: Gets a list of existing languages that has `term` in its `name`
4. `POST /lang/{id}/update`: Updates a language given `id`.
5. `DELETE /lang/{id}`: Deletes a language given `id`.


###Request

The request body must be `application/x-www-form-urlencoded` formatted for `POST`, `PUT`.
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

        $ curl   "http://127.0.0.1:8080/lang/ZPL"  -X PUT -d "Influenced+by=C&Developer=Chamberlain+et+al.+at+University+of+Washington"
        {
            "data":         {
                "Developer": "Chamberlain et al. at University of Washington", 
                "Influenced by": "C", 
                "lang_id": 429, 
                "name": "ZPL"
            }, 
            "success": true
        }

2. Search a language

        $ curl   "http://127.0.0.1:8080/lang/search/java"
        {
            "data": [
                {
                    "Appeared in": "1995 \u00a0( 1995 ) [ 1 ]", 
                    "Designed by": "James Gosling and Sun Microsystems", 
                    "Developer": "Oracle Corporation", 
                    "Dialects": "Generic Java , Pizza", 
                    "Implementation language": "C and C++", 
                    "Influenced": "Ada 2005 , BeanShell , C# , Clojure , D , ECMAScript , Groovy , J# , JavaScript , PHP , Python , Scala , Seed7 , Vala", 
                    "Influenced by": "Ada 83 , C++ , C# , [ 2 ] Eiffel , [ 3 ] Generic Java , Mesa , [ 4 ] Modula-3 , [ 5 ] Oberon , [ 6 ] Objective-C , [ 7 ] UCSD Pascal , [ 8 ] [ 9 ] Smalltalk", 
                    "License": "GNU General Public License , Java Community Process", 
                    "Major implementations": "OpenJDK , many others", 
                    "OS": "Cross-platform (multi-platform)", 
                    "Paradigm(s)": "multi-paradigm : object-oriented , structured , imperative , generic , reflective", 
                    "Stable release": "Java Standard Edition 7 Update 21 (1.7.21) (April\u00a016,\u00a02013 ; 47 days ago \u00a0( 2013-04-16 ) )", 
                    "Typing discipline": "Static, strong, safe , nominative , manifest", 
                    "Usual filename extensions": ".java, .class, .jar", 
                    "lang_id": 197, 
                    "name": "Java"
                }, 
                {
                    "Developer": "Sun Microsystems", 
                    "License": "GPL", 
                    "OS": "Cross-platform", 
                    "Platform": "Java Runtime Environment", 
                    "Stable release": "1.2 (June\u00a02,\u00a02009 \u00a0( 2009-06-02 ) )", 
                    "lang_id": 205, 
                    "name": "JavaFX Script"
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