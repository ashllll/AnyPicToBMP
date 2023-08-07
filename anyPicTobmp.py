import os
from PIL import Image

def convert_to_bmp(source_path):
    target_path = os.path.dirname(source_path)
    if not os.path.exists(os.path.join(target_path, 'bmp')):
        os.makedirs(os.path.join(target_path, 'bmp'))
    for root, dirs, files in os.walk(source_path):
        for name in files:
            ext = os.path.splitext(name)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
                target_filename = os.path.splitext(name)[0] + '.bmp'
                img = Image.open(os.path.join(root, name))
                img.save(os.path.join(target_path, 'bmp', target_filename))

if __name__ == '__main__':
    source_path = input('请输入要转换的图片所在目录：')
    convert_to_bmp(source_path)
    print('图片转换完成！')
