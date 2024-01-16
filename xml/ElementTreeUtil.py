from xml.etree import ElementTree as ET

# 直接读取xml文件，形成ElementTree结构
tree = ET.parse('lab1.xml')
# 获取root tag
root = tree.getroot()

# 打印root的tag
print(root.tag)
# 打印root的attrib
print(root.attrib)
# 使用root索引访问标签的值，[0]是R1标签，[0]是R1标签中的第一个标签device_type, .text是取这个标签的值，自然值就是cisco_ios
print(root[0][0].text)
print('\n')
# 打印root的child层的tag和attrib
for child in root:
   print(child.tag, child.attrib)

# 查找find()
print(root.find('R1'))

