import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import jieba
from collections import Counter
import re
from datetime import datetime


# 在代码开头添加这个简单的字体修复
import matplotlib.pyplot as plt
import matplotlib as mpl

# 方法1: 使用系统字体
try:
    mpl.rcParams['font.family'] = ['Arial Unicode MS', 'DejaVu Sans', 'sans-serif']
    mpl.rcParams['axes.unicode_minus'] = False
    print("字体设置成功")
except:
    print("使用默认字体")

# 方法2: 完全禁用字体警告
import warnings
warnings.filterwarnings('ignore', category=UserWarning)

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# # 提取评论数据

# 1. 将数据保存为data.json文件
# 2. 使用以下代码加载
import json
with open('data.json', 'r', encoding='utf-8') as f:
    comments_data = json.load(f)  # 会自动转换false/null


# comments_data = {
#     "status_code": 0,
#     "comments": [
#         # 这里插入您提供的完整JSON数据中的comments数组
# {
#             "cid": "7569543503384036153",
#             "text": "@薏湫 @漱江语 @我和我的贝斯",
#             "aweme_id": "7568361402794287973",
#             "create_time": 1762421688,
#             "digg_count": 0,
#             "status": 1,
#             "user": {
#                 "uid": "1700307667009380",
#                 "short_id": "31431035259",
#                 "nickname": "yoko",
#                 "avatar_thumb": {
#                     "uri": "100x100/aweme-avatar/tos-cn-avt-0015_cbf7523c85a1f306f763c272030fb2f4",
#                     "url_list": [
#                         "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_cbf7523c85a1f306f763c272030fb2f4.jpeg?from=2064092626"
#                     ],
#                     "width": 720,
#                     "height": 720
#                 },
#                 "follow_status": 0,
#                 "is_block": false,
#                 "custom_verify": "",
#                 "unique_id": "31431035259",
#                 "enterprise_verify_reason": "",
#                 "is_ad_fake": false,
#                 "profile_component_disabled": null,
#                 "region": "CN",
#                 "commerce_user_level": 0,
#                 "platform_sync_info": null,
#                 "secret": 0,
#                 "geofencing": null,
#                 "user_canceled": false,
#                 "status": 1,
#                 "follower_status": 0,
#                 "comment_setting": 0,
#                 "cover_url": null,
#                 "item_list": null,
#                 "new_story_cover": null,
#                 "is_star": false,
#                 "type_label": null,
#                 "ad_cover_url": null,
#                 "relative_users": null,
#                 "cha_list": null,
#                 "sec_uid": "MS4wLjABAAAAAIXJXA7J40KRx4WY1GhWE2Vddn2yNsEbamBGAV8BHPk0wYUEDZqbh1nO_vMcqfvL",
#                 "need_points": null,
#                 "homepage_bottom_toast": null,
#                 "can_set_geofencing": null,
#                 "white_cover_url": null,
#                 "user_tags": null,
#                 "ban_user_functions": [],
#                 "aweme_control": {
#                     "can_forward": true,
#                     "can_share": true,
#                     "can_comment": true,
#                     "can_show_comment": true
#                 },
#                 "card_entries": null,
#                 "display_info": null,
#                 "card_entries_not_display": null,
#                 "card_sort_priority": null,
#                 "interest_tags": null,
#                 "link_item_list": null,
#                 "user_permissions": null,
#                 "offline_info_list": null,
#                 "is_blocking_v2": false,
#                 "is_blocked_v2": false,
#                 "close_friend_type": 0,
#                 "signature_extra": null,
#                 "personal_tag_list": null,
#                 "cf_list": null,
#                 "im_role_ids": null,
#                 "not_seen_item_id_list": null,
#                 "follower_list_secondary_information_struct": null,
#                 "endorsement_info_list": null,
#                 "text_extra": null,
#                 "contrail_list": null,
#                 "data_label_list": null,
#                 "not_seen_item_id_list_v2": null,
#                 "special_people_labels": null,
#                 "familiar_visitor_user": null,
#                 "avatar_schema_list": null,
#                 "profile_mob_params": null,
#                 "disable_image_comment_saved": 0,
#                 "verification_permission_ids": null,
#                 "batch_unfollow_relation_desc": null,
#                 "batch_unfollow_contain_tabs": null,
#                 "creator_tag_list": null,
#                 "private_relation_list": null,
#                 "identity_labels": null
#             },
#             "reply_id": "0",
#             "user_digged": 0,
#             "reply_comment": null,
#             "text_extra": [
#                 {
#                     "start": 0,
#                     "end": 3,
#                     "user_id": "1829225058012248",
#                     "type": 0,
#                     "hashtag_name": "",
#                     "hashtag_id": "",
#                     "sec_uid": "MS4wLjABAAAAFZd8tGBGC74i3OVdaS3VuPebOXC_sMfc5P2E8c5HA8isr55Kt6CbOBGW87qZSfVy"
#                 },
#                 {
#                     "start": 4,
#                     "end": 8,
#                     "user_id": "108117151281",
#                     "type": 0,
#                     "hashtag_name": "",
#                     "hashtag_id": "",
#                     "sec_uid": "MS4wLjABAAAAExNOYBA84YqBangOImx0fDRWFoN6prMyHnZLofFodn0"
#                 },
#                 {
#                     "start": 9,
#                     "end": 16,
#                     "user_id": "2590902183797148",
#                     "type": 0,
#                     "hashtag_name": "",
#                     "hashtag_id": "",
#                     "sec_uid": "MS4wLjABAAAA2o0UsBmWVmvNDVCtd_sEDUPF_VIaYUOjiBPwcG_F4Hj8Wcjl947-y-0ZUCkDqM_a"
#                 }
#             ],
#             "label_text": "",
#             "label_type": -1,
#             "reply_comment_total": 0,
#             "reply_to_reply_id": "0",
#             "is_author_digged": false,
#             "stick_position": 0,
#             "user_buried": false,
#             "label_list": null,
#             "is_hot": false,
#             "text_music_info": null,
#             "image_list": null,
#             "is_note_comment": 0,
#             "ip_label": "广东",      # ip 地域
#             "can_share": true,
#             "item_comment_total": 347,
#             "level": 1,
#             "video_list": null,
#             "sort_tags": "{\"bottom\":1}",
#             "is_user_tend_to_reply": false,
#             "content_type": 1,
#             "is_folded": false,
#             "enter_from": "homepage_hot"
#         },
#         {
#             "cid": "7569599665823662906",
#             "text": "革命是要流血牺牲的",     # 评论文本
#             "aweme_id": "7568361402794287973",
#             "create_time": 1762434764,     # 发布时间
#             "digg_count": 4,               # 点赞数
#             "status": 1,
#             "user": {
#                 "uid": "63916472199",
#                 "short_id": "1480879554",
#                 "nickname": "小道士",    #用户名
#                 "avatar_thumb": {
#                     "uri": "100x100/aweme-avatar/mosaic-legacy_2ecb20007c4ac1728ff94",
#                     "url_list": [
#                         "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/mosaic-legacy_2ecb20007c4ac1728ff94.jpeg?from=2064092626"
#                     ],
#                     "width": 720,
#                     "height": 720
#                 },
#                 "follow_status": 0,
#                 "is_block": false,
#                 "custom_verify": "",
#                 "unique_id": "",
#                 "enterprise_verify_reason": "",
#                 "is_ad_fake": false,
#                 "profile_component_disabled": null,
#                 "region": "CN",
#                 "commerce_user_level": 0,
#                 "platform_sync_info": null,
#                 "secret": 0,
#                 "geofencing": null,
#                 "user_canceled": false,
#                 "status": 1,
#                 "follower_status": 0,
#                 "comment_setting": 0,
#                 "cover_url": null,
#                 "item_list": null,
#                 "new_story_cover": null,
#                 "is_star": false,
#                 "type_label": null,
#                 "ad_cover_url": null,
#                 "relative_users": null,
#                 "cha_list": null,
#                 "sec_uid": "MS4wLjABAAAAgGO_U2WUo46xzpEp_WA4qCG6qvuXe-kFhUXqkbME2Rw",
#                 "need_points": null,
#                 "homepage_bottom_toast": null,
#                 "can_set_geofencing": null,
#                 "white_cover_url": null,
#                 "user_tags": null,
#                 "ban_user_functions": null,
#                 "aweme_control": {
#                     "can_forward": true,
#                     "can_share": true,
#                     "can_comment": true,
#                     "can_show_comment": true
#                 },
#                 "card_entries": null,
#                 "display_info": null,
#                 "card_entries_not_display": null,
#                 "card_sort_priority": null,
#                 "interest_tags": null,
#                 "link_item_list": null,
#                 "user_permissions": null,
#                 "offline_info_list": null,
#                 "is_blocking_v2": false,
#                 "is_blocked_v2": false,
#                 "close_friend_type": 0,
#                 "signature_extra": null,
#                 "personal_tag_list": null,
#                 "cf_list": null,
#                 "im_role_ids": null,
#                 "not_seen_item_id_list": null,
#                 "follower_list_secondary_information_struct": null,
#                 "endorsement_info_list": null,
#                 "text_extra": null,
#                 "contrail_list": null,
#                 "data_label_list": null,
#                 "not_seen_item_id_list_v2": null,
#                 "special_people_labels": null,
#                 "familiar_visitor_user": null,
#                 "avatar_schema_list": null,
#                 "profile_mob_params": null,
#                 "disable_image_comment_saved": 0,
#                 "verification_permission_ids": null,
#                 "batch_unfollow_relation_desc": null,
#                 "batch_unfollow_contain_tabs": null,
#                 "creator_tag_list": null,
#                 "private_relation_list": null,
#                 "identity_labels": null
#             },
#             "reply_id": "0",
#             "user_digged": 0,
#             "reply_comment": null,
#             "text_extra": [],
#             "label_text": "",
#             "label_type": -1,
#             "reply_comment_total": 0,
#             "reply_to_reply_id": "0",
#             "is_author_digged": false,
#             "stick_position": 0,
#             "user_buried": false,
#             "label_list": null,
#             "is_hot": false,
#             "text_music_info": null,
#             "image_list": null,
#             "is_note_comment": 0,
#             "ip_label": "陕西",
#             "item_comment_total": 347,
#             "level": 1,
#             "video_list": null,
#             "sort_tags": "{\"eco_level_3\":1,\"bottom\":1}",
#             "is_user_tend_to_reply": false,
#             "content_type": 1,
#             "is_folded": false,
#             "enter_from": "homepage_hot"
#         },
#         {
#             "cid": "7575784801580434202",
#             "text": "我要收藏这个评论区。以后有女的说不支持极端女权，就把这个给他看。",
#             "aweme_id": "7568361402794287973",
#             "create_time": 1763874853,
#             "digg_count": 5,
#             "status": 1,
#             "user": {
#                 "uid": "84256418923",
#                 "short_id": "323854922",
#                 "nickname": "大雨🌧️做法",
#                 "avatar_thumb": {
#                     "uri": "100x100/aweme-avatar/tos-cn-i-0813c001_oQ5ZRAEGOEWUfLSLIAAr9AEeBBbzeZiA17IzAx",
#                     "url_list": [
#                         "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c001_oQ5ZRAEGOEWUfLSLIAAr9AEeBBbzeZiA17IzAx.jpeg?from=2064092626"
#                     ],
#                     "width": 720,
#                     "height": 720
#                 },
#                 "follow_status": 0,
#                 "is_block": false,
#                 "custom_verify": "",
#                 "unique_id": "",
#                 "enterprise_verify_reason": "",
#                 "is_ad_fake": false,
#                 "profile_component_disabled": null,
#                 "region": "CN",
#                 "commerce_user_level": 0,
#                 "platform_sync_info": null,
#                 "secret": 0,
#                 "geofencing": null,
#                 "user_canceled": false,
#                 "status": 1,
#                 "follower_status": 0,
#                 "comment_setting": 0,
#                 "cover_url": null,
#                 "item_list": null,
#                 "new_story_cover": null,
#                 "is_star": false,
#                 "type_label": null,
#                 "ad_cover_url": null,
#                 "relative_users": null,
#                 "cha_list": null,
#                 "sec_uid": "MS4wLjABAAAAU8GMGcRsLYA3i9DCimkXNMO5SO_6ZkPL6juKHPQ4J9k",
#                 "need_points": null,
#                 "homepage_bottom_toast": null,
#                 "can_set_geofencing": null,
#                 "white_cover_url": null,
#                 "user_tags": null,
#                 "ban_user_functions": [],
#                 "aweme_control": {
#                     "can_forward": true,
#                     "can_share": true,
#                     "can_comment": true,
#                     "can_show_comment": true
#                 },
#                 "card_entries": null,
#                 "display_info": null,
#                 "card_entries_not_display": null,
#                 "card_sort_priority": null,
#                 "interest_tags": null,
#                 "link_item_list": null,
#                 "user_permissions": null,
#                 "offline_info_list": null,
#                 "is_blocking_v2": false,
#                 "is_blocked_v2": false,
#                 "close_friend_type": 0,
#                 "signature_extra": null,
#                 "personal_tag_list": null,
#                 "cf_list": null,
#                 "im_role_ids": null,
#                 "not_seen_item_id_list": null,
#                 "follower_list_secondary_information_struct": null,
#                 "endorsement_info_list": null,
#                 "text_extra": null,
#                 "contrail_list": null,
#                 "data_label_list": null,
#                 "not_seen_item_id_list_v2": null,
#                 "special_people_labels": null,
#                 "familiar_visitor_user": null,
#                 "avatar_schema_list": null,
#                 "profile_mob_params": null,
#                 "disable_image_comment_saved": 0,
#                 "verification_permission_ids": null,
#                 "batch_unfollow_relation_desc": null,
#                 "batch_unfollow_contain_tabs": null,
#                 "creator_tag_list": null,
#                 "private_relation_list": null,
#                 "identity_labels": null
#             },
#             "reply_id": "0",
#             "user_digged": 0,
#             "reply_comment": null,
#             "text_extra": [],
#             "label_text": "",
#             "label_type": -1,
#             "reply_comment_total": 0,
#             "reply_to_reply_id": "0",
#             "is_author_digged": false,
#             "stick_position": 0,
#             "user_buried": false,
#             "label_list": null,
#             "is_hot": false,
#             "text_music_info": null,
#             "image_list": null,
#             "is_note_comment": 0,
#             "ip_label": "湖南",
#             "item_comment_total": 347,
#             "level": 1,
#             "video_list": null,
#             "sort_tags": "{\"eco_level_11\":1,\"eco_level_1\":1,\"eco_level_5\":1,\"eco_level_8\":1,\"eco_level_2\":1,\"bottom\":1,\"eco_level_10\":1}",
#             "is_user_tend_to_reply": false,
#             "content_type": 1,
#             "is_folded": false,
#             "enter_from": "homepage_hot"
#         },
#         {
#             "cid": "7575648886690267944",
#             "text": "你能顺利出生，能读书，能考驾照，能工作，能穿漂亮衣服，都是因为有女权主义者，她们的极端，她们的激进",
#             "aweme_id": "7568361402794287973",
#             "create_time": 1763843213,
#             "digg_count": 25,
#             "status": 1,
#             "user": {
#                 "uid": "75887441492",
#                 "short_id": "168821962",
#                 "nickname": "十六夜 -⩊-",
#                 "avatar_thumb": {
#                     "uri": "100x100/aweme-avatar/tos-cn-avt-0015_6301d792fe1a122344d9e6b7769fe99f",
#                     "url_list": [
#                         "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_6301d792fe1a122344d9e6b7769fe99f.jpeg?from=2064092626"
#                     ],
#                     "width": 720,
#                     "height": 720
#                 },
#                 "follow_status": 0,
#                 "is_block": false,
#                 "custom_verify": "",
#                 "unique_id": "",
#                 "enterprise_verify_reason": "",
#                 "is_ad_fake": false,
#                 "profile_component_disabled": null,
#                 "region": "CN",
#                 "commerce_user_level": 0,
#                 "platform_sync_info": null,
#                 "secret": 0,
#                 "geofencing": null,
#                 "user_canceled": false,
#                 "status": 1,
#                 "follower_status": 0,
#                 "comment_setting": 0,
#                 "cover_url": null,
#                 "item_list": null,
#                 "new_story_cover": null,
#                 "is_star": false,
#                 "type_label": null,
#                 "ad_cover_url": null,
#                 "relative_users": null,
#                 "cha_list": null,
#                 "sec_uid": "MS4wLjABAAAAzx_CEElXH3NvHkNiLkQ56CXWoK-NT4CPNJ0r3MncJYo",
#                 "need_points": null,
#                 "homepage_bottom_toast": null,
#                 "can_set_geofencing": null,
#                 "white_cover_url": null,
#                 "user_tags": null,
#                 "ban_user_functions": [],
#                 "aweme_control": {
#                     "can_forward": true,
#                     "can_share": true,
#                     "can_comment": true,
#                     "can_show_comment": true
#                 },
#                 "card_entries": null,
#                 "display_info": null,
#                 "card_entries_not_display": null,
#                 "card_sort_priority": null,
#                 "interest_tags": null,
#                 "link_item_list": null,
#                 "user_permissions": null,
#                 "offline_info_list": null,
#                 "is_blocking_v2": false,
#                 "is_blocked_v2": false,
#                 "close_friend_type": 0,
#                 "signature_extra": null,
#                 "personal_tag_list": null,
#                 "cf_list": null,
#                 "im_role_ids": null,
#                 "not_seen_item_id_list": null,
#                 "follower_list_secondary_information_struct": null,
#                 "endorsement_info_list": null,
#                 "text_extra": null,
#                 "contrail_list": null,
#                 "data_label_list": null,
#                 "not_seen_item_id_list_v2": null,
#                 "special_people_labels": null,
#                 "familiar_visitor_user": null,
#                 "avatar_schema_list": null,
#                 "profile_mob_params": null,
#                 "disable_image_comment_saved": 0,
#                 "verification_permission_ids": null,
#                 "batch_unfollow_relation_desc": null,
#                 "batch_unfollow_contain_tabs": null,
#                 "creator_tag_list": null,
#                 "private_relation_list": null,
#                 "identity_labels": null
#             },
#             "reply_id": "0",
#             "user_digged": 0,
#             "reply_comment": null,
#             "text_extra": [],
#             "label_text": "",
#             "label_type": -1,
#             "reply_comment_total": 0,
#             "reply_to_reply_id": "0",
#             "is_author_digged": false,
#             "stick_position": 0,
#             "user_buried": false,
#             "label_list": null,
#             "is_hot": false,
#             "text_music_info": null,
#             "image_list": null,
#             "is_note_comment": 0,
#             "ip_label": "英国",
#             "item_comment_total": 347,
#             "level": 1,
#             "video_list": null,
#             "sort_tags": "{\"bottom\":1,\"eco_level_2\":1,\"eco_level_10\":1,\"eco_level_11\":1,\"eco_level_1\":1,\"eco_level_8\":1,\"eco_level_5\":1}",
#             "is_user_tend_to_reply": false,
#             "content_type": 1,
#             "is_folded": false,
#             "enter_from": "homepage_hot"
#         },
#         {
#             "cid": "7569494515582419747",
#             "text": "一个个都骂女权，三八妇女节，却不说，这些都是一个个女性用鲜血换来的，嫉妒没有四八中男节的[尬笑]谁拦着你们去牺牲了[尬笑]你们也可以用鲜血去争取呀[尬笑]真搞笑",
#             "aweme_id": "7568361402794287973",
#             "create_time": 1762410284,
#             "digg_count": 37,
#             "status": 1,
#             "user": {
#                 "uid": "65931711297",
#                 "short_id": "1085867775",
#                 "nickname": "口罩姨姨",
#                 "avatar_thumb": {
#                     "uri": "100x100/aweme-avatar/tos-cn-i-0813_ooua7O6xSEEABABhdENFmAeEIeDAROATDAfB4h",
#                     "url_list": [
#                         "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_ooua7O6xSEEABABhdENFmAeEIeDAROATDAfB4h.jpeg?from=2064092626"
#                     ],
#                     "width": 720,
#                     "height": 720
#                 },
#                 "follow_status": 0,
#                 "is_block": false,
#                 "custom_verify": "",
#                 "unique_id": "h278097281",
#                 "enterprise_verify_reason": "",
#                 "is_ad_fake": false,
#                 "profile_component_disabled": null,
#                 "region": "CN",
#                 "commerce_user_level": 0,
#                 "platform_sync_info": null,
#                 "secret": 0,
#                 "geofencing": null,
#                 "user_canceled": false,
#                 "status": 1,
#                 "follower_status": 0,
#                 "comment_setting": 0,
#                 "cover_url": null,
#                 "item_list": null,
#                 "new_story_cover": null,
#                 "is_star": false,
#                 "type_label": null,
#                 "ad_cover_url": null,
#                 "relative_users": null,
#                 "cha_list": null,
#                 "sec_uid": "MS4wLjABAAAA8X07kR4BAromDNbl1FVvSpvN20KrQsTr3PszZPRgfEc",
#                 "need_points": null,
#                 "homepage_bottom_toast": null,
#                 "can_set_geofencing": null,
#                 "white_cover_url": null,
#                 "user_tags": null,
#                 "ban_user_functions": [],
#                 "aweme_control": {
#                     "can_forward": true,
#                     "can_share": true,
#                     "can_comment": true,
#                     "can_show_comment": true
#                 },
#                 "card_entries": null,
#                 "display_info": null,
#                 "card_entries_not_display": null,
#                 "card_sort_priority": null,
#                 "interest_tags": null,
#                 "link_item_list": null,
#                 "user_permissions": null,
#                 "offline_info_list": null,
#                 "is_blocking_v2": false,
#                 "is_blocked_v2": false,
#                 "close_friend_type": 0,
#                 "signature_extra": null,
#                 "personal_tag_list": null,
#                 "cf_list": null,
#                 "im_role_ids": null,
#                 "not_seen_item_id_list": null,
#                 "follower_list_secondary_information_struct": null,
#                 "endorsement_info_list": null,
#                 "text_extra": null,
#                 "contrail_list": null,
#                 "data_label_list": null,
#                 "not_seen_item_id_list_v2": null,
#                 "special_people_labels": null,
#                 "familiar_visitor_user": null,
#                 "avatar_schema_list": null,
#                 "profile_mob_params": null,
#                 "disable_image_comment_saved": 0,
#                 "verification_permission_ids": null,
#                 "batch_unfollow_relation_desc": null,
#                 "batch_unfollow_contain_tabs": null,
#                 "creator_tag_list": null,
#                 "private_relation_list": null,
#                 "identity_labels": null
#             },
#             "reply_id": "0",
#             "user_digged": 0,
#             "reply_comment": null,
#             "text_extra": [],
#             "label_text": "",
#             "label_type": -1,
#             "reply_comment_total": 0,
#             "reply_to_reply_id": "0",
#             "is_author_digged": false,
#             "stick_position": 0,
#             "user_buried": false,
#             "label_list": null,
#             "is_hot": false,
#             "text_music_info": null,
#             "image_list": null,
#             "is_note_comment": 0,
#             "ip_label": "辽宁",
#             "item_comment_total": 347,
#             "level": 1,
#             "video_list": null,
#             "sort_tags": "{\"eco_level_2\":1,\"bottom\":1,\"eco_level_10\":1,\"eco_level_11\":1,\"eco_level_1\":1,\"eco_level_5\":1,\"eco_level_8\":1}",
#             "is_user_tend_to_reply": false,
#             "content_type": 1,
#             "is_folded": false,
#             "enter_from": "homepage_hot"
#         },
#         {
#             "cid": "7569818736384082737",
#             "text": "现在的所谓极端女权只能算基本男权[钱]",
#             "aweme_id": "7568361402794287973",
#             "create_time": 1762485770,
#             "digg_count": 27,
#             "status": 1,
#             "user": {
#                 "uid": "96371080096",
#                 "short_id": "690724778",
#                 "nickname": "ᶘ ͡°ᴥ͡°ᶅ",
#                 "avatar_thumb": {
#                     "uri": "100x100/aweme-avatar/tos-cn-i-0813c000-ce_oYjEA6DfDevQFJAgIKog7MNDgECB8NAw7VfcQA",
#                     "url_list": [
#                         "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c000-ce_oYjEA6DfDevQFJAgIKog7MNDgECB8NAw7VfcQA.jpeg?from=2064092626"
#                     ],
#                     "width": 720,
#                     "height": 720
#                 },
#                 "follow_status": 0,
#                 "is_block": false,
#                 "custom_verify": "",
#                 "unique_id": "L10070706",
#                 "enterprise_verify_reason": "",
#                 "is_ad_fake": false,
#                 "profile_component_disabled": null,
#                 "region": "CN",
#                 "commerce_user_level": 0,
#                 "platform_sync_info": null,
#                 "secret": 0,
#                 "geofencing": null,
#                 "user_canceled": false,
#                 "status": 1,
#                 "follower_status": 0,
#                 "comment_setting": 0,
#                 "cover_url": null,
#                 "item_list": null,
#                 "new_story_cover": null,
#                 "is_star": false,
#                 "type_label": null,
#                 "ad_cover_url": null,
#                 "relative_users": null,
#                 "cha_list": null,
#                 "sec_uid": "MS4wLjABAAAApUByzx_M19widA8u68AaOv7lvr5AVBNVNgyM8Vcz_OM",
#                 "need_points": null,
#                 "homepage_bottom_toast": null,
#                 "can_set_geofencing": null,
#                 "white_cover_url": null,
#                 "user_tags": null,
#                 "ban_user_functions": [],
#                 "aweme_control": {
#                     "can_forward": true,
#                     "can_share": true,
#                     "can_comment": true,
#                     "can_show_comment": true
#                 },
#                 "card_entries": null,
#                 "display_info": null,
#                 "card_entries_not_display": null,
#                 "card_sort_priority": null,
#                 "interest_tags": null,
#                 "link_item_list": null,
#                 "user_permissions": null,
#                 "offline_info_list": null,
#                 "is_blocking_v2": false,
#                 "is_blocked_v2": false,
#                 "close_friend_type": 0,
#                 "signature_extra": null,
#                 "personal_tag_list": null,
#                 "cf_list": null,
#                 "im_role_ids": null,
#                 "not_seen_item_id_list": null,
#                 "follower_list_secondary_information_struct": null,
#                 "endorsement_info_list": null,
#                 "text_extra": null,
#                 "contrail_list": null,
#                 "data_label_list": null,
#                 "not_seen_item_id_list_v2": null,
#                 "special_people_labels": null,
#                 "familiar_visitor_user": null,
#                 "avatar_schema_list": null,
#                 "profile_mob_params": null,
#                 "disable_image_comment_saved": 0,
#                 "verification_permission_ids": null,
#                 "batch_unfollow_relation_desc": null,
#                 "batch_unfollow_contain_tabs": null,
#                 "creator_tag_list": null,
#                 "private_relation_list": null,
#                 "identity_labels": null
#             },
#             "reply_id": "0",
#             "user_digged": 0,
#             "reply_comment": null,
#             "text_extra": [],
#             "label_text": "",
#             "label_type": -1,
#             "reply_comment_total": 0,
#             "reply_to_reply_id": "0",
#             "is_author_digged": false,
#             "stick_position": 0,
#             "user_buried": false,
#             "label_list": null,
#             "is_hot": false,
#             "text_music_info": null,
#             "image_list": null,
#             "is_note_comment": 0,
#             "ip_label": "四川",
#             "item_comment_total": 347,
#             "level": 1,
#             "video_list": null,
#             "sort_tags": "{\"eco_level_11\":1,\"eco_level_1\":1,\"eco_level_5\":1,\"eco_level_8\":1,\"eco_level_2\":1,\"bottom\":1,\"eco_level_10\":1}",
#             "is_user_tend_to_reply": false,
#             "content_type": 1,
#             "is_folded": false,
#             "enter_from": "homepage_hot"
#         },
#         {
#             "cid": "7577936448033276729",
#             "text": "无论女孩还是男孩，其实大家一出生都是女权主义者了[黄脸祈祷]母亲享受的平权对待和工作机会，学校女老师教育这些最普遍不过的，我们大家已经开始成为女权主义者并那么做了",
#             "aweme_id": "7568361402794287973",
#             "create_time": 1764375824,
#             "digg_count": 6,
#             "status": 1,
#             "user": {
#                 "uid": "3337723133046659",
#                 "short_id": "2935429921",
#                 "nickname": "悲伤一只鹰",
#                 "avatar_thumb": {
#                     "uri": "100x100/aweme-avatar/tos-cn-i-0813_fbe45e7b0ec4463a960f0bca257ae354",
#                     "url_list": [
#                         "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_fbe45e7b0ec4463a960f0bca257ae354.jpeg?from=2064092626"
#                     ],
#                     "width": 720,
#                     "height": 720
#                 },
#                 "follow_status": 0,
#                 "is_block": false,
#                 "custom_verify": "",
#                 "unique_id": "00106n",
#                 "enterprise_verify_reason": "",
#                 "is_ad_fake": false,
#                 "profile_component_disabled": null,
#                 "region": "CN",
#                 "commerce_user_level": 0,
#                 "platform_sync_info": null,
#                 "secret": 0,
#                 "geofencing": null,
#                 "user_canceled": false,
#                 "status": 1,
#                 "follower_status": 0,
#                 "comment_setting": 0,
#                 "cover_url": null,
#                 "item_list": null,
#                 "new_story_cover": null,
#                 "is_star": false,
#                 "type_label": null,
#                 "ad_cover_url": null,
#                 "relative_users": null,
#                 "cha_list": null,
#                 "sec_uid": "MS4wLjABAAAA6h78tQKuJfjbz6CqmbSHMQ2_3EMfq4qwCNr3fCIuINvhV2nXHs4sUwU7ZYLqfoaQ",
#                 "need_points": null,
#                 "homepage_bottom_toast": null,
#                 "can_set_geofencing": null,
#                 "white_cover_url": null,
#                 "user_tags": null,
#                 "ban_user_functions": null,
#                 "aweme_control": {
#                     "can_forward": true,
#                     "can_share": true,
#                     "can_comment": true,
#                     "can_show_comment": true
#                 },
#                 "card_entries": null,
#                 "display_info": null,
#                 "card_entries_not_display": null,
#                 "card_sort_priority": null,
#                 "interest_tags": null,
#                 "link_item_list": null,
#                 "user_permissions": null,
#                 "offline_info_list": null,
#                 "is_blocking_v2": false,
#                 "is_blocked_v2": false,
#                 "close_friend_type": 0,
#                 "signature_extra": null,
#                 "personal_tag_list": null,
#                 "cf_list": null,
#                 "im_role_ids": null,
#                 "not_seen_item_id_list": null,
#                 "follower_list_secondary_information_struct": null,
#                 "endorsement_info_list": null,
#                 "text_extra": null,
#                 "contrail_list": null,
#                 "data_label_list": null,
#                 "not_seen_item_id_list_v2": null,
#                 "special_people_labels": null,
#                 "familiar_visitor_user": null,
#                 "avatar_schema_list": null,
#                 "profile_mob_params": null,
#                 "disable_image_comment_saved": 0,
#                 "verification_permission_ids": null,
#                 "batch_unfollow_relation_desc": null,
#                 "batch_unfollow_contain_tabs": null,
#                 "creator_tag_list": null,
#                 "private_relation_list": null,
#                 "identity_labels": null
#             },
#             "reply_id": "0",
#             "user_digged": 0,
#             "reply_comment": null,
#             "text_extra": [],
#             "label_text": "",
#             "label_type": -1,
#             "reply_comment_total": 0,
#             "reply_to_reply_id": "0",
#             "is_author_digged": false,
#             "stick_position": 0,
#             "user_buried": false,
#             "label_list": null,
#             "is_hot": false,
#             "text_music_info": null,
#             "image_list": null,
#             "is_note_comment": 0,
#             "ip_label": "江苏",
#             "item_comment_total": 347,
#             "level": 1,
#             "video_list": null,
#             "sort_tags": "{\"eco_level_11\":1,\"eco_level_10\":1,\"eco_level_1\":1,\"eco_level_5\":1,\"eco_level_8\":1,\"eco_level_2\":1,\"bottom\":1}",
#             "is_user_tend_to_reply": false,
#             "content_type": 1,
#             "is_folded": false,
#             "enter_from": "homepage_hot",
#             "can_create_item": true
#         },
#         {
#             "cid": "7569596772596712255",
#             "text": "现在女人说话难听都能算极端女权了[愉快]",
#             "aweme_id": "7568361402794287973",
#             "create_time": 1762434091,
#             "digg_count": 33,
#             "status": 1,
#             "user": {
#                 "uid": "12520492186",
#                 "short_id": "697793512",
#                 "nickname": "Aeuiin^",
#                 "avatar_thumb": {
#                     "uri": "100x100/aweme-avatar/tos-cn-avt-0015_cad393626f4550eb5df56b29e8f713fe",
#                     "url_list": [
#                         "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_cad393626f4550eb5df56b29e8f713fe.jpeg?from=2064092626"
#                     ],
#                     "width": 720,
#                     "height": 720
#                 },
#                 "follow_status": 0,
#                 "is_block": false,
#                 "custom_verify": "",
#                 "unique_id": "myonly557",
#                 "enterprise_verify_reason": "",
#                 "is_ad_fake": false,
#                 "profile_component_disabled": null,
#                 "region": "CN",
#                 "commerce_user_level": 0,
#                 "platform_sync_info": null,
#                 "secret": 0,
#                 "geofencing": null,
#                 "user_canceled": false,
#                 "status": 1,
#                 "follower_status": 0,
#                 "comment_setting": 0,
#                 "cover_url": null,
#                 "item_list": null,
#                 "new_story_cover": null,
#                 "is_star": false,
#                 "type_label": null,
#                 "ad_cover_url": null,
#                 "relative_users": null,
#                 "cha_list": null,
#                 "sec_uid": "MS4wLjABAAAAYDSEaAh5vE4vQfuxNbLBc0CtLONiSHu-pfywMl5NUV0",
#                 "need_points": null,
#                 "homepage_bottom_toast": null,
#                 "can_set_geofencing": null,
#                 "white_cover_url": null,
#                 "user_tags": null,
#                 "ban_user_functions": [],
#                 "aweme_control": {
#                     "can_forward": true,
#                     "can_share": true,
#                     "can_comment": true,
#                     "can_show_comment": true
#                 },
#                 "card_entries": null,
#                 "display_info": null,
#                 "card_entries_not_display": null,
#                 "card_sort_priority": null,
#                 "interest_tags": null,
#                 "link_item_list": null,
#                 "user_permissions": null,
#                 "offline_info_list": null,
#                 "is_blocking_v2": false,
#                 "is_blocked_v2": false,
#                 "close_friend_type": 0,
#                 "signature_extra": null,
#                 "personal_tag_list": null,
#                 "cf_list": null,
#                 "im_role_ids": null,
#                 "not_seen_item_id_list": null,
#                 "follower_list_secondary_information_struct": null,
#                 "endorsement_info_list": null,
#                 "text_extra": null,
#                 "contrail_list": null,
#                 "data_label_list": null,
#                 "not_seen_item_id_list_v2": null,
#                 "special_people_labels": null,
#                 "familiar_visitor_user": null,
#                 "avatar_schema_list": null,
#                 "profile_mob_params": null,
#                 "disable_image_comment_saved": 0,
#                 "verification_permission_ids": null,
#                 "batch_unfollow_relation_desc": null,
#                 "batch_unfollow_contain_tabs": null,
#                 "creator_tag_list": null,
#                 "private_relation_list": null,
#                 "identity_labels": null
#             },
#             "reply_id": "0",
#             "user_digged": 0,
#             "reply_comment": null,
#             "text_extra": [],
#             "label_text": "",
#             "label_type": -1,
#             "reply_comment_total": 3,
#             "reply_to_reply_id": "0",
#             "is_author_digged": false,
#             "stick_position": 0,
#             "user_buried": false,
#             "label_list": null,
#             "is_hot": false,
#             "text_music_info": null,
#             "image_list": null,
#             "is_note_comment": 0,
#             "ip_label": "河北",
#             "item_comment_total": 347,
#             "level": 1,
#             "video_list": null,
#             "sort_tags": "{\"bottom\":1,\"eco_level_2\":1,\"eco_level_10\":1,\"eco_level_11\":1,\"eco_level_1\":1,\"eco_level_5\":1,\"eco_level_8\":1}",
#             "is_user_tend_to_reply": false,
#             "content_type": 1,
#             "is_folded": false,
#             "enter_from": "homepage_hot"
#         },
#         {
#             "cid": "7575894960944366393",
#             "text": "",
#             "aweme_id": "7568361402794287973",
#             "create_time": 1763900501,
#             "digg_count": 0,
#             "status": 1,
#             "user": {
#                 "uid": "163155938385015",
#                 "short_id": "39727753773",
#                 "nickname": "小甜心不渝",
#                 "avatar_thumb": {
#                     "uri": "100x100/aweme-avatar/tos-cn-i-0813c000-ce_oQE7IAEAeoOvAHBzAiBxf2SnkA9AgiAweudEEK",
#                     "url_list": [
#                         "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c000-ce_oQE7IAEAeoOvAHBzAiBxf2SnkA9AgiAweudEEK.jpeg?from=2064092626"
#                     ],
#                     "width": 720,
#                     "height": 720
#                 },
#                 "follow_status": 0,
#                 "is_block": false,
#                 "custom_verify": "",
#                 "unique_id": "39727753773",
#                 "enterprise_verify_reason": "",
#                 "is_ad_fake": false,
#                 "profile_component_disabled": null,
#                 "region": "CN",
#                 "commerce_user_level": 0,
#                 "platform_sync_info": null,
#                 "secret": 0,
#                 "geofencing": null,
#                 "user_canceled": false,
#                 "status": 1,
#                 "follower_status": 0,
#                 "comment_setting": 0,
#                 "cover_url": null,
#                 "item_list": null,
#                 "new_story_cover": null,
#                 "is_star": false,
#                 "type_label": null,
#                 "ad_cover_url": null,
#                 "relative_users": null,
#                 "cha_list": null,
#                 "sec_uid": "MS4wLjABAAAAqyD7WGQQGFGrQmT1VcyqAmVVVfeZQBJhkHHMz-MzhtE",
#                 "need_points": null,
#                 "homepage_bottom_toast": null,
#                 "can_set_geofencing": null,
#                 "white_cover_url": null,
#                 "user_tags": null,
#                 "ban_user_functions": null,
#                 "aweme_control": {
#                     "can_forward": true,
#                     "can_share": true,
#                     "can_comment": true,
#                     "can_show_comment": true
#                 },
#                 "card_entries": null,
#                 "display_info": null,
#                 "card_entries_not_display": null,
#                 "card_sort_priority": null,
#                 "interest_tags": null,
#                 "link_item_list": null,
#                 "user_permissions": null,
#                 "offline_info_list": null,
#                 "is_blocking_v2": false,
#                 "is_blocked_v2": false,
#                 "close_friend_type": 0,
#                 "signature_extra": null,
#                 "personal_tag_list": null,
#                 "cf_list": null,
#                 "im_role_ids": null,
#                 "not_seen_item_id_list": null,
#                 "follower_list_secondary_information_struct": null,
#                 "endorsement_info_list": null,
#                 "text_extra": null,
#                 "contrail_list": null,
#                 "data_label_list": null,
#                 "not_seen_item_id_list_v2": null,
#                 "special_people_labels": null,
#                 "familiar_visitor_user": null,
#                 "avatar_schema_list": null,
#                 "profile_mob_params": null,
#                 "disable_image_comment_saved": 0,
#                 "verification_permission_ids": null,
#                 "batch_unfollow_relation_desc": null,
#                 "batch_unfollow_contain_tabs": null,
#                 "creator_tag_list": null,
#                 "private_relation_list": null,
#                 "identity_labels": null
#             },
#             "reply_id": "0",
#             "user_digged": 0,
#             "reply_comment": null,
#             "text_extra": [],
#             "label_text": "",
#             "label_type": -1,
#             "reply_comment_total": 0,
#             "reply_to_reply_id": "0",
#             "is_author_digged": false,
#             "sticker": {
#                 "id": "7453124173745881123",
#                 "width": 2000,
#                 "height": 2000,
#                 "static_url": {
#                     "uri": "tos-cn-o-0812/oYBDENEDA1fAqhJA0ntuyaqIPAFoexAb6yCnAg",
#                     "url_list": [
#                         "https://p26-sign.douyinpic.com/obj/tos-cn-o-0812/oYBDENEDA1fAqhJA0ntuyaqIPAFoexAb6yCnAg?lk3s=7b078dd2&x-expires=1764486000&x-signature=fEk7ISCMoO6Jsk6luWtQNLW3wOs%3D&from=2064092626&s=sticker_comment&se=false&sc=sticker_heif&biz_tag=aweme_comment&l=2025112914495021E923D282BD67161787",
#                         "https://p9-sign.douyinpic.com/obj/tos-cn-o-0812/oYBDENEDA1fAqhJA0ntuyaqIPAFoexAb6yCnAg?lk3s=7b078dd2&x-expires=1764486000&x-signature=xFG6AkAs7XXACSHGVi%2FyzDjkEZA%3D&from=2064092626&s=sticker_comment&se=false&sc=sticker_heif&biz_tag=aweme_comment&l=2025112914495021E923D282BD67161787",
#                         "https://p3-sign.douyinpic.com/obj/tos-cn-o-0812/oYBDENEDA1fAqhJA0ntuyaqIPAFoexAb6yCnAg?lk3s=7b078dd2&x-expires=1764486000&x-signature=FiO8Gw2izg07WqxPzvdvmx8NY%2BU%3D&from=2064092626&s=sticker_comment&se=false&sc=sticker_heif&biz_tag=aweme_comment&l=2025112914495021E923D282BD67161787"
#                     ],
#                     "width": 2000,
#                     "height": 2000
#                 },
#                 "animate_url": {
#                     "uri": "tos-cn-o-0812/oYBDENEDA1fAqhJA0ntuyaqIPAFoexAb6yCnAg",
#                     "url_list": [
#                         "https://p26-sign.douyinpic.com/obj/tos-cn-o-0812/oYBDENEDA1fAqhJA0ntuyaqIPAFoexAb6yCnAg?lk3s=7b078dd2&x-expires=1764486000&x-signature=fEk7ISCMoO6Jsk6luWtQNLW3wOs%3D&from=2064092626&s=sticker_comment&se=false&sc=sticker_heif&biz_tag=aweme_comment&l=2025112914495021E923D282BD67161787",
#                         "https://p9-sign.douyinpic.com/obj/tos-cn-o-0812/oYBDENEDA1fAqhJA0ntuyaqIPAFoexAb6yCnAg?lk3s=7b078dd2&x-expires=1764486000&x-signature=xFG6AkAs7XXACSHGVi%2FyzDjkEZA%3D&from=2064092626&s=sticker_comment&se=false&sc=sticker_heif&biz_tag=aweme_comment&l=2025112914495021E923D282BD67161787",
#                         "https://p3-sign.douyinpic.com/obj/tos-cn-o-0812/oYBDENEDA1fAqhJA0ntuyaqIPAFoexAb6yCnAg?lk3s=7b078dd2&x-expires=1764486000&x-signature=FiO8Gw2izg07WqxPzvdvmx8NY%2BU%3D&from=2064092626&s=sticker_comment&se=false&sc=sticker_heif&biz_tag=aweme_comment&l=2025112914495021E923D282BD67161787"
#                     ],
#                     "width": 2000,
#                     "height": 2000
#                 },
#                 "sticker_type": 2,
#                 "origin_package_id": "-1151911032521140",
#                 "id_str": "7453124173745881123",
#                 "author_sec_uid": "",
#                 "activity_schema": "",
#                 "activity_desc": ""
#             },
#             "stick_position": 0,
#             "user_buried": false,
#             "label_list": null,
#             "is_hot": false,
#             "text_music_info": null,
#             "image_list": null,
#             "is_note_comment": 0,
#             "ip_label": "福建",
#             "item_comment_total": 347,
#             "level": 1,
#             "video_list": null,
#             "sort_tags": "{\"bottom\":1}",
#             "is_user_tend_to_reply": false,
#             "content_type": 2,
#             "is_folded": false,
#             "enter_from": "homepage_hot"
#         },
#         {
#             "cid": "7573109946775913257",
#             "text": "[抱抱你][抱抱你][抱抱你]",
#             "aweme_id": "7568361402794287973",
#             "create_time": 1763252068,
#             "digg_count": 0,
#             "status": 1,
#             "user": {
#                 "uid": "104822493241",
#                 "short_id": "3643631342",
#                 "nickname": "୧⍤⃝耶",
#                 "avatar_thumb": {
#                     "uri": "100x100/aweme-avatar/tos-cn-i-0813c001_oUAATZBAgiIpA6HZnaB5IgvGaP2RAkBVAipEq",
#                     "url_list": [
#                         "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c001_oUAATZBAgiIpA6HZnaB5IgvGaP2RAkBVAipEq.jpeg?from=2064092626"
#                     ],
#                     "width": 720,
#                     "height": 720
#                 },
#                 "follow_status": 0,
#                 "is_block": false,
#                 "custom_verify": "",
#                 "unique_id": "shadow0799",
#                 "enterprise_verify_reason": "",
#                 "is_ad_fake": false,
#                 "profile_component_disabled": null,
#                 "region": "CN",
#                 "commerce_user_level": 0,
#                 "platform_sync_info": null,
#                 "secret": 0,
#                 "geofencing": null,
#                 "user_canceled": false,
#                 "status": 1,
#                 "follower_status": 0,
#                 "comment_setting": 0,
#                 "cover_url": null,
#                 "item_list": null,
#                 "new_story_cover": null,
#                 "is_star": false,
#                 "type_label": null,
#                 "ad_cover_url": null,
#                 "relative_users": null,
#                 "cha_list": null,
#                 "sec_uid": "MS4wLjABAAAAfu996DjEHtByVWssaLSPA7XzRxSHggK4UgZH5U0lShw",
#                 "need_points": null,
#                 "homepage_bottom_toast": null,
#                 "can_set_geofencing": null,
#                 "white_cover_url": null,
#                 "user_tags": null,
#                 "ban_user_functions": null,
#                 "aweme_control": {
#                     "can_forward": true,
#                     "can_share": true,
#                     "can_comment": true,
#                     "can_show_comment": true
#                 },
#                 "card_entries": null,
#                 "display_info": null,
#                 "card_entries_not_display": null,
#                 "card_sort_priority": null,
#                 "interest_tags": null,
#                 "link_item_list": null,
#                 "user_permissions": null,
#                 "offline_info_list": null,
#                 "is_blocking_v2": false,
#                 "is_blocked_v2": false,
#                 "close_friend_type": 0,
#                 "signature_extra": null,
#                 "personal_tag_list": null,
#                 "cf_list": null,
#                 "im_role_ids": null,
#                 "not_seen_item_id_list": null,
#                 "follower_list_secondary_information_struct": null,
#                 "endorsement_info_list": null,
#                 "text_extra": null,
#                 "contrail_list": null,
#                 "data_label_list": null,
#                 "not_seen_item_id_list_v2": null,
#                 "special_people_labels": null,
#                 "familiar_visitor_user": null,
#                 "avatar_schema_list": null,
#                 "profile_mob_params": null,
#                 "disable_image_comment_saved": 0,
#                 "verification_permission_ids": null,
#                 "batch_unfollow_relation_desc": null,
#                 "batch_unfollow_contain_tabs": null,
#                 "creator_tag_list": null,
#                 "private_relation_list": null,
#                 "identity_labels": null
#             },
#             "reply_id": "0",
#             "user_digged": 0,
#             "reply_comment": null,
#             "text_extra": [],
#             "label_text": "",
#             "label_type": -1,
#             "reply_comment_total": 0,
#             "reply_to_reply_id": "0",
#             "is_author_digged": false,
#             "stick_position": 0,
#             "user_buried": false,
#             "label_list": null,
#             "is_hot": false,
#             "text_music_info": null,
#             "image_list": null,
#             "is_note_comment": 0,
#             "ip_label": "陕西",
#             "item_comment_total": 347,
#             "level": 1,
#             "video_list": null,
#             "sort_tags": "{\"bottom\":1}",
#             "is_user_tend_to_reply": false,
#             "content_type": 1,
#             "is_folded": false,
#             "enter_from": "homepage_hot"
#         }
#     ],
#     "cursor": 180,
#     "has_more": 0,
#     "reply_style": 2,
#     "total": 347,
#     "extra": {
#         "now": 1764398990000,
#         "fatal_item_ids": null,
#         "scenes": null
#     },
#     "log_pb": {
#         "impr_id": "2025112914495021E923D282BD67161787"
#     },
#     "hotsoon_filtered_count": 0,
#     "user_commented": -1,
#     "fast_response_comment": {
#         "constant_response_words": [
#             "赞",
#             "比心",
#             "加油"
#         ],
#         "timed_response_words": [
#             "早上好",
#             "下午好",
#             "晚上好"
#         # 由于篇幅限制，我在实际代码中会使用完整数据
#     ]
# },
#     "comment_config": {},
#     "general_comment_config": {},
#     "show_management_entry_point": 0,
#     "folded_comment_count": 0
# }

def extract_comments_info(comments_data):
    """提取评论信息"""
    comments_list = []

    for comment in comments_data['comments']:
        # 跳过空文本评论
        if not comment.get('text', '').strip():
            continue

        comment_info = {
            'cid': comment['cid'],
            'text': comment['text'],
            'create_time': datetime.fromtimestamp(comment['create_time']),
            'digg_count': comment['digg_count'],
            'user_nickname': comment['user']['nickname'],
            'ip_label': comment.get('ip_label', '未知'),
            'reply_comment_total': comment.get('reply_comment_total', 0)
        }
        comments_list.append(comment_info)

    return pd.DataFrame(comments_list)


# 创建DataFrame
df = extract_comments_info(comments_data)
print("数据概览:")
print(f"总评论数: {len(df)}")
print(f"时间范围: {df['create_time'].min()} 到 {df['create_time'].max()}")
print("\n前5条评论:")
print(df[['text', 'digg_count', 'ip_label']].head())

# 1. 点赞数分布可视化
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.hist(df['digg_count'], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('评论点赞数分布')
plt.xlabel('点赞数')
plt.ylabel('频次')
plt.grid(True, alpha=0.3)

# 2. 地域分布
plt.subplot(2, 3, 2)
region_counts = df['ip_label'].value_counts()
plt.pie(region_counts.values, labels=region_counts.index, autopct='%1.1f%%')
plt.title('评论地域分布')

# 3. 文本长度分析
df['text_length'] = df['text'].str.len()
plt.subplot(2, 3, 3)
plt.hist(df['text_length'], bins=15, alpha=0.7, color='lightgreen', edgecolor='black')
plt.title('评论文本长度分布')
plt.xlabel('文本长度')
plt.ylabel('频次')
plt.grid(True, alpha=0.3)

# 4. 点赞数与文本长度关系
plt.subplot(2, 3, 4)
plt.scatter(df['text_length'], df['digg_count'], alpha=0.6, color='coral')
plt.title('文本长度 vs 点赞数')
plt.xlabel('文本长度')
plt.ylabel('点赞数')
plt.grid(True, alpha=0.3)

# 5. 时间趋势分析
plt.subplot(2, 3, 5)
df['date'] = df['create_time'].dt.date
daily_comments = df.groupby('date').size()
plt.plot(daily_comments.index, daily_comments.values, marker='o', linewidth=2)
plt.title('每日评论数量趋势')
plt.xlabel('日期')
plt.ylabel('评论数')
plt.xticks(rotation=45)

# 6. 高点赞评论分析
plt.subplot(2, 3, 6)
top_comments = df.nlargest(5, 'digg_count')[['text', 'digg_count', 'ip_label']]
# 简化文本显示
top_comments['short_text'] = top_comments['text'].str[:10] + '...'
y_pos = range(len(top_comments))
plt.barh(y_pos, top_comments['digg_count'])
plt.yticks(y_pos, top_comments['short_text'])
plt.title('高点赞评论TOP5')
plt.xlabel('点赞数')

plt.tight_layout()
plt.show()


# 文本内容分析
def analyze_text_content(df):
    """分析文本内容"""
    # 合并所有文本
    all_text = ' '.join(df['text'].dropna())

    # 使用jieba分词
    words = jieba.cut(all_text)

    # 过滤停用词和短词
    stop_words = {'的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个', '上', '也', '很',
                  '到', '说', '要', '去', '你', '会', '着', '没有', '看', '好', '自己', '这'}
    filtered_words = [word for word in words if len(word) > 1 and word not in stop_words]

    # 词频统计
    word_freq = Counter(filtered_words)

    return word_freq


# 生成词云
def generate_wordcloud(word_freq):
    """生成词云图"""
    wordcloud = WordCloud(
        font_path='simhei.ttf',
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


# 情感倾向分析（简单版）
def simple_sentiment_analysis(df):
    """简单情感分析"""
    positive_words = ['支持', '好', '喜欢', '赞', '棒', '优秀', '感谢', '爱', '美丽', '开心']
    negative_words = ['反对', '不好', '讨厌', '垃圾', '恶心', '恨', '丑陋', '伤心', '极端', '流血', '牺牲']

    sentiments = []
    for text in df['text']:
        pos_count = sum(1 for word in positive_words if word in text)
        neg_count = sum(1 for word in negative_words if word in text)

        if pos_count > neg_count:
            sentiments.append('积极')
        elif neg_count > pos_count:
            sentiments.append('消极')
        else:
            sentiments.append('中性')

    df['sentiment'] = sentiments
    return df


# 执行分析
print("\n=== 文本分析 ===")
word_freq = analyze_text_content(df)
print("高频词汇TOP10:")
for word, count in word_freq.most_common(10):
    print(f"{word}: {count}次")

# 生成词云
generate_wordcloud(word_freq)

# 情感分析
df = simple_sentiment_analysis(df)

# 情感分布可视化
plt.figure(figsize=(10, 6))
sentiment_counts = df['sentiment'].value_counts()
plt.bar(sentiment_counts.index, sentiment_counts.values, color=['green', 'gray', 'red'])
plt.title('评论情感分布')
plt.ylabel('评论数量')
for i, v in enumerate(sentiment_counts.values):
    plt.text(i, v + 0.1, str(v), ha='center', va='bottom')
plt.show()

# 详细数据报告
print("\n=== 详细数据报告 ===")
print(f"总评论数: {len(df)}")
print(f"总点赞数: {df['digg_count'].sum()}")
print(f"平均点赞数: {df['digg_count'].mean():.2f}")
print(f"涉及地域数量: {df['ip_label'].nunique()}")
print(f"最长评论: {df.loc[df['text_length'].idxmax(), 'text'][:50]}...")
print(f"最高点赞评论: {df.loc[df['digg_count'].idxmax(), 'text']}")

# 地域分析详情
print("\n=== 地域分析 ===")
region_analysis = df.groupby('ip_label').agg({
    'digg_count': ['count', 'sum', 'mean'],
    'text_length': 'mean'
}).round(2)
print(region_analysis)