import cv2
import os

from imaging_interview import(
preprocess_image_change_detection,
compare_frames_change_detection)

img_list = os.listdir(r'20_c')
unique_img_list = []
original_length= len(img_list)

while len(img_list)!=0:
    # print(len(img_list))
    img_path_1 = img_list[0]
    unique_img_list.append(img_path_1)
    
    img_1 = cv2.imread(os.path.join('c23',img_path_1))
    gray_1 = preprocess_image_change_detection(img_1,gaussian_blur_radius_list=[1,3,5,7],black_mask=[4,25,4,0])

    img_list = img_list[1:]
    temp_list =[]

    for img_path_2 in img_list:
        img_2  = cv2.imread(os.path.join('c23',img_path_2))
        gray_2 = preprocess_image_change_detection(img_2,gaussian_blur_radius_list=[1,3,5,7],black_mask=[4,25,4,0])

        score,res_cnts,thresh = compare_frames_change_detection(
                                    gray_1,gray_2,min_contour_area=3000)
        if score>6000:
            temp_list.append(img_path_2)
    img_list=temp_list


print(f"Total number of frames : {original_length}, Number of unique frames : {len(unique_img_list)}, Number of duplicates : {original_length-len(unique_img_list)}")

# try:
#     os.makedirs(r'unique_pics')
# except:pass

# for u_img in unique_img_list:
#     img =cv2.imread(os.path.join('c23',u_img))
#     cv2.imwrite(os.path.join('unique_pics',u_img),img)








