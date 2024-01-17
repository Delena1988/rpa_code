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
print('------------------------')

tree = ET.parse('lab2.xml')
root = tree.getroot()
itemList = root.find('Items').findall('Item')

for item in root.find('Items').iter('Item'):
   if item.find('PATIENT_NAME') != None:
      print(item.find('PATIENT_NAME').text)
   if item.find('INPATIENT_ID') != None:
      print(item.find('INPATIENT_ID').text)
   if item.find('CHECK_TIME') != None:
      print(item.find('CHECK_TIME').text)
   if item.find('INSPECTION_ID') != None:
      print(item.find('INSPECTION_ID').text)
   if item.find('TEST_ORDER_NAME') != None:
      print(item.find('TEST_ORDER_NAME').text)
   if item.find('QUANTITATIVE_RESULT') != None:
      print(item.find('QUANTITATIVE_RESULT').text)
   if item.find('TEST_ITEM_ID') != None:
      print(item.find('TEST_ITEM_ID').text)
   if item.find('CHINESE_NAME') != None:
      print(item.find('CHINESE_NAME').text)
   if item.find('TEST_ITEM_UNIT') != None:
      print(item.find('TEST_ITEM_UNIT').text)
   if item.find('TEST_ITEM_REFERENCE') != None:
      print(item.find('TEST_ITEM_REFERENCE').text)
   if item.find('QUALITATIVE_RESULT') != None:
      print(item.find('QUALITATIVE_RESULT').text)
   print()
