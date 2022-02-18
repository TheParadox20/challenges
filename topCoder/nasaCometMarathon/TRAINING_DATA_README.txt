-=-=-=-=-= INFORMATION ABOUT THE SOHO COMET TRAINING DATASET =-=-=-=-=-

Each provided subdirectory corresponds to a single set of SOHO/LASCO observations of a comet. Specifically, we provide a plain text .txt file that provides the necessary metadata about the comet, and the set of "FITS" formatted science data files in which the comet is observed. Details of each are as below. Each comet is assigned a random four-digit identifier, and labeled as cmt0001 through cmt2000, with subdirectories and the plain text metadata files named accordingly.

-=-=-=-=-= PLAIN TEXT METADATA FILES =-=-=-=-=-

An example file contents looks as follows:
# Comet ID: cmt1234
# Comet Group: Kreutz
# Brightness Category: C
# Number Measurements: 9
#      DATE     TIME     FILENAME       X       Y  VMAG
 2018-10-03 02:24:06 22697473.fts   15.00  904.00  7.50
 2018-10-03 02:36:05 22697474.fts   29.00  894.00  8.20
 2018-10-03 02:48:05 22697475.fts   42.00  884.00  8.40
 2018-10-03 03:12:11 22697479.fts   68.00  865.00  8.20
 2018-10-03 03:24:05 22697480.fts   80.00  854.00  8.50
 2018-10-03 03:36:05 22697481.fts   95.00  845.00  8.90
 2018-10-03 03:48:05 22697482.fts  111.00  833.00 10.60
 2018-10-03 04:00:05 22697483.fts  124.00  823.00 10.20
 2018-10-03 04:12:05 22697484.fts  135.00  815.00  8.90

i. The first line is the randomly assigned comet identifier, e.g. cmt1234.
ii. The second line provides the grouping to which the comet belongs. The SOHO comets fall into five groupings: Kreutz, Meyer, Marsden, Kracht, KrachtII, and Non-group. The first five of these are comet families -- that is, the comets of these groups all follow a very similar orbit through space. The six grouping - Non-group - encompasses all SOHO comets that do not appear to be related to any known comet family or population. Approximately 85% of the comets provided belong to the Kreutz family, which is the dominant source of SOHO comet discoveries.
iii. The third line provides the Brightness category of the comet, A, B or C, with C being the faintest. This category is determined from the physical brightness (visual magnitude, or VMAG) of the comet in the data, which is recorded for every observation. As noted below, many comets emerge from the background noise (i.e. very faint), and then brighten to some extent before fading again. Thus, we use the median of the five brightest observation points to determine the overall brightness category for the comet.
iv. Number of Measurements provides the number of individual observations provided for a given comet. Most data sets have 5 - 15 observations, but a small number have over 40. Many have less than 5 observations - please see the "MISC NOTE #1" below regarding this.
v. The fifth line is the header column for the date/time/position/VMAG of the comet.

The remaining lines in the file provide the date/time/position/VMAG of the comet. The date and time correspond to the actual date and time of the data files, with the filename column providing the correspond FITS file name. The X and Y values provide the recorded x,y pixel location of the assumed comet center. It is important to note that this value may be approximate (+/- 5 pixels) for extremely faint and diffuse comets. The extremely bright "cmt0030" may be a good target to visually validate that models are extracting the correct portion of the data array from the FITS files.

The VMAG column provides the estimated visual magnitude of the comet, based on the standard astronomical visual magnitude scale. Again, it must be noted that any VMAG below approximately 9.0 is effectively instrument noise level or below, and thus the error bars on the VMAG estimate become substantial. In some cases, the VMAG may be listed as NAN, indicating that our algorithm was unable to obtain any reasonable estimate for the comet VMAG. In most cases this is because the comet is too faint, though in sporadic cases it can be as a result of defects in the data files, cosmic ray noise in the data, or some other sporadic event. Comet brightnesses should generally follow a relatively consistent trend, so any erratic changes in VMAG should be treated with caution.

 -=-=-=-=-= FITS FORMAT DATA FILES =-=-=-=-=-

We provide data files in the standard astronomical Flexible Image Transport System (FITS) data format. A FITS file can be considered to be an image file, nominally of 1024x1024 pixels, and an associated metadata "header" which contains a number of metadata parameters about that image, including date, time, dimensions, exposure time, and other miscellaneous properties. We suggest normalizing all images by the exposure time (EXPTIME) value provided in the header, as there are sometimes variations in exposure that can affect the apparent brightness of a comet.

A number of software tools provide interfaces to FITS data format, with the python-based AstroPy a particularly popular choice. Normalizing a FITS would look something like the following.
>>> from astropy.io import fits
>>> image, header = fits.getdata( 'filename.fts', header=True)
>>> image_norm = image / header['EXPTIME']

-=-=-=-=-= MISC NOTES =-=-=-=-=-

#1. For a comet to be deemed as "real" (versus simply being instrument noise of some kind), we must be able to track the object in at least five consecutive images. In this data archive, we do provide examples of comets with less than five consecutive images as we happen to know from other data sources that these particular observations are indeed real comets. Thus, we provide these observations here in case they are useful for training algorithms. However, algorithms should not base their evaluation against comets with less than five observations.

#2. An important consideration is that SOHO comets are not uniform in morphology. Some may be large and bright with very long, bright tails (e.g., "cmt1256"), while others are small, faint, and diffuse in appearance (e.g. "cmt1234"), and others may be stellar and bright in appearance (e.g., "cmt0716"). However, individual comets are largely very self-consistent in morphology. That is, a comet will not abruptly grow/lost a long tail, will not alternate between bright/stellar and faint/diffuse, etc. Changes in morphology happen over the span of hours or more.

#3. A related consideration should be that comets must obey the laws of physics in terms of their motion. That is, they move in near-perfect straight lines over short distances and time durations. A very slight curvature may be noted in the trajectory of some comets seen over a long observing window, but most follow an approximate straight line. Similarly, their velocity - either in physical units or in pixels-per-second - will be a somewhat consistent value, though many will exhibit a steady acceleration as they near the Sun, and a steady decelerate as they recede.
