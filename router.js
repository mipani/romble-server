'use strict';

var _ = require( 'underscore' );

class Router {

	/**
	 * @property		{Object}		appInstance
	 * The application instance that we register endpoints against
	 */

	/**
	 * @property		{Object}		routes
	 * A table of routes to handler functions
	 */

	constructor( appInstance ) {
		this.appInstance = appInstance;

		this.setupRoutes();
	}

	setupRoutes() {
		this.getRoutes = {
			'/': this.serveDefaultRoute
		};

		_( this.getRoutes ).each( function( callback, route ) {
			this.appInstance.get( route, callback );
		}, this );
	}

	serveDefaultRoute( request, response ) {
		response.render( 'home' );
	}

	go() {
		this.appInstance.listen( Router.DEFAULT_PORT );
	}
}

Router.DEFAULT_PORT = 3000;

module.exports = Router;
