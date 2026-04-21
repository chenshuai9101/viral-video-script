"""
短视频平台特性配置
根据各平台特性定制内容策略
"""

# 抖音平台配置
douyin_config = {
    "name": "抖音",
    "duration_range": (15, 60),
    "features": {
        "节奏": "快节奏、强刺激",
        "情绪": "情绪化、共鸣强",
        "开头": "3秒必须抓住注意力",
        "内容": "爆点前置、反转设置",
        "结尾": "强互动引导"
    },
    "script_structure": {
        "钩子": "0-3秒",
        "铺垫": "3-8秒",
        "转折": "8-20秒",
        "高潮": "20-45秒",
        "结尾": "45-60秒"
    },
    "title_style": ["震惊体", "数字体", "悬念体", "对比体"],
    "hooks_style": ["震惊式", "痛点式", "数字式", "冲突式"],
    "popular_tags": ["#爆款", "#干货", "#涨知识", "#必看", "#建议收藏"]
}

# 小红书平台配置
xiaohongshu_config = {
    "name": "小红书",
    "duration_range": (30, 90),
    "features": {
        "节奏": "生活化、有温度",
        "情绪": "情感共鸣、利他性强",
        "开头": "场景化引入、建立身份认同",
        "内容": "真实分享、干货价值",
        "结尾": "种草推荐、收藏引导"
    },
    "script_structure": {
        "引入": "0-10秒",
        "问题": "10-25秒",
        "方案": "25-50秒",
        "效果": "50-70秒",
        "总结": "70-90秒"
    },
    "title_style": ["种草体", "攻略体", "分享体", "测评体"],
    "hooks_style": ["身份式", "场景式", "问题式", "分享式"],
    "popular_tags": ["#好物推荐", "#干货分享", "#种草", "#真实测评", "#必买"]
}

# 快手平台配置
kuaishou_config = {
    "name": "快手",
    "duration_range": (30, 120),
    "features": {
        "节奏": "接地气、不做作",
        "情绪": "真实感、亲切感",
        "开头": "真实场景、接地气开场",
        "内容": "老铁文化、情感连接",
        "结尾": "互动引导、关注引导"
    },
    "script_structure": {
        "开场": "0-10秒",
        "故事": "10-40秒",
        "转折": "40-70秒",
        "高潮": "70-100秒",
        "呼吁": "100-120秒"
    },
    "title_style": ["真实体", "故事体", "分享体", "经验体"],
    "hooks_style": ["真实式", "故事式", "自述式", "分享式"],
    "popular_tags": ["#老铁", "#真实分享", "#经验之谈", "#推荐", "#关注"]
}

# 平台配置映射
PLATFORM_CONFIG = {
    "douyin": douyin_config,
    "xiaohongshu": xiaohongshu_config,
    "kuaishou": kuaishou_config
}

def get_platform_config(platform: str) -> dict:
    """获取平台配置"""
    return PLATFORM_CONFIG.get(platform.lower(), douyin_config)

def get_platform_features(platform: str) -> dict:
    """获取平台特性"""
    config = get_platform_config(platform)
    return config.get("features", {})

def get_platform_structure(platform: str) -> dict:
    """获取平台内容结构"""
    config = get_platform_config(platform)
    return config.get("script_structure", {})

def get_platform_tags(platform: str) -> list:
    """获取平台常用标签"""
    config = get_platform_config(platform)
    return config.get("popular_tags", [])
