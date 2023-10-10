import json
import os
# import cv2
# import requests
# import numpy as np
# import matplotlib.pyplot as plt
def read_dataset(root = '/data/pjc/data', dataset_name='coco', split = 'train', img_id = 12345):
    if dataset_name == 'coco':
        ann_path = os.path.join(root +'/'+ dataset_name, 'annotations')
        # print(ann_path)
        ann_file_name = 'captions_' + split + '2014.json'
        path = os.path.join(ann_path,ann_file_name)
        # print(path)
        dataset = json.load(open(path))
        ann_images = []
        ann_annotations = []
        for img in dataset["images"]:
            if img['id'] == img_id:
                ann_images = img
        for ann in dataset["annotations"]:
            if ann['image_id'] == img_id:
                ann_annotations.append(ann)
        print('image_id: {}'.format(ann_images['id']))
        print('file_name: {}'.format(ann_images['file_name']))
        print('coco_url: {}'.format(ann_images['coco_url']))
        print('flickr_url: {}'.format(ann_images['flickr_url']))
        d = 0
        for aa in ann_annotations:
            d += 1
            print('caption_{}: {}'.format(d, aa['caption']))
        # img_path = os.path.join(root +'/'+ dataset_name, 'images')
        # img_file_name = os.path.join(img_path + '/' + split + '2014', ann_images['file_name'])
        # # print(img_file_name)
        # service_img = cv2.imread(img_file_name)
        # # print(image_.shape)
        # # 保存本地
        # loacl_path = './img_cache/'
        # if not os.path.exists(loacl_path):
        #     os.system(r"mkdir {}".format(loacl_path))  # 调用系统命令行来创建文件
        # cv2.imwrite(loacl_path + ann_images['file_name'], service_img)
        # loacal_img = cv2.imread(loacl_path)
        # # 显示图像
        # cv2.namedWindow(dataset_name + "image")  # 创建一个image的窗口
        # cv2.imshow(ann_images['file_name'], loacal_img)  # 显示图像
        # cv2.waitKey()  # 默认为0，无限等待
        # cv2.destroyAllWindows()
        # try:
        #     img_url = ann_images['coco_url']
        #     img_data = requests.get(img_url).content
        #     img = np.asarray(bytearray(img_data), dtype="uint8")
        #     # img = cv2.imdecode(img, -1)
        #     # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        #     image = cv2.imdecode(img, cv2.IMREAD_COLOR)
        #     cv2.imshow('url_image_show', image)
        #     if cv2.waitKey(10000) & 0xFF == ord('q'):
        #         cv2.destroyAllWindows()
        # except Exception as e:
        #     print(f'download image {img_url} error: {e}')

    elif dataset_name == 'flick':
        pass
    else:
        print('Error dataset name')

def get_img_id(root = '/data/pjc/data_bbox', dataset_name = 'coco', split = 'train', rank = 0):
    file_name = split + '_ids.txt'
    data_path = os.path.join(root + '/'+ dataset_name+'_precomp', file_name)
    # print(data_path)
    with open(data_path, encoding='utf-8') as file:
        content = file.readlines()
    return int(content[rank])


if __name__ == "__main__":
    # coco or flick dataset
    # ch = input("----------please enter 1 or 2----------\n------1 => rank   2 => image id ------\n")
    # if ch == '1':
    #     rank = int(input("Please enter the number of images you want to query in the data set: \n"))
    #     img_id = get_img_id(root = '/data/pjc/CMR-Pro/data', dataset_name = 'coco', split = 'train',rank = rank-1)
    #     read_dataset(root='/data/pjc/data', dataset_name='coco', split='train', img_id = img_id)
    # elif ch == '2':
    #     img_id = int(input("Please enter thr image id of images: \n"))
    #     read_dataset(root='/data/pjc/data', dataset_name='coco', split='train', img_id=img_id)
    # else:
    #     print("Wrong input")
    rank = int(input("Please enter the number of images you want to query in the data set: \n"))
    img_id = get_img_id(root='/data/pjc/CMR-Pro/data', dataset_name='coco', split='train', rank=rank - 1)
    read_dataset(root='/data/pjc/data', dataset_name='coco', split='train', img_id=img_id)