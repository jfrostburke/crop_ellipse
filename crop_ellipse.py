import numpy as np
from astropy.io import fits
from astropy.modeling.models import Ellipse2D

(x_0, y_0) = (1000., 2500.)  # Center of ellipse, pixel coords
(a, b) = (500., 300.)  # Major and minor axes of ellipse, pixel coords
theta = np.pi/4  # Orientation of ellipse, radians
ellipse = Ellipse2D(amplitude=1., x_0=x_0, y_0=y_0,
                    a=a, b=b, theta=theta) 

img_filename = 'elp1m008-fl05-20170101-0119-e91.fits'  # Example image I had access to
with fits.open(img_filename) as hdul:

    data = hdul[0].data
    y, x = np.mgrid[0:data.shape[0], 0:data.shape[1]]
    ellipse_mask = ellipse(x, y).astype(bool)
    cropped_data = np.where(ellipse_mask, data, np.nan)
    hdul[0].data = cropped_data
    hdul.writeto('cropped_image.fits')

