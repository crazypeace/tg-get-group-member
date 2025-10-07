# tg-get-group-member
Telegram 查询群组成员

<img width="699" height="293" alt="image" src="https://github.com/user-attachments/assets/d19320b5-ef33-4816-a96b-45f9efbedafd" />


api_id, api_hash 需要自己申请  
https://my.telegram.org/apps  
具体步骤不写了, 自己去问 google 和 gpt  


## 搭环境
```
apt install -y python3-pip
pip3 install telethon pyyaml --break-system-packages
```

## 运行
```
python3 tg-get-group-member.py
```

## 运行结果示例
```
正在获取群组成员列表: FuckGFW-Newbie 翻墙新手村
跳过Exceptions列表中的用户 ID: 816194782
跳过Exceptions列表中的用户 ID: 6521155977
...略

--- 群组成员列表 ---
6617181826:
  username: atefatman
  full_name: 子 肥
7919966027:
  username: crazypeace_anti_bot_bot
  full_name: CZ_antibot_bot
...略

✅ 共获取 1216 名成员
📄 已保存到文件: members_1517821953.yaml
```

## 注意
因为我自己的理解, 跳过了 Exceptions 里面的用户.

<img width="480" height="158" alt="2025-10-07_21-09-42" src="https://github.com/user-attachments/assets/9ee8645d-85ec-4575-b716-69b9d1443446" />

如果你有自己的需要, 可以屏蔽掉这个判断, 这样得到所有的群成员.
