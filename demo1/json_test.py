import json
# json
json_dict = {
    "data": {
        "usre_list": [
            {
                "id": 1,
                "us_name": "张来博"
            },
            {
                "id": 2,
                "us_name": "柳梦强"
            }
        ]
    }
}
print(json_dict)

print("\n\n")
# 转换为json数据
json_str = json.dumps(json_dict)
print(json_str)


# json 转换为 字典
print(json.loads(json_str))
