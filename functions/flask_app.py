import sys
import os

# Add the parent directory (where 'src' is located) to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import app
from aws_lambda_wsgi import response

def handler(event, context):
    """AWS Lambda handler for the Flask app."""
    return response(app, event, context)
