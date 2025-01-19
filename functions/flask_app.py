from src import app  # Import your Flask app
from aws_lambda_wsgi import response

def handler(event, context):
    """AWS Lambda handler for the Flask app."""
    return response(app, event, context)
