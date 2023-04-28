from PIL import Image
from pdf2image import convert_from_path

pdf_path = "/Users/linjian/Downloads/RPA_PIC/2023-04-19_黄兴贵_03240061.pdf"
output_image_path = "/Users/linjian/Downloads/RPA_PIC/2023-04-19_黄兴贵_03240061.jpg"

# 将PDF文件转换为图像列表
image_list = convert_from_path(pdf_path)

# 获取第一个图像的尺寸
page_width, page_height = image_list[0].size

# 创建一个与所有图像大小相同的画布
merged_image = Image.new("RGB", (page_width, page_height * len(image_list)), (255, 255, 255))

# 将所有图像粘贴到画布上
for i, image in enumerate(image_list):
    merged_image.paste(image, (0, i * page_height))

# 将画布保存为一张长图
merged_image.save(output_image_path)