pyramid_settings
----------------

`pyramid_settings` is simplest package (2 functions to be fair) that enables you
to load python modules as pyramid settings files.

TL;DR; You can ditch most of your .ini files and store your settings in clean python.

Usage
=====

    from pyramid.config import Configurator

    from pyramid_settings import load_settings


    def main(global_config, **settings):
        """ This function returns a Pyramid WSGI application.
        """
        
        load_settings(__name__, settings, config=global_config)
        
        config = Configurator(settings=settings)
        config.scan()
        return config.make_wsgi_app()

and this is all you need (if you use paster ini files and pserv) to be able to use:

    $ pserv development.ini pysettings=settings.py,base.py,roman.py
    
Warning
=======

Everything you see here is work in progress and should not be ever used in
production (trust me - don't trust me). Contributions, critique, angry letters
and such are welcome.
