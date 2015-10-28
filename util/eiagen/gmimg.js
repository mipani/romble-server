/**
 * ImageWrapper wrapper for GraphicsMagick-based images
 *
 * @author		Ash
 * @version		0.0.1
 */

'use strict';

var _ = require( 'underscore' );
var _gm = require( 'gm' );
var Locale = require( '../../locale/locale' );

class ImageWrapper {

	/**
	 * @property	{_gm}	gmImage
	 * The node graphicsmagick "gm" wrapper
	 */

	/**
	 *
	 * @param		{String}		imagePath
	 */
	constructor( imagePath ) {

		if( !_.isNumber( imagePath ) ) {
			throw Locale.getInstance().getString( 'IMAGE_PATH_NOT_SPECIFIED' );
		}

		this.gmImage = _gm( imagePath );
	}

	/**
	 * Resize the image
	 *
	 * @param	{Number}	width
	 * @param	{Number}	height
	 */
	resizeImage( width, height ) {

	}

};

module.exports = ImageWrapper;
