from gunicorn.app.wsgiapp import WSGIApplication

def run_server():
    gunicorn_app = WSGIApplication()
    gunicorn_app.app_uri = 'wsgi:flask_app'  # Replace 'wsgi' with your WSGI file name and 'app' with your Flask app variable name
    gunicorn_app.run()

if __name__ == '__main__':
    run_server()
