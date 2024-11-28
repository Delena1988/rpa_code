import jieba
import pandas as pd

text = "现病史：患者1月余来无明显诱因下出现声音嘶哑，无咽痛，无吞咽不适，无发热畏寒，无恶心呕吐，无咳嗽咳痰，无胸闷气促，无心慌心悸等不适。在劳累及大声讲话后声嘶加重，休息后不能缓解，呈持续性，遂至我院就诊行喉镜检查示“双侧声带水肿，左侧声带新生物”。予以对症处理后未见好转，现患者为求进一步治疗，门诊拟“声带肿物”收住入院。" \
       "发病来，神志清，精神可，饮食及睡眠治疗可，二便无殊，近期体重无明显增减。" \
       "患有“2型糖尿病”病史1年余，平素服用“西格列汀二甲双胍片1片 BID”降糖。" \
       "患者既往曾于10余年前在宁波医院行声带手术（具体不详），术后恢复尚可，偶有声嘶，休息后能缓解。"

arr = []
a = text.split("。")
for tmp in a:
    b = tmp.split("；")
    for tmp in b:
        c = tmp.split("，")
        arr = arr + c
#
# for tmp in arr:
#     print(tmp)
#     seg_list = jieba.cut(tmp, cut_all=False)
#     # print(seg_list)
#     print("/ ".join(seg_list))  # 精确模式
