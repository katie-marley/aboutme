# app.py is the main file responsible for running the app #
from flask import Flask, Response, request, url_for

# instantiate the Flask application object #
app = Flask(__name__)


# set up a route and bind a function #
@app.route('/')
def welcome_to_flask():
    return "Welcome to Flask!"


@app.route('/hello')
def hello_from_flask():
    return "Hello from Flask!"


@app.route('/goodbye')
def goodbye_from_flask():
    return "Goodbye from Flask!"


@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit Response object")
# http response created #
# links this function to making a http request #
# mimetypes='text/plain' #


@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    # universal text formatting #
    # take the data sent as part of the request the user made #
    # put it into a standard way #
    return Response("You posted this data " + data_sent)


# the route variable word is a string by default #
# equivalent to @app.route('/dynamic/<string:word>') #
@app.route('/dynamic/<word>')
def get_name(word):
    return Response("Hello " + word)
# angle brackets make it a placeholder #
# thing in the angle brackets made into a parameter #
# this route variable is


@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    message = "Your number squared is " +  str(squared)
    return message
# squares the input number #


@app.route('/sayhello/<name>')
def say_hello_page(name):
    return """
    <html>
    <head>
        <title>Simple Flask Route</title>
    </head>
    <body>
        <h1>Name Page</h1>
        <p>Hello {}!</p>
    </body>
    </html>
    """.format(name)


# want another route called /person #
# want to pass in their name and their age #
# want to return HTML that displays the person's name and age #


@app.route('/person/<name>/<int:age>')
def person(name, age):
    welcome_url = url_for('welcome_to_flask')
    hello_url = url_for('hello_from_flask')
    goodbye_url = url_for('goodbye_from_flask')
    return """
    <html>
    <head>
        <title>Simple Flask Route</title>
    </head>
    <body>
        <h1><center>Name Page</center></h1>
        <p><center>Hello <b>{}</b> your age is <b>{}</b></center></p>
        <nav><a href="{}">Welcome</a>
        <nav><a href="{}">Hello</a>
        <nav><a href="{}">Goodbye</a>
    </body>
    <br></br>
    <hr></hr>

    </nav>
    <br></br>
    <footer>
        <p><center>This page is copyrighted &copy</center></p>
    </footer>
    </html>
    """.format(name, age, welcome_url, hello_url, goodbye_url)
# here is for the wiggly braces order #


@app.route('/index/<name>/<int:age>')
def index(name, age):
    url = url_for('get_text')
    return """
    <html>
    <head>
        <title>Sample - Flask Routes</title>
    </head>
    <body>
        <h1><center>Name Page</center></h1>
        <p><center>Hello <b>{}</b></center></p>
        <p>You are {} year(s) old.</p>
        <hr>
        <a href="{}">Welcome</a>
    </body>
    </html>
    """.format(name, age, url)
# here is for the wiggly braces order #


@app.route('/names')
def names():
    url_chloe = url_for('chloe_page')
    url_marley = url_for('marley_page')
    return """
        <html>
            <head>
            <title>Names</title>                
            </head>
            <body>
                <h1>Names</h1>
                <p><a href="{}">Chloe</a></p>
                <p><a href="{}">Marley</a></p>
            </body>
        </html>
    """.format(url_chloe, url_marley)


@app.route('/about/chloe')
def chloe_page():
    url_both_names = url_for('names')
    return """
        <html>
            <head>
                <title>Chloe</title>
            </head>
        <body>
            <h1><center>This is me!</center></h1>
            <div style="background-color:#D8BFD8;color:black; padding:20px;">
            <br>
            </div>
            <img src="{{url_for('photos', filename='chloe.png')}}" align="middle"/>
            <br>
            <h2><center>These are my favourite things</center></h2>
            
            <table>
                <tr>
                    <th>Theme</th>
                    <th>Favourite</th>
                </tr>
                <tr>
                    <td>Food</td>
                    <td>Chilli Con Carne</td>
                </tr>
                <tr>
                    <td>Music</td>
                    <td>Jazz</td>
                </tr>
                <tr>
                    <td>Colour</td>
                    <td>Purple</td>
                </tr>
                <tr>
                    <td>Film</td>
                    <td>Donnie Darko</td>
                </tr>
            </table>
        </body>
        <footer>
            <p><a href="{}">BACK TO NAMES</a></p>
            <p><center>Copyright &copy</center></p>
        </footer>
        </html>
    """.format(url_both_names)


@app.route('/about/marley')
def marley_page():
    url_both_names = url_for('names')
    return """
        <html>
            <head>
                <title>Marley</title>
            </head>
        <body>
            <h1>This is me!</h1>
            <div style="background-color:#5DBB63;color:black; padding:20px;">
            <br>
            </div>
            <img src="marley.png"/>
            <br>
            <h2>These are my favourite things</h2>

            <table>
                <tr>
                    <th>Theme</th>
                    <th>Favourite</th>
                </tr>
                <tr>
                    <td>Food</td>
                    <td>Breakfast</td>
                </tr>
                <tr>
                    <td>Music</td>
                    <td>Indie</td>
                </tr>
                <tr>
                    <td>Colour</td>
                    <td>Green</td>
                </tr>
                <tr>
                    <td>Film</td>
                    <td>Shrek</td>
                </tr>
            </table>
        </body>
        <footer>
            <p><a href="{}">BACK TO NAMES</a></p>
            <p><center>Copyright &copy</center></p>
        </footer>
        </html>
    """.format(url_both_names)
# here is for the wiggly braces order #


# if this script is invoked directly (rather than being imported), run the flask app  #
if __name__ == "__main__":
    app.run(debug=True)
