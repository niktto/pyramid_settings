from pyramid.config import Configurator

from pyramid_settings import load_settings


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    load_settings(__name__, settings, config=global_config)
    print(settings)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
