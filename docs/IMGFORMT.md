File: IMGFORMT.TXT

Date: 10/24/2015

Description: Embedded Image Asset File Specification

Author: mipani

Version: 1.0

# What is the embedded image asset?

Embedded Image Asset (.eia,/.iff) is a file format used for image assets in
embedded systems. It is designed to be a format that, with little or no
client-side processing, can be directly loaded into your embedded system's video
hardware. They are optimal as a standard image format for classic video game
consoles.

Embedded Image Assets are greatly flexible and support any type of video
display hardware's format.

# File format

The file format uses an EA IFF 85 format container, so refer to the EA IFF 85
standard for additional information on Embedded Image Asset's "chunk" format.

The IFF format of an EIA image is as follows:

| FORM:EIAx		| EIAx, where x is the EIA Revision	      |
|-----------------------|---------------------------------------------|
| EMHD			| EMHD EMbedded image asset HeaDer	      |
| EPLO			| EPLO Embedded image asset PLatform Options  |
| EPAL			| EPAL EMbedded image asset PALette           |
| EIMG			| EIMG EMbedded IMaGe asset		      |

Any number of optional AUTH, (c)  , or TEXT chunks may be inserted. These
may contain metadata about the image in any textual format. What to do with
these chunks is up to the implementing decoder; they are completely optional
and a conformant decoder may ignore them gracefully.

## EMHD

EMHD format is as follows:

```
typedef struct {
	uint16_t		width;				Image width
	uint16_t		height;				Image height
	uint8_t			bpp;				Image BPP
								BPP may be 1, 2, 4, 8, 16, or 24.
								BPP > 8 implies non-indexed color
	uint8_t			compressType;			image data compression type
								0 - No compression
								1 - RLE
								2 - LZW
								3 - Huffman
	uint8_t			hardwarePlatform;		Specifies the hardware format
								this image data and palette
								data is stored as.
								( See below )
} EIAHeader;
```

### Compression Type
EIA image data may be compressed in one of three ways: Run-Length Encoding
(RLE), Liv-Zempel-Welch (LZW), or a Huffman tree. An uncompressed image is
stored as type 00, and may be loaded directly into your video hardware
depending on the Hardware Platform flag (see below).

Consequently, if the image is compressed, it must first be uncompressed
before being loaded into your video display hardware (unless of course, your
video display hardware can perform the uncompression!)

#### Hardware Platform
The Hardware Platform specifies the format of this image data. After
decompression, the specified image data is directly loadable into
the video display hardware of your implementation. For the purpose
of cross-compatible image loaders, a standard table of supported
video display hardware is maintained.

EIA also mandates a standard format known as EIA Stream. EIA Stream
is a simple byte stream of pixels. For BPP levels of 8 and below, an
EIA stream is a simple array of numbers (packed at the level of the bits
per pixel). For BPP levels greater than 8, RGB values are directly
specified in an array. File types of EIA Stream have Hardware Platform 01.
EIA Stream files are intended for cross-system compatibility, or displaying
images on embedded platforms that first require any operations such as
quantization.

A Hardware Platform of 00 means that this EIA file is intended for an
undocumented platform. All Hardware Platform IDs are reserved; if your
EIA is for a platform not listed in the table below, you must use type 00.


| ID | HardwarePlatform |
|----|------------------|
| 00 | Undefined/custom |
| 01 | EIA Stream	|
| 02 | Sega Megadrive   |

The selected Hardware Platform also has implications for how your EPAL
color table is stored (see below).

## EPLO
The EPLO chunk defines options specific to the selected Hardware Platform.
Therefore, its contents are dependent on the Hardware Platform selected.

### 00 - Undefined/Custom
The EPLO options are implementation-specific. If your implementation does not
implement Hardware Platform 00, this EPLO chunk is unusable.

### 01 - EIA Stream
There are no additional options required for the EIA Stream platform. The EPLO
will be ignored for this Hardware Platform.

### 02 - Sega Megadrive
The Sega Megadrive allows you to specify whether or not this image asset
is laid out in row-major order (tiles) or column-major order (sprites).
It consists of a single uint8_t, where 00 is row-major order and 01 is
tile-major.

## EPAL
The EPAL is the color palette for your image. An EPAL is provided for all images
that have a BPP of 8 or less.

Like the EIMG, the EPAL is provided in a format directly usable by your video
hardware of choice. Therefore, the format of the EPAL depends directly on
the Hardware Platform flag provided in the EMHD.

### EPAL Formats

#### 00 - Undefined/Custom
This color palette is in an undefined format. Only the specific implementation
knows how to use this flag. If your encoder does not implement type 00, the
image palette (as well as the image itself) cannot be used. Color palettes of
type 00 are not compatible with other decoders.

#### 01 - EIA Stream
An EIA Stream palette is a simple list of 24-bit RGB triplets. The first one
is palette entry 0, the second is 1, etc.

The EPAL will be ignored if the EIA Stream image is greater
than 8 bits per pixel.

#### 02 - Sega Megadrive
The Sega Megadrive VDP stores four color tables as an array of 16 uint16_t
values in the format 0BGR. The EPAL for a Sega Megadrive will therefore
be provided as sixteen uint16_t values, in this format.

## EIMG
The EIMG block is the raw image data. Depending on the mode of compression
and your hardware platform, this image may be directly loadable into your GPU.

### Compression
If your hardware platform does not support hardware compression, you must
decompress the EIMG before loading it into your hardware. EIA supports three
modes of compression: RLE, LZW, and Huffman.

### Hardware Platforms

#### 00 - Undefined/Custom
This EIMG is handled depending on how your loader has implemented type 00.
If your loader doesn't or cannot implement type 00, this image cannot be
displayed. Images of type 00 are not intended to be shared across platforms.

#### 01 - EIA Stream
An EIA Stream is stored as a simple array of values depending on your bits
per pixel. Every image begins at 0,0 and is stored as a simple array which
progresses in the pattern 0 to width, then 0 to height.

1bpp - Eight pixels are packed in a single byte.
2bpp - Four pixels are packed in a single byte.
4bpp - Two pixels are packed in a single byte.
8bpp - This byte represents one pixel.

For images of 16 bpp, each pixel is specified as an unsigned 16-bit integer
in the format RGGB.

For images of 24 bpp, each pixel is specified as an RGB triplet in the form
RR GG BB.

#### 02 - Sega Megadrive
The Sega Megadrive VDP supports images in either row-major order or column-major
order, depending on the EPLO option. This does not impact how tiles are loaded
into the VDP; rather, the EPLO option is provided as a flag.

The image data should be interpreted as a list of unsigned 32-bit integers.
Each nibble in each unsigned 32-bit integer is a pixel. Images are organized
in 8x8 "tiles", each representing an 8x8 segment of the image.
