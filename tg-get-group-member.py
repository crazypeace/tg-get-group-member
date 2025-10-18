from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantBanned
import yaml

# 到这里申请 https://my.telegram.org/apps
api_id = 12345678
api_hash = 'f9847f9847f9847f9847f9847f984747'

# 群组的 username 或 ID
group = -100xxxxxxxxxx #私有群是负整数
#group = 'groupusername' #公开群的username字符串

# 登录的用户的手机号
phone_number = '+8613812345678'


client = TelegramClient('session_' + phone_number, api_id, api_hash)

async def main():
    await client.start(phone=phone_number)

    # 获取群实体
    entity = await client.get_entity(group)

    print(f"正在获取群组成员列表: {entity.title}")

    # 统计用户信息
    data = {}

    # 获得群组中的成员
    async for m in client.iter_participants(entity, limit=None):
        # 过滤逻辑：如果用户在 Permissions 里面的 Exceptions 列表里面，则跳过
        if isinstance(m.participant, ChannelParticipantBanned):
            print(f"跳过Exceptions列表中的用户 ID: {m.id}") # 可选的调试信息
            continue
        
        # 获取加入时间（如果有）
        joined_at = getattr(m.participant, 'date', None)
        joined_at_str = joined_at.isoformat() if joined_at else None
        
        data[m.id] = {
            'username': m.username or '',
            'full_name': f"{m.first_name or ''} {m.last_name or ''}".strip(),
            'joined_at': joined_at_str
        }

    yaml_text = yaml.dump(data, allow_unicode=True, sort_keys=False)

    # 输出到命令行
    print("\n--- 群组成员列表 ---")
    print(yaml_text)

    print(f"✅ 共获取 {len(data)} 名成员")
    
    # 保存到文件
    output_file = f"members_{entity.id}.yaml"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(yaml_text)

    print(f"📄 已保存到文件: {output_file}")

with client:
    client.loop.run_until_complete(main())
