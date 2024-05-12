import sys
import os

# Get the current directory of the script
project_home = os.path.dirname(os.path.abspath(__file__))

# Add your project directory to the sys.path
if project_home not in sys.path:
    sys.path.append(project_home)

# Import flask app but need to call it "application" for WSGI to work
from flask_app import app as application  # noqa
