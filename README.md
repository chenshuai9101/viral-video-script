# 🚀 短视频爆款文案生成器 (viral-video-script)

> 为自媒体创作者打造的爆款短视频脚本生成工具

## ✨ 功能特性

- 📱 **平台垂直适配** - 支持抖音、小红书、快手三大平台
- 📝 **爆款公式内置** - 100+标题模板、50+开头钩子、20+内容结构
- ⚡ **一键生成** - 输入主题即可生成完整脚本
- 🎬 **分镜描述** - 自动生成拍摄分镜建议
- 🏷️ **标签推荐** - 智能推荐平台热门标签

## 📦 安装

```bash
pip install -r requirements.txt
```

## 🚀 快速开始

### Python API 使用

```python
from scripts.generator import ScriptGenerator

# 初始化生成器
gen = ScriptGenerator()

# 生成抖音爆款脚本
result = gen.generate_script(
    topic="职场沟通技巧",
    platform="douyin",
    style="干货",
    duration="30s"
)

print(result["titles"])      # 爆款标题
print(result["main_script"]) # 完整脚本
print(result["tags"])        # 推荐标签
```

### 生成效果示例

```python
# 输入
topic = "职场沟通技巧"
platform = "douyin"
style = "干货"
duration = "30s"

# 输出示例
{
    "titles": [
        "学会这3点，职场沟通效率翻倍",
        "月薪8k的人都在用的沟通技巧",
        "为什么你说话总得罪人？"
    ],
    "main_script": {
        "structure": "抖音黄金结构",
        "content": "【开场钩子】\n你绝对想不到，职场沟通竟然...\n\n【问题铺垫】\n关于职场沟通，你是不是也有这些困惑？\n...",
        "steps": [...]
    },
    "storyboard": [...],
    "tags": ["#干货分享", "#职场技巧", "#涨知识", ...]
}
```

### 跨平台适配

```python
# 将抖音脚本适配到小红书
adapted = gen.adapt_platform(
    original_script="...",
    target_platform="xiaohongshu",
    source_platform="douyin"
)
```

### 批量生成

```python
# 一次生成多条脚本
results = gen.batch_generate(
    topics=["职场沟通", "时间管理", "情绪控制"],
    platform="douyin",
    style="干货",
    count_per_topic=5
)
```

## 📋 平台特性对比

| 平台 | 时长 | 风格 | 核心要素 |
|------|------|------|----------|
| 抖音 | 15-60秒 | 快节奏、情绪化 | 3秒钩子、爆点前置 |
| 小红书 | 30-90秒 | 种草风、生活化 | 真实分享、情感共鸣 |
| 快手 | 30-120秒 | 接地气、真实感 | 老铁文化、互动引导 |

## 📚 爆款公式库

### 标题公式
```
数字 + 痛点 + 承诺 = 高点击率标题
```

示例：
- 「揭秘」类：原来这才是...的真相
- 「数字」类：3个方法让你...
- 「对比」类：从...到...我只用了...
- 「悬念」类：没想到...竟然...

### 开头钩子
- 震惊体：99%的人都踩过这个坑！
- 痛点体：你是不是也经常...
- 数字体：只需3秒，教你...
- 冲突体：明明...为什么他...

### 内容结构
- 抖音黄金结构：钩子→铺垫→转折→高潮→结尾
- 小红书种草结构：引入→痛点→方案→效果→总结
- 快手分享结构：开场→故事→转折→高潮→呼吁

## 📁 项目结构

```
viral-video-script/
├── SKILL.md                 # Skill配置文件
├── README.md               # 项目说明文档
├── requirements.txt        # 依赖列表
└── scripts/
    ├── __init__.py         # 包初始化
    ├── generator.py        # 脚本生成器
    ├── formulas.py          # 爆款公式库
    └── platforms.py        # 平台特性配置
```

## 🔧 开发

```bash
# 克隆项目
git clone https://github.com/chenshuai9101/viral-video-script.git

# 进入目录
cd viral-video-script

# 安装依赖
pip install -r requirements.txt

# 运行测试
python -c "from scripts import ScriptGenerator; print('OK')"
```

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 联系方式

- GitHub: [chenshuai9101/viral-video-script](https://github.com/chenshuai9101/viral-video-script)
