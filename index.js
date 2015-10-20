#!/usr/local/bin/node

'use strict';

var express = require( 'express' );
var exphbs  = require( 'express-handlebars' );
var Router = require( './router' );

var app = express();
app.engine( 'handlebars', exphbs( { defaultLayout: 'main' } ) );
app.set( 'view engine', 'handlebars' );

var router = new Router( app );
router.go();
