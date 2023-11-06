# Images
## Vector graphic images
Vector images are created with a drawing-package or a computer aided design (CAF) package each component is an individual drawing object. The image is then stored as a vector graphic file. Each file contains a "Drawing list" command list consisting of the "commands", these commands are for each object in the image.  The commands have "attributes" these attributes are needed to make the "properties" of the object. The most important vector property is the dimensions of the object. The image is scalable. 
*Note: vector images cannot be made without a graph plotter thus are usually made into bitmap*
## Bitmap images
Is made up of pixels (picture elements) it is the smallest identifiable part of a bitmap image. The image is stored a two-dimensional matrix. Each pixel has a position and a colour. The color scheme needs to be defined.  The number of bits used per pixel is called "Colour Depth/Bit Depth". Bit depth is best defined as amount of R, G & B in RGB. A colour depth of 8 bits can represent up to 256 different colours. Whereas bit depth of 8 bits is 256 * 256 * 256 = 16777216 unique colours. 
The image resolution is defined in the bitmap file. A bitmap file contains the colour to define resolution and colour depth


| Vector                             | Bitmap                                          |     |
| ---------------------------------- | ----------------------------------------------- | --- |
| used by engineers                  | directly produced by camera                     |     |
| Neds to convert to bitmap to print | The choice to insert into documents or webpages |     |
|                                    |                                                 |     |

# Sound 
Needs 2 major components to store:
1. *Sampling resolution* (stores amplitude of sound)
	- if too few are used then there will be error in the sampling of the sound
	- the industry average is a16 bits, which provides reasonable quality
2. *Sampling rate*
	- Number on samples per second


# File size calc 
### for images
(resolution * Colour Depth<sub>)/(8 * 1024<sup>n</sup>)</sub> if n is 1 then kibibyte if 2 then mebibyte 
***note bit depth * 3 can also be used***
## for sound 
(resolution * rate) if n is 1 then kibibyte if 2 then mebibyte 

# Compression 
| lossy                                   | lossless                                                                  |
| --------------------------------------- | ------------------------------------------------------------------------- |
| Reduced size but details are lost       | Reduced size but no permanent changes                                     |
| Removes details humans cannot notice    | RLE: run length encoding, converts sequences to (value,number of repeats) |
| Reduce colour depth/sampling resolution | RLE works well with bitmaps                                               |














