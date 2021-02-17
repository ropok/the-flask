# # from flask import Flask, render_template

# # app = Flask(__name__)

# # # @app.route('/hello/')
# # # @app.route('/hello/<name>')
# # # def hello (name=None):
# # #     return render_template('hello.html', name=name)

# # # from markupsafe import Markup
# # # Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
# # # Markup.escape('<blink>hacker</blink>')
# # # Markup('<em>Marked up</em> &raquo; HTML').striptags()

# # from flask import request

# # with app.test_request_context('/hello', method='POST'):
# #     # now you can do something with the request until the
# #     # end of the with block, such as basic asertions:
# #     assert request.path == '/hello'
# #     assert request.method == 'POST'

# # from flask import request

# # with app.request_context(environ):
# #     assert request.method == 'POST'

# from flask import request

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')


'''
Reading Cookies:
'''
from flask import request

@app.@app.route('/')
def index():
   usernae = request.cookies.get('username')
   # use cookies.get(key) instead of cookies[key] to not get a
   # KeyError if the cookie is missing.

'''
Storing cookies:
'''
from flask import make_reponse

@app.@app.route('/')
def index():
   resp = make_reponse(render_template(...))
   resp.set_cookie('username', 'the username')
   return resp