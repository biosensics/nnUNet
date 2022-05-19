import os
import shutil
from os import listdir
from os.path import isfile, join
import nibabel as nib
import numpy as np
import SimpleITK as sitk
import random

# root_adrs = 'nnunet_folders\\nnUNet_raw_data_base\\nnUNet_raw_data\\Task401_1000CTs/labelsTr'
# tr_seg_files = [f for f in listdir(root_adrs)]
#
# for f in tr_seg_files:
#     print(f)
#     file = nib.load(os.path.join(root_adrs, f))
#     hd = file.header
#
#     seg_ar = np.copy(file.get_data())
#     seg_ar[seg_ar != 2] = 0
#     seg_ar[seg_ar > 0] = 1
#     seg_ar = seg_ar.astype(np.uint8)
#
#     new_file = nib.Nifti1Image(seg_ar, file.affine, header=hd)
#     new_file.set_data_dtype(np.uint8)
#     nib.save(new_file, os.path.join(root_adrs, f))
#
# print('Done')

split_name = 'labelsTr'
root_adrs = 'nnunet_folders\\nnUNet_raw_data_base\\nnUNet_raw_data\\Task401_1000CTs'
target_adrs = 'nnunet_folders\\nnUNet_raw_data_base\\nnUNet_raw_data\\Task501_250CTs'
file_list = [f for f in listdir(os.path.join(root_adrs, 'labelsTr'))][0:883]
file_list = random.sample(file_list, 250)

for f in file_list:
    print(f)
    shutil.move(os.path.join(root_adrs, 'labelsTr',f), os.path.join(target_adrs, 'labelsTr', f))
    shutil.move(os.path.join(root_adrs, 'imagesTr', f.replace('.nii.gz', '_0000.nii.gz')),
                os.path.join(target_adrs, 'imagesTr', f.replace('.nii.gz', '_0000.nii.gz')))
print('Done')
