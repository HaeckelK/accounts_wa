from flask import Blueprint

bp = Blueprint('imports', __name__)

from accounts.imports import routes
