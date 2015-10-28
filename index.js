#!/usr/local/bin/node

'use strict';

var Express = require( 'express' );
var exphbs  = require( 'express-handlebars' );
var Router = require( './router' );
var Locale = require( './locale/locale' );

class Application {

	/**
	 * @property	{Express}		expressInstance
	 * An instance of the Express framework
	 */

	 /**
	  * @property	{Router}		router
	  * An instance of Romble router.
	  */

	 // Set up an Application instance
	 constructor() {
		this.init();
	 }

	 init() {
		this.expressInstance = Express();

		this.expressInstance.engine( Application.TEMPLATE_ENGINE, exphbs( { defaultLayout: 'main' } ) );
		this.expressInstance.set( 'view engine', Application.VIEW_ENGINE );

		this.router = new Router( this.expressInstance );
		this.router.go();
	 }
};

Application.TEMPLATE_ENGINE = 'handlebars';
Application.VIEW_ENGINE = 'handlebars';

var application = new Application();

console.log( Locale.getInstance().getString( 'APPLICATION_TITLE' ) + ' OK!' );
