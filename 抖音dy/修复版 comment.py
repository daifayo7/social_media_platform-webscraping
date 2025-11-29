import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import jieba
from collections import Counter
import json
from datetime import datetime
import re

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 修复后的数据 - 将JavaScript的false/null转换为Python的False/None
comments_data = {
    "status_code": 0,
    "comments": [
        {
            "cid": "7569543503384036153",
            "text": "@薏湫 @漱江语 @我和我的贝斯",
            "aweme_id": "7568361402794287973",
            "create_time": 1762421688,
            "digg_count": 0,
            "status": 1,
            "user": {
                "uid": "1700307667009380",
                "short_id": "31431035259",
                "nickname": "yoko",
                "avatar_thumb": {
                    "uri": "100x100/aweme-avatar/tos-cn-avt-0015_cbf7523c85a1f306f763c272030fb2f4",
                    "url_list": [
                        "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_cbf7523c85a1f306f763c272030fb2f4.jpeg?from=2064092626"
                    ],
                    "width": 720,
                    "height": 720
                },
                "follow_status": 0,
                "is_block": False,  # 修复：false -> False
                "custom_verify": "",
                "unique_id": "31431035259",
                "enterprise_verify_reason": "",
                "is_ad_fake": False,  # 修复：false -> False
                "profile_component_disabled": None,  # 修复：null -> None
                "region": "CN",
                "commerce_user_level": 0,
                "platform_sync_info": None,  # 修复：null -> None
                "secret": 0,
                "geofencing": None,  # 修复：null -> None
                "user_canceled": False,  # 修复：false -> False
                "status": 1,
                "follower_status": 0,
                "comment_setting": 0,
                "cover_url": None,  # 修复：null -> None
                "item_list": None,  # 修复：null -> None
                "new_story_cover": None,  # 修复：null -> None
                "is_star": False,  # 修复：false -> False
                "type_label": None,  # 修复：null -> None
                "ad_cover_url": None,  # 修复：null -> None
                "relative_users": None,  # 修复：null -> None
                "cha_list": None,  # 修复：null -> None
                "sec_uid": "MS4wLjABAAAAAIXJXA7J40KRx4WY1GhWE2Vddn2yNsEbamBGAV8BHPk0wYUEDZqbh1nO_vMcqfvL",
                "need_points": None,  # 修复：null -> None
                "homepage_bottom_toast": None,  # 修复：null -> None
                "can_set_geofencing": None,  # 修复：null -> None
                "white_cover_url": None,  # 修复：null -> None
                "user_tags": None,  # 修复：null -> None
                "ban_user_functions": [],
                "aweme_control": {
                    "can_forward": True,
                    "can_share": True,
                    "can_comment": True,
                    "can_show_comment": True
                },
                "card_entries": None,  # 修复：null -> None
                "display_info": None,  # 修复：null -> None
                "card_entries_not_display": None,  # 修复：null -> None
                "card_sort_priority": None,  # 修复：null -> None
                "interest_tags": None,  # 修复：null -> None
                "link_item_list": None,  # 修复：null -> None
                "user_permissions": None,  # 修复：null -> None
                "offline_info_list": None,  # 修复：null -> None
                "is_blocking_v2": False,  # 修复：false -> False
                "is_blocked_v2": False,  # 修复：false -> False
                "close_friend_type": 0,
                "signature_extra": None,  # 修复：null -> None
                "personal_tag_list": None,  # 修复：null -> None
                "cf_list": None,  # 修复：null -> None
                "im_role_ids": None,  # 修复：null -> None
                "not_seen_item_id_list": None,  # 修复：null -> None
                "follower_list_secondary_information_struct": None,  # 修复：null -> None
                "endorsement_info_list": None,  # 修复：null -> None
                "text_extra": None,  # 修复：null -> None
                "contrail_list": None,  # 修复：null -> None
                "data_label_list": None,  # 修复：null -> None
                "not_seen_item_id_list_v2": None,  # 修复：null -> None
                "special_people_labels": None,  # 修复：null -> None
                "familiar_visitor_user": None,  # 修复：null -> None
                "avatar_schema_list": None,  # 修复：null -> None
                "profile_mob_params": None,  # 修复：null -> None
                "disable_image_comment_saved": 0,
                "verification_permission_ids": None,  # 修复：null -> None
                "batch_unfollow_relation_desc": None,  # 修复：null -> None
                "batch_unfollow_contain_tabs": None,  # 修复：null -> None
                "creator_tag_list": None,  # 修复：null -> None
                "private_relation_list": None,  # 修复：null -> None
                "identity_labels": None  # 修复：null -> None
            },
            "reply_id": "0",
            "user_digged": 0,
            "reply_comment": None,  # 修复：null -> None
            "text_extra": [
                {
                    "start": 0,
                    "end": 3,
                    "user_id": "1829225058012248",
                    "type": 0,
                    "hashtag_name": "",
                    "hashtag_id": "",
                    "sec_uid": "MS4wLjABAAAAFZd8tGBGC74i3OVdaS3VuPebOXC_sMfc5P2E8c5HA8isr55Kt6CbOBGW87qZSfVy"
                },
                {
                    "start": 4,
                    "end": 8,
                    "user_id": "108117151281",
                    "type": 0,
                    "hashtag_name": "",
                    "hashtag_id": "",
                    "sec_uid": "MS4wLjABAAAAExNOYBA84YqBangOImx0fDRWFoN6prMyHnZLofFodn0"
                },
                {
                    "start": 9,
                    "end": 16,
                    "user_id": "2590902183797148",
                    "type": 0,
                    "hashtag_name": "",
                    "hashtag_id": "",
                    "sec_uid": "MS4wLjABAAAA2o0UsBmWVmvNDVCtd_sEDUPF_VIaYUOjiBPwcG_F4Hj8Wcjl947-y-0ZUCkDqM_a"
                }
            ],
            "label_text": "",
            "label_type": -1,
            "reply_comment_total": 0,
            "reply_to_reply_id": "0",
            "is_author_digged": False,  # 修复：false -> False
            "stick_position": 0,
            "user_buried": False,  # 修复：false -> False
            "label_list": None,  # 修复：null -> None
            "is_hot": False,  # 修复：false -> False
            "text_music_info": None,  # 修复：null -> None
            "image_list": None,  # 修复：null -> None
            "is_note_comment": 0,
            "ip_label": "广东",
            "can_share": True,
            "item_comment_total": 347,
            "level": 1,
            "video_list": None,  # 修复：null -> None
            "sort_tags": "{\"bottom\":1}",
            "is_user_tend_to_reply": False,  # 修复：false -> False
            "content_type": 1,
            "is_folded": False,  # 修复：false -> False
            "enter_from": "homepage_hot"
        },
        # 添加其他评论数据，确保同样修复false/null
        {
            "cid": "7569599665823662906",
            "text": "革命是要流血牺牲的",
            "aweme_id": "7568361402794287973",
            "create_time": 1762434764,
            "digg_count": 4,
            "status": 1,
            "user": {
                "uid": "63916472199",
                "short_id": "1480879554",
                "nickname": "小道士",
                "is_block": False,  # 修复
                "custom_verify": "",
                "unique_id": "",
                "is_ad_fake": False,  # 修复
                "profile_component_disabled": None,  # 修复
                # ... 其他用户字段，确保修复所有false/null
            },
            "reply_id": "0",
            "user_digged": 0,
            "reply_comment": None,  # 修复
            "text_extra": [],
            "label_text": "",
            "label_type": -1,
            "reply_comment_total": 0,
            "reply_to_reply_id": "0",
            "is_author_digged": False,  # 修复
            "stick_position": 0,
            "user_buried": False,  # 修复
            "label_list": None,  # 修复
            "is_hot": False,  # 修复
            "text_music_info": None,  # 修复
            "image_list": None,  # 修复
            "is_note_comment": 0,
            "ip_label": "陕西",
            "item_comment_total": 347,
            "level": 1,
            "video_list": None,  # 修复
            "sort_tags": "{\"eco_level_3\":1,\"bottom\":1}",
            "is_user_tend_to_reply": False,  # 修复
            "content_type": 1,
            "is_folded": False,  # 修复
            "enter_from": "homepage_hot"
        }
        # 继续添加其他评论...
    ],
    "cursor": 180,
    "has_more": 0,
    "reply_style": 2,
    "total": 347,
    "extra": {
        "now": 1764398990000,
        "fatal_item_ids": None,  # 修复：null -> None
        "scenes": None  # 修复：null -> None
    },
    "log_pb": {
        "impr_id": "2025112914495021E923D282BD67161787"
    },
    "hotsoon_filtered_count": 0,
    "user_commented": -1,
    "fast_response_comment": {
        "constant_response_words": [
            "赞",
            "比心",
            "加油"
        ],
        "timed_response_words": [
            "早上好",
            "下午好",
            "晚上好"
        ]
    },
    "comment_config": {},
    "general_comment_config": {},
    "show_management_entry_point": 0,
    "folded_comment_count": 0
}


def safe_extract_comments(data):
    """安全提取评论信息，处理可能的数据异常"""
    comments_list = []

    # 检查数据结构
    if not data or 'comments' not in data:
        print("错误：数据格式不正确，缺少'comments'字段")
        return pd.DataFrame()

    comments = data['comments']
    if not comments:
        print("警告：评论列表为空")
        return pd.DataFrame()

    print(f"找到 {len(comments)} 条评论")

    for i, comment in enumerate(comments):
        try:
            # 检查必要字段
            if 'create_time' not in comment:
                print(f"警告：第{i + 1}条评论缺少create_time字段")
                continue

            if 'text' not in comment:
                print(f"警告：第{i + 1}条评论缺少text字段")
                continue

            # 提取信息
            comment_info = {
                'cid': comment.get('cid', f'unknown_{i}'),
                'text': comment.get('text', ''),
                'create_time': comment.get('create_time'),
                'digg_count': comment.get('digg_count', 0),
                'user_nickname': comment.get('user', {}).get('nickname', '未知用户'),
                'ip_label': comment.get('ip_label', '未知地区'),
                'reply_comment_total': comment.get('reply_comment_total', 0)
            }

            # 转换时间戳为datetime
            try:
                comment_info['create_time'] = datetime.fromtimestamp(comment_info['create_time'])
            except (ValueError, TypeError) as e:
                print(f"时间戳转换错误: {e}，使用当前时间")
                comment_info['create_time'] = datetime.now()

            comments_list.append(comment_info)

        except Exception as e:
            print(f"处理第{i + 1}条评论时出错: {e}")
            continue

    return pd.DataFrame(comments_list)


# 自动修复函数 - 如果您有大量数据需要修复
def fix_javascript_syntax(data_str):
    """自动修复JavaScript语法到Python语法"""
    # 将JavaScript的false/null替换为Python的False/None
    data_str = data_str.replace(': false', ': False')
    data_str = data_str.replace(': null', ': None')
    data_str = data_str.replace(':false', ':False')
    data_str = data_str.replace(':null', ':None')
    return data_str


def main():
    print("开始提取评论数据...")
    df = safe_extract_comments(comments_data)

    if df.empty:
        print("错误：没有成功提取到任何评论数据")
        print("请检查数据格式是否正确")
        return

    print("\n数据提取成功！")
    print(f"总评论数: {len(df)}")
    print(f"时间范围: {df['create_time'].min()} 到 {df['create_time'].max()}")
    print("\n前5条评论:")
    print(df[['text', 'digg_count', 'ip_label']].head())

    # 数据预处理
    df['text_length'] = df['text'].str.len()
    df['date'] = df['create_time'].dt.date

    # 创建可视化
    create_visualizations(df)

    # 文本分析
    analyze_text(df)


def create_visualizations(df):
    """创建可视化图表"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    # 1. 点赞数分布
    axes[0, 0].hist(df['digg_count'], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    axes[0, 0].set_title('评论点赞数分布')
    axes[0, 0].set_xlabel('点赞数')
    axes[0, 0].set_ylabel('频次')
    axes[0, 0].grid(True, alpha=0.3)

    # 2. 地域分布
    region_counts = df['ip_label'].value_counts().head(10)
    axes[0, 1].bar(region_counts.index, region_counts.values, color='lightcoral')
    axes[0, 1].set_title('评论地域分布TOP10')
    axes[0, 1].set_ylabel('评论数量')
    axes[0, 1].tick_params(axis='x', rotation=45)

    # 3. 文本长度分析
    axes[1, 0].hist(df['text_length'], bins=15, alpha=0.7, color='lightgreen', edgecolor='black')
    axes[1, 0].set_title('评论文本长度分布')
    axes[1, 0].set_xlabel('文本长度')
    axes[1, 0].set_ylabel('频次')
    axes[1, 0].grid(True, alpha=0.3)

    # 4. 高点赞评论
    top_comments = df.nlargest(5, 'digg_count')[['text', 'digg_count']]
    top_comments['short_text'] = top_comments['text'].str[:15] + '...'
    y_pos = range(len(top_comments))
    axes[1, 1].barh(y_pos, top_comments['digg_count'], color='gold')
    axes[1, 1].set_yticks(y_pos)
    axes[1, 1].set_yticklabels(top_comments['short_text'])
    axes[1, 1].set_title('高点赞评论TOP5')
    axes[1, 1].set_xlabel('点赞数')

    plt.tight_layout()
    plt.show()


def analyze_text(df):
    """分析文本内容"""
    # 词频分析
    all_text = ' '.join(df['text'].astype(str))
    words = jieba.cut(all_text)

    stop_words = {'的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一'}
    filtered_words = [word for word in words if len(word) > 1 and word not in stop_words]

    word_freq = Counter(filtered_words)

    # 生成词云
    try:
        wordcloud = WordCloud(
            font_path='/System/Library/Fonts/PingFang.ttc',
            width=800,
            height=400,
            background_color='white',
            max_words=100
        ).generate_from_frequencies(word_freq)

        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('评论关键词词云')
        plt.show()
    except Exception as e:
        print(f"生成词云时出错: {e}")
        print("使用备用字体...")
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            max_words=100
        ).generate_from_frequencies(word_freq)

        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('评论关键词词云')
        plt.show()

    # 数据报告
    print("\n=== 数据报告 ===")
    print(f"总评论数: {len(df)}")
    print(f"总点赞数: {df['digg_count'].sum()}")
    print(f"平均点赞数: {df['digg_count'].mean():.2f}")
    print(f"涉及地域数量: {df['ip_label'].nunique()}")
    print(f"平均评论长度: {df['text_length'].mean():.2f} 字符")


# 运行主程序
if __name__ == "__main__":
    main()