import falcon
from user_resource import UserResource


def create_app():
    application = falcon.App()
    application.add_route('/user', UserResource())
    return application

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
