/**
 * Locale wrapper for Romble
 *
 * @author		Ash
 * @version		0.0.1
 */

'use strict';

var Settings = require( '../options' );

let singleton = Symbol();
let singletonEnforcer = Symbol();

class Locale {

	/**
	 * @property	{Object}	currentLocale
	 * The lookup table for locale strings
	 */

    /**
     * @param 	{Symbol}	enforcer
     */
    constructor( enforcer ) {
        if ( enforcer !== singletonEnforcer ) {
            throw "Cannot construct locale singleton!";
        }

        // Sets the locale table based on the setting specified
        var currentLocale = './' + Settings.CURRENT_LOCALE;
        this.currentLocale = require( currentLocale );
    }

    /**
     * @returns Locale
     */
    static getInstance() {
        if ( !this[ singleton ] ) {
            this[ singleton ] = new Locale( singletonEnforcer );
        }
        return this[ singleton ];
    }

	/**
	 * Get a locale string for the current locale
	 *
	 * @param		{String}		id		Locale string id
	 * @returns		{String}
	 */
	getString( id ) {
		return this.currentLocale[ id ];
	}

}

module.exports = Locale;
