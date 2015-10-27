'use strict';

var _ = require( 'underscore' );
var TestView = require( './views/testview' );

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
			'/': _.bind( this.serveDefaultRoute, this ),
			'/test': _.bind( this.serveTestRoute, this )
		};

		_( this.getRoutes ).each( function( callback, route ) {
			this.appInstance.get( route, callback );
		}, this );
	}

	serveDefaultRoute( request, response ) {
		response.render( 'home' );
	}

	serveTestRoute( request, response ) {
		this.testView = this.testView || new TestView();
		response.send( this.testView.render() );
	}

	go() {
		this.appInstance.listen( Router.DEFAULT_PORT );
	}
}

Router.DEFAULT_PORT = 3000;

module.exports = Router;
