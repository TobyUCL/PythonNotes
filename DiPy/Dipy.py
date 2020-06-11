import numpy as np
import nibabel as nib
import dipy.reconst.dti as dti
from dipy.data import read_stanford_hardi

img, gtab = read_stanford_hardi()

data = img.get_data()
print('data.shape (%d, %d, %d, %d)' % data.shape)

from dipy.segment.mask import median_otsu

maskdata, mask = median_otsu(data, vol_idx=range(10, 50), median_radius=3, numpass=1, autocrop=True, dilate=2)

print('maskdata.shape (%d, %d, %d, %d)' % maskdata.shape)

print("Done")
