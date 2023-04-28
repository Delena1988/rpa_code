import requests
from requests_toolbelt import MultipartEncoder
# import os

file_path = '/Users/linjian/Downloads/RPA_PIC/2023-04-04_王兴水_03239184.pdf'
request_url='http://192.168.3.67:3109/hug_interview/manage/file/rpa-file-upload.mvc'
filename = file_path.split("\\")[-1:][0]
# total_size = os.path.getsize(file_path)

data = MultipartEncoder(
    fields={
        "filename": filename,
        # "totalSize": str(total_size),
        "fileName": (filename, open(file_path, 'rb'), 'application/octet-stream')
    }
)

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Content-Type": data.content_type
}

response = requests.post(request_url, headers=headers, data=data)
print(response.text)