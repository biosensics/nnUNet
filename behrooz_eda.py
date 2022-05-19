from collections import OrderedDict
import os
import shutil
from os import listdir
from os.path import isfile, join
import nibabel as nib
import numpy as np
import SimpleITK as sitk
import pandas as pd

root_adrs = 'nnunet_folders\\nnUNet_raw_data_base\\' \
            'nnUNet_raw_data\Task777_1000CTs\\labelsTr'
tr_seg_files = [f for f in listdir(root_adrs)]

# prop_dic = OrderedDict()
# for file in tr_seg_files:
#     try:
#         print(file)
#         case_dic = {}
#         adrs = os.path.join(root_adrs, file)
#         case_dic['case_address'] = adrs
#         img_nib = nib.load(adrs)
#         case_dic['nib_size'] = img_nib.shape
#         case_dic['nib_space'] = img_nib.affine[(0, 1, 2), (0, 1, 2)]
#         case_dic['orientation'] = nib.aff2axcodes(img_nib.affine)
#
#         img_sitk = sitk.ReadImage(adrs)
#         case_dic['sitk_size'] = img_sitk.GetSize()
#         case_dic['sitk_space'] = img_sitk.GetSpacing()
#         prop_dic[file] = case_dic
#     except Exception as e:
#         print('!' * 60)
#         print(e)
#
# df = pd.DataFrame.from_dict(prop_dic, orient='index')
# df.to_csv('nifti_eda_test.csv')


prop_dic = OrderedDict()
for file in tr_seg_files:
    try:
        print(file)
        case_dic = {}
        adrs = os.path.join(root_adrs, file)
        case_dic['case_address'] = adrs
        img_nib = nib.load(adrs)
        seg = np.array(img_nib)
        case_dic['nib_size'] = img_nib.shape
        case_dic['nib_space'] = img_nib.affine[(0, 1, 2), (0, 1, 2)]
        case_dic['orientation'] = nib.aff2axcodes(img_nib.affine)

        img_sitk = sitk.ReadImage(adrs)
        case_dic['sitk_size'] = img_sitk.GetSize()
        case_dic['sitk_space'] = img_sitk.GetSpacing()
        prop_dic[file] = case_dic
    except Exception as e:
        print('!' * 60)
        print(e)

df = pd.DataFrame.from_dict(prop_dic, orient='index')
df.to_csv('nifti_eda_test.csv')