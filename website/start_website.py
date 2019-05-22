import app
import logging
from waitress import serve


serve(app.create_app(), listen='0.0.0.0:80')

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)
