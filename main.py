import os
import sys

import connexion
from dotenv import load_dotenv

os.environ['AWS_ACCESS_KEY_ID'] = 'localstack'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'localstack'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api('swagger.yaml', arguments={'title': 'Docs Mining API'})
app.app.secret_key = "LeafmanZSecretKey"

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
