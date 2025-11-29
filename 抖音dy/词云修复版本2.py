import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import jieba
from collections import Counter
import json
from datetime import datetime
import os
import warnings
import matplotlib as mpl


# 彻底解决中文显示问题
def setup_chinese_font_comprehensive():
    """全面设置中文字体"""
    try:
        # 方法1: 尝试macOS系统字体
        mac_fonts = [
            'PingFang SC',
            'Hiragino Sans GB',
            'Heiti SC',
            'Arial Unicode MS',
            'STHeiti',
            'Microsoft YaHei'
        ]

        # 检查系统字体
        available_fonts = []
        for font in mac_fonts:
            try:
                test_font = mpl.font_manager.FontProperties(family=font)
                if mpl.font_manager.findfont(test_font) != test_font.get_name():
                    available_fonts.append(font)
            except:
                continue

        if available_fonts:
            plt.rcParams['font.sans-serif'] = available_fonts + ['DejaVu Sans']
            print(f"✅ 使用系统字体: {available_fonts[0]}")
        else:
            # 方法2: 使用matplotlib的默认字体，但用英文标签
            plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
            print("⚠️  使用英文标签（系统缺少中文字体）")

        plt.rcParams['axes.unicode_minus'] = False

    except Exception as e:
        print(f"字体设置失败: {e}")
        plt.rcParams['font.sans-serif'] = ['DejaVu Sans']


# 初始化字体设置
setup_chinese_font_comprehensive()

# 忽略警告
warnings.filterwarnings('ignore')

# # 提取评论数据

# 1. 将数据保存为data.json文件
# 2. 使用以下代码加载
import json
with open('data.json', 'r', encoding='utf-8') as f:
    comments_data = json.load(f)  # 会自动转换false/null


def safe_extract_comments(data):
    """安全提取评论信息"""
    comments_list = []

    if not data or 'comments' not in data:
        print("错误：数据格式不正确")
        return pd.DataFrame()

    comments = data['comments']
    print(f"找到 {len(comments)} 条评论")

    for i, comment in enumerate(comments):
        try:
            if 'create_time' not in comment or 'text' not in comment:
                continue

            comment_info = {
                'cid': comment.get('cid', f'unknown_{i}'),
                'text': str(comment.get('text', '')),
                'create_time': comment.get('create_time'),
                'digg_count': comment.get('digg_count', 0),
                'user_nickname': comment.get('user', {}).get('nickname', '未知用户'),
                'ip_label': comment.get('ip_label', '未知地区'),
                'reply_comment_total': comment.get('reply_comment_total', 0)
            }

            try:
                comment_info['create_time'] = datetime.fromtimestamp(comment_info['create_time'])
            except:
                comment_info['create_time'] = datetime.now()

            comments_list.append(comment_info)

        except Exception as e:
            print(f"处理第{i + 1}条评论时出错: {e}")
            continue

    return pd.DataFrame(comments_list)


def create_chinese_visualizations(df):
    """创建中文可视化图表"""
    if df.empty:
        print("没有数据可分析")
        return

    # 创建图形
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # 1. 点赞数分布 - 使用中文标题
    axes[0, 0].hist(df['digg_count'], bins=20, alpha=0.7, color='#1f77b4', edgecolor='black')
    axes[0, 0].set_title('评论点赞数分布', fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('点赞数')
    axes[0, 0].set_ylabel('评论数量')
    axes[0, 0].grid(True, alpha=0.3)

    # 2. 地域分布 - 直接使用中文
    region_counts = df['ip_label'].value_counts().head(8)
    bars = axes[0, 1].bar(range(len(region_counts)), region_counts.values,
                          color=['#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                                 '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22'])
    axes[0, 1].set_title('评论地域分布TOP8', fontsize=14, fontweight='bold')
    axes[0, 1].set_ylabel('评论数量')
    axes[0, 1].set_xticks(range(len(region_counts)))
    axes[0, 1].set_xticklabels(region_counts.index, rotation=45, ha='right')

    # 在柱状图上显示数值
    for bar, count in zip(bars, region_counts.values):
        height = bar.get_height()
        axes[0, 1].text(bar.get_x() + bar.get_width() / 2., height,
                        f'{count}', ha='center', va='bottom')

    # 3. 文本长度分析
    df['text_length'] = df['text'].str.len()
    axes[1, 0].hist(df['text_length'], bins=15, alpha=0.7, color='#2ca02c', edgecolor='black')
    axes[1, 0].set_title('评论文本长度分布', fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('文本长度（字符数）')
    axes[1, 0].set_ylabel('评论数量')
    axes[1, 0].grid(True, alpha=0.3)

    # 4. 高点赞评论 - 使用编号代替长文本
    top_comments = df.nlargest(5, 'digg_count')[['digg_count', 'ip_label']].copy()
    y_pos = range(len(top_comments))
    bars = axes[1, 1].barh(y_pos, top_comments['digg_count'], color='#ff7f0e')
    axes[1, 1].set_yticks(y_pos)
    # 使用简短标签
    labels = [f'评论{i + 1}[{top_comments.iloc[i]["ip_label"]}]' for i in range(len(top_comments))]
    axes[1, 1].set_yticklabels(labels)
    axes[1, 1].set_title('高点赞评论TOP5', fontsize=14, fontweight='bold')
    axes[1, 1].set_xlabel('点赞数')

    # 在条形图上显示数值
    for bar, count in zip(bars, top_comments['digg_count']):
        width = bar.get_width()
        axes[1, 1].text(width, bar.get_y() + bar.get_height() / 2.,
                        f'{count}', ha='left', va='center', fontweight='bold')

    plt.tight_layout()
    # 在plt.show()之前添加
    # 保存词云图片
    plt.savefig('analysis_chart.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

    # 单独显示高点赞评论内容
    print("\n📋 高点赞评论详情:")
    top_comments_detail = df.nlargest(5, 'digg_count')[['text', 'digg_count', 'ip_label']]
    for i, (idx, row) in enumerate(top_comments_detail.iterrows()):
        print(f"{i + 1}. [{row['ip_label']}] 👍{row['digg_count']}")
        print(f"   {row['text']}")
        print()


def create_advanced_wordcloud(df):
    """创建高级词云（解决中文问题）"""
    try:
        # 文本处理
        all_text = ' '.join(df['text'].astype(str))
        words = jieba.cut(all_text)

        # 扩展停用词列表
        stop_words = {
            '的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一',
            '一个', '上', '也', '很', '到', '说', '要', '去', '你', '会', '着',
            '没有', '看', '好', '自己', '这', '那', '她', '他', '它', '我们', '你们',
            '他们', '这个', '那个', '这些', '那些', '这样', '那样', '这里', '那里'
        }

        filtered_words = [word for word in words if len(word) > 1 and word not in stop_words]
        word_freq = Counter(filtered_words)

        print("🎨 生成高级词云...")

        # macOS 字体路径
        font_paths = [
            '/System/Library/Fonts/PingFang.ttc',  # 苹方字体
            '/System/Library/Fonts/STHeiti Light.ttc',  # 华文黑体
            '/System/Library/Fonts/STHeiti Medium.ttc',
            '/Library/Fonts/Arial Unicode.ttf',
            None  # 使用默认字体
        ]

        wordcloud = None
        used_font = "默认字体"

        for font_path in font_paths:
            try:
                if font_path and os.path.exists(font_path):
                    wordcloud = WordCloud(
                        font_path=font_path,
                        width=1000,
                        height=600,
                        background_color='white',
                        max_words=150,
                        colormap='viridis',
                        relative_scaling=0.5,
                        stopwords=set(),  # 我们已经手动过滤了
                        collocations=False
                    ).generate_from_frequencies(word_freq)
                    used_font = os.path.basename(font_path)
                    print(f"✅ 使用字体: {used_font}")
                    break
                elif font_path is None:
                    wordcloud = WordCloud(
                        width=1000,
                        height=600,
                        background_color='white',
                        max_words=150,
                        colormap='viridis'
                    ).generate_from_frequencies(word_freq)
                    used_font = "系统默认"
                    print("ℹ️  使用默认字体")
                    break
            except Exception as e:
                continue

        if wordcloud:
            # 创建更大的图形
            plt.figure(figsize=(16, 9))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.title('抖音评论关键词词云分析', fontsize=20, fontweight='bold', pad=20)
            plt.tight_layout()
            plt.show()

            # 显示词频统计
            print("\n📊 词频统计TOP15:")
            for i, (word, count) in enumerate(word_freq.most_common(15)):
                print(f"   {i + 1:2d}. {word}: {count}次")

        else:
            print("❌ 词云生成失败，跳过...")

    except Exception as e:
        print(f"❌ 生成词云时出错: {e}")


def create_sentiment_analysis(df):
    """简单情感分析"""
    print("\n😊 情感倾向分析:")

    # 简单关键词情感分析
    positive_words = ['支持', '好', '喜欢', '赞', '棒', '优秀', '感谢', '爱', '美丽', '开心', '加油']
    negative_words = ['反对', '不好', '讨厌', '垃圾', '恶心', '恨', '丑陋', '伤心', '流血', '牺牲', '骂']

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

    # 情感分布
    sentiment_counts = df['sentiment'].value_counts()
    print("情感分布:")
    for sentiment, count in sentiment_counts.items():
        percentage = (count / len(df)) * 100
        print(f"  {sentiment}: {count}条 ({percentage:.1f}%)")

    # 情感与点赞的关系
    print("\n情感与点赞数关系:")
    sentiment_stats = df.groupby('sentiment')['digg_count'].agg(['mean', 'max', 'count'])
    print(sentiment_stats.round(2))


def save_enhanced_report(df):
    """保存增强版分析报告"""
    try:
        with open('抖音评论深度分析报告.txt', 'w', encoding='utf-8') as f:
            f.write("抖音评论深度分析报告\n")
            f.write("=" * 60 + "\n\n")

            f.write(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"总评论数: {len(df)}\n")
            f.write(f"总点赞数: {df['digg_count'].sum()}\n")
            f.write(f"平均点赞数: {df['digg_count'].mean():.2f}\n")
            f.write(f"评论时间范围: {df['create_time'].min()} 到 {df['create_time'].max()}\n\n")

            f.write("📊 基本统计分析\n")
            f.write("-" * 40 + "\n")
            f.write(f"最长评论: {df['text'].str.len().max()} 字符\n")
            f.write(f"最短评论: {df['text'].str.len().min()} 字符\n")
            f.write(f"平均评论长度: {df['text'].str.len().mean():.1f} 字符\n\n")

            f.write("🌍 地域分布分析\n")
            f.write("-" * 40 + "\n")
            for region, count in df['ip_label'].value_counts().items():
                percentage = (count / len(df)) * 100
                f.write(f"{region}: {count}条 ({percentage:.1f}%)\n")

            f.write("\n⭐ 高点赞评论分析\n")
            f.write("-" * 40 + "\n")
            top_comments = df.nlargest(10, 'digg_count')
            for i, (idx, row) in enumerate(top_comments.iterrows()):
                f.write(f"\n{i + 1}. [{row['ip_label']}] 👍{row['digg_count']}\n")
                f.write(f"   内容: {row['text']}\n")

            # 高频词汇分析
            all_text = ' '.join(df['text'].astype(str))
            words = jieba.cut(all_text)
            stop_words = {'的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一'}
            filtered_words = [word for word in words if len(word) > 1 and word not in stop_words]
            word_freq = Counter(filtered_words)

            f.write("\n🔤 高频词汇分析\n")
            f.write("-" * 40 + "\n")
            for i, (word, count) in enumerate(word_freq.most_common(25)):
                f.write(f"{i + 1:2d}. {word}: {count}次\n")

            # 用户分析
            f.write("\n👤 用户分析\n")
            f.write("-" * 40 + "\n")
            user_stats = df['user_nickname'].value_counts()
            f.write(f"总用户数: {len(user_stats)}\n")
            f.write("活跃用户TOP5:\n")
            for user, count in user_stats.head().items():
                f.write(f"  {user}: {count}条评论\n")

        print("📄 深度分析报告已保存到: 抖音评论深度分析报告.txt")
    except Exception as e:
        print(f"保存报告时出错: {e}")


# 主程序
def main():
    print("🚀 开始深度分析抖音评论数据...")

    # 提取数据
    df = safe_extract_comments(comments_data)

    if df.empty:
        print("❌ 没有提取到有效评论数据")
        return

    print(f"✅ 数据提取成功！共 {len(df)} 条评论")

    # 生成中文可视化图表
    print("\n📊 生成中文可视化图表...")
    create_chinese_visualizations(df)

    # 生成高级词云
    print("\n🎨 生成高级词云...")
    create_advanced_wordcloud(df)

    # 情感分析
    create_sentiment_analysis(df)

    # 保存增强版报告
    save_enhanced_report(df)

    print("\n🎉 深度分析完成！")
    print("💡 提示: 如果图表中文仍显示异常，请检查系统中文字体安装情况")


if __name__ == "__main__":
    main()