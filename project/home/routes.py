from . import home_blueprint


@home_blueprint.route('/')
def home():
    return { 'message': 'Hello World!' }, 200