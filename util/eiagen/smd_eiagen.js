/**
 * Sega Megadrive eiagen
 *
 * @author		Ash
 * @version		0.0.1
 */

'use strict';

var _ = require( 'underscore' );
var FS = require( 'fs' );

class SmdEiaFactory {

	/**
	 * Generates an EIA image and deposits the result in ../tmp/<filename>
	 *
	 * @param		{String}		imagePath		Pathname to image file
	 * @param		{String}		result			Filename in ../tmp to deposit in
	 * @param		{Boolean}		newImage		Disable caching, throw out whatever
	 * 												may be in tmp
	 */
	generateEIA( imagePath, result, newImage ) {

		// If explicitly requested, or the file doesn't exist
		// Regenerate the file in the ../../tmp directory
		if( newImage === true || !this._fileExists( '../../tmp/' + result ) ) {
			// Create an ImageWrapper
			var image = new ImageWrapper( imagePath );

			// If either width or height is greater than 320 and 224 respectively,
			// resize the image down to 320x224
		}

	}

	/**
	 * Works around node's crappy, exception-based method of verifying a file's existence
	 *
	 * @private
	 * @param		{String}		path
	 * @returns		{Boolean}
	 */
	_fileExists( path ) {
		try {
			FS.accessSync( path, FS.R_OK );
			// File exists
			return true;
		} catch( e ) {
			// File does not exist
			return false;
		}
	}
};

module.exports = SmdEiaFactory;
