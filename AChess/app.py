#
# Web based GUI for AChess
#

# packages
from flask import Flask
from flask import render_template

# create web app instance
app = Flask(__name__)

# define root(index) route
@app.route('/')
def root():
    return render_template('AChess.html')

# main driver
if __name__ == '__main__':
    # Start HTTP server
    app.run(debug= True, threaded= True)
