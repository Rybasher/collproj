from brighton import app
from one.blueprints import posts
import view
import os


app.register_blueprint(posts, url_prefix='/meetings')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(debug=True, port=port)
