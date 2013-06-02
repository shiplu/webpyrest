import web
import lang

#render = web.template.render('templates/')
	

"""
Url mapping
Basically a url of type /X/Y/Z will be handled by X module's Y class with parameter Z
So, 
lang/create will be be handled by lang.create class
lang/view/3 will be be handled by lang.view class with parameter 3

"""
urls = (
  '/(\w*)/(create|delete|update)', '\1.\2'
  '/(\w*)/(view|search)/(.*)', '\1.\2'
)

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()        


