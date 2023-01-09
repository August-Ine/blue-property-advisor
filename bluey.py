import os
from app import create_app, db
from app.models import User,Role 

#create app instance with selected config 
app = create_app(os.getenv('FLASK_CONFIG','development'))

#to make the variables available for debugging with the python shell
@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User,Role=Role)
