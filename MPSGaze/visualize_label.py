import cv2
import numpy as np

def draw_arrow(image_in, pitchyaw, center, length, thickness=2, color=(0, 0, 0)):
    image_out = image_in.copy()
    pos = (int(center[0]), int(center[1]))
    dx = -length * np.sin(pitchyaw[1]) * np.cos(pitchyaw[0])
    dy = -length * np.sin(pitchyaw[0])

    cv2.circle(image_out,pos,int(length),color,2)
    cv2.arrowedLine(image_out, tuple(np.round(pos).astype(np.int32)), tuple(np.round([pos[0] + dx, pos[1] + dy]).astype(int)), color, thickness, cv2.LINE_AA, tipLength=0.2)
    return image_out

def draw_everything(input_img, label_list, show_text=False, show_gaze=True,show_landms=True):
    img_gaze = input_img.copy()
    img_head = input_img.copy()
    for label in label_list:
        for i in range(len(label)):
            label[i] = float(label[i])

        le = np.maximum(label[2],label[3])/2
        img_gaze = draw_arrow(img_gaze,(label[-5],label[-4]),center=(label[0]+label[2]/2.,label[1]+label[3]/2.),length=le,color=(0, 0, 255))
        img_head = draw_arrow(img_head,(label[-3],label[-2]),center=(label[0]+label[2]/2.,label[1]+label[3]/2.),length=le,color=(0, 255, 0))
    cv2.imwrite('./vis_gaze.jpg',img_gaze)
    # cv2.imwrite('./vis_head.jpg',img_head)

im_addr = './0_Parade_Parade_0_364.jpg'
label_txt_addr = './label_eg.txt'

im = cv2.imread(im_addr)
label_list = []
with open(label_txt_addr,'r') as f:
    lines = f.readlines()
for line in lines[1:]:
    label_list.append(line.split())
draw_everything(im,label_list)