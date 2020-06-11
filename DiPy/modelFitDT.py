"""
Preform a model fit on DWI data to get the DT
"""

import numpy as np
import dipy.reconst.dti as dti
import dipy.data as dpd
from dipy.io.image import load_nifti, save_nifti
from dipy.io.gradients import read_bvals_bvecs
from dipy.core.gradients import gradient_table
from dipy.viz import window, actor
import matplotlib.pyplot as plt

# Enables/disables interactive visualization
interactive = False

"""
get example data to perform the fit on
"""
hardi_fname, hardi_bval_fname, hardi_bvec_fname = dpd.get_fnames('stanford_hardi')
# data is a numpy array which contains the DWI signal, affine is the local orientation
data, affine = load_nifti(hardi_fname)
# reduce the DWI to only a small region to make this example more efficient
roi_idx = (slice(20, 50), slice(55, 85), slice(38, 39)) 
data = data[roi_idx]

# bvals and bvecs are numpy arrays
bvals, bvecs = read_bvals_bvecs(hardi_bval_fname, hardi_bvec_fname)


"""
Performing the fit
"""
# convert the bvecs and bvals into a gradient table
gtab = gradient_table(bvals, bvecs)

# initialize a DTI model class instance using the gradient table used in the measurement
dti_wls = dti.TensorModel(gtab)

# Perform the model-fit, the default algorithm is weigthed least squares from Chang2005 
fit_wls = dti_wls.fit(data)


"""
Accessing the DT

The diffusion tensor is now stored in the fit_wls class, along with the:
    FA
    MD
    evecs
    evals
    and others
"""

diffusion_tensor_values = fit_wls.lower_triangular()
fa1 = fit_wls.fa
evals1 = fit_wls.evals
evecs1 = fit_wls.evecs
cfa1 = dti.color_fa(fa1, evecs1)
sphere = dpd.default_sphere
"""
ren = window.Renderer()
ren.add(actor.tensor_slicer(evals1, evecs1, scalar_colors=cfa1, sphere=sphere,
                            scale=0.3))
print('Saving illustration as tensor_ellipsoids_wls.png')
window.record(ren, out_path='tensor_ellipsoids_wls.png', size=(600, 600))
if interactive:
    window.show(ren)
"""



"""
Experiment how the WLS fit performs when given B0 normalized data 

First create a new model fit when only 1 b0 is given.
Next normalise the b2000s by the one b0, enter [1,1,1,1,...,1] for the b0 image.
"""
last_b0_idx = 9
bvals_1b0 = bvals[last_b0_idx:]
bvecs_1b0 = bvecs[last_b0_idx:]
data_1b0 = data[:,:,:,last_b0_idx:]

# convert the bvecs and bvals into a gradient table
gtab_1b0 = gradient_table(bvals_1b0, bvecs_1b0)

# initialize a DTI model class instance using the gradient table used in the measurement
dti_wls_1b0 = dti.TensorModel(gtab_1b0)

# Perform the model-fit, the default algorithm is weigthed least squares from Chang2005 
fit_wls_1b0 = dti_wls_1b0.fit(data_1b0)

diffusion_tensor_values_1b0 = fit_wls_1b0.lower_triangular()
fa1_1b0 = fit_wls_1b0.fa
evals1_1b0 = fit_wls_1b0.evals
evecs1_1b0 = fit_wls_1b0.evecs

# look at the difference between these two predictions, we expect there to be some small differnce between the two, if they are identitcal then we should be suspicious
fa_rel_err = fa_diff = (fa1 - fa1_1b0)/fa1
mean_fa_rel_err = np.mean(fa_rel_err) # this is very low

"""
Now create the b0 normalised image

first divide the b2000 image by the b0 image
then define a new b0 image for the model fit, it is a matrix of 1s.
then do the model fit
"""
b0_img = data_1b0[:,:,:,0].copy()
b2000_img = data_1b0[:,:,:,1:].copy()

norm_b2000_img = np.zeros(b2000_img.shape)
for i in range(b2000_img.shape[-1]):
    a_DWI_norm = b2000_img[:,:,:,i]/b0_img
    norm_b2000_img[:,:,:,i] = a_DWI_norm.copy() 

# create the 'normed' b0 image this has shape [30,30,1,1]
norm_b0 = np.ones(b2000_img[:,:,:,:1].shape )

# thus concatenate the two sets
data_b0Normed = np.concatenate((norm_b0, norm_b2000_img),axis=3)

## Now perform the model fit
# initialize a DTI model class instance using the gradient table used in the measurement
dti_wls_b0Normed = dti.TensorModel(gtab_1b0)

# Perform the model-fit, the default algorithm is weigthed least squares from Chang2005 
fit_wls_b0Normed = dti_wls_b0Normed.fit(data_b0Normed)

diffusion_tensor_values_b0Normed = fit_wls_b0Normed.lower_triangular()
fa1_b0Normed = fit_wls_b0Normed.fa
evals1_b0Normed = fit_wls_b0Normed.evals
evecs1_b0Normed = fit_wls_b0Normed.evecs

"""
Now to compare the b0 norm, and not normed, FA values
"""
fa_norm_notNorm_diff = fa1_b0Normed-fa1_1b0 # as you can see it is the same up to tiny (~-12) computational error 
