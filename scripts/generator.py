"""
短视频脚本生成器
核心功能：生成爆款短视频脚本
"""

import random
from typing import Optional, List, Dict
from .formulas import (
    TITLE_TEMPLATES, HOOK_TEMPLATES, STRUCTURE_TEMPLATES,
    get_title_templates, get_hook_templates, get_structure_template, fill_template
)
from .platforms import get_platform_config, get_platform_tags


class ScriptGenerator:
    """短视频脚本生成器"""
    
    def __init__(self):
        self.platform_config = {
            "douyin": get_platform_config("douyin"),
            "xiaohongshu": get_platform_config("xiaohongshu"),
            "kuaishou": get_platform_config("kuaishou"),
        }
    
    def generate_script(
        self,
        topic: str,
        platform: str = "douyin",
        style: str = "干货",
        duration: str = "30s"
    ) -> Dict:
        """
        生成完整的短视频脚本
        
        Args:
            topic: 视频主题
            platform: 目标平台 (douyin/xiaohongshu/kuaishou)
            style: 内容风格 (干货/情感/搞笑/种草)
            duration: 视频时长 (15s/30s/60s)
        
        Returns:
            包含脚本、标题、标签等完整内容
        """
        platform = platform.lower()
        config = get_platform_config(platform)
        structure = get_structure_template(platform)
        
        # 生成标题
        titles = self.generate_titles(topic, platform, count=3)
        
        # 生成开头钩子
        hook = self.generate_hook(topic, platform)
        
        # 生成完整脚本
        script = self._generate_script_content(
            topic=topic,
            platform=platform,
            style=style,
            hook=hook,
            structure=structure
        )
        
        # 生成标签
        tags = self.generate_tags(topic, platform, count=10)
        
        # 生成分镜描述
        storyboard = self._generate_storyboard(script, duration)
        
        return {
            "titles": titles,
            "main_script": script,
            "storyboard": storyboard,
            "tags": tags,
            "hook": hook,
            "platform": platform,
            "style": style,
            "duration": duration
        }
    
    def generate_titles(
        self,
        topic: str,
        platform: str = "douyin",
        count: int = 3
    ) -> List[str]:
        """
        生成爆款标题
        
        Args:
            topic: 视频主题
            platform: 目标平台
            count: 生成数量
        
        Returns:
            标题列表
        """
        config = get_platform_config(platform)
        title_styles = config.get("title_style", ["数字"])
        
        titles = []
        for _ in range(count):
            style = random.choice(title_styles)
            style_templates = TITLE_TEMPLATES.get(style, TITLE_TEMPLATES["数字"])
            template = random.choice(style_templates)
            
            # 根据主题填充模板
            title = self._fill_title_template(template, topic)
            titles.append(title)
        
        return titles
    
    def generate_hook(
        self,
        topic: str,
        platform: str = "douyin"
    ) -> str:
        """
        生成3秒开头钩子
        
        Args:
            topic: 视频主题
            platform: 目标平台
        
        Returns:
            钩子文案
        """
        config = get_platform_config(platform)
        hook_styles = config.get("hooks_style", ["震惊"])
        
        style = random.choice(hook_styles)
        hook_templates = HOOK_TEMPLATES.get(style, HOOK_TEMPLATES["震惊"])
        template = random.choice(hook_templates)
        
        # 填充模板
        hook = self._fill_hook_template(template, topic)
        return hook
    
    def generate_tags(
        self,
        topic: str,
        platform: str = "douyin",
        count: int = 10
    ) -> List[str]:
        """
        生成推荐标签
        
        Args:
            topic: 视频主题
            platform: 目标平台
            count: 标签数量
        
        Returns:
            标签列表
        """
        config = get_platform_config(platform)
        base_tags = config.get("popular_tags", [])
        
        # 根据主题生成相关标签
        topic_tags = self._generate_topic_tags(topic)
        
        # 合并并随机选择
        all_tags = list(set(base_tags + topic_tags))
        selected_tags = random.sample(all_tags, min(count, len(all_tags)))
        
        return selected_tags
    
    def adapt_platform(
        self,
        original_script: str,
        target_platform: str,
        source_platform: str = "douyin"
    ) -> Dict:
        """
        跨平台脚本适配
        
        Args:
            original_script: 原脚本
            target_platform: 目标平台
            source_platform: 源平台
        
        Returns:
            适配后的脚本内容
        """
        target_config = get_platform_config(target_platform)
        source_config = get_platform_config(source_platform)
        
        # 调整内容风格
        adapted_content = self._adapt_content(
            original_script,
            source_config,
            target_config
        )
        
        # 生成适配后的标题
        titles = self.generate_titles(
            self._extract_topic(original_script),
            target_platform,
            count=3
        )
        
        # 生成适配后的标签
        tags = self.generate_tags(
            self._extract_topic(original_script),
            target_platform
        )
        
        return {
            "titles": titles,
            "script": adapted_content,
            "tags": tags,
            "source_platform": source_platform,
            "target_platform": target_platform
        }
    
    def batch_generate(
        self,
        topics: List[str],
        platform: str = "douyin",
        style: str = "干货",
        count_per_topic: int = 3
    ) -> List[Dict]:
        """
        批量生成脚本
        
        Args:
            topics: 主题列表
            platform: 目标平台
            style: 内容风格
            count_per_topic: 每个主题生成数量
        
        Returns:
            脚本列表
        """
        results = []
        for topic in topics:
            for _ in range(count_per_topic):
                script = self.generate_script(topic, platform, style)
                results.append(script)
        return results
    
    # ============ 私有方法 ============
    
    def _generate_script_content(
        self,
        topic: str,
        platform: str,
        style: str,
        hook: str,
        structure: Dict
    ) -> Dict:
        """生成脚本内容"""
        template = structure.get("template", "")
        
        # 根据不同风格生成内容
        if style == "干货":
            content = self._generate_knowledge_content(topic, platform)
        elif style == "情感":
            content = self._generate_emotion_content(topic, platform)
        elif style == "搞笑":
            content = self._generate_funny_content(topic, platform)
        elif style == "种草":
            content = self._generate_planting_content(topic, platform)
        else:
            content = self._generate_knowledge_content(topic, platform)
        
        # 填充结构模板
        filled_script = fill_template(
            template,
            hook=hook,
            **content
        )
        
        return {
            "structure": structure.get("name", ""),
            "content": filled_script,
            "steps": structure.get("steps", [])
        }
    
    def _generate_knowledge_content(self, topic: str, platform: str) -> Dict:
        """生成干货内容"""
        return {
            "setup": f"关于{topic}，你是不是也有这些困惑？",
            "solution": f"今天分享{topic}的核心要点，让你少走弯路",
            "showcase": f"学会这些{topic}技巧，效率提升翻倍",
            "summary": f"总结一下{topic}的关键点：记住这几点就够了",
            "cta": "觉得有用的话，点赞收藏支持一下"
        }
    
    def _generate_emotion_content(self, topic: str, platform: str) -> Dict:
        """生成情感内容"""
        return {
            "setup": f"关于{topic}，我有些话想说...",
            "solution": f"其实{topic}背后的原因，很多人不知道",
            "showcase": f"经历过才明白，{topic}的意义",
            "summary": f"希望每个在{topic}中的人，都能找到答案",
            "cta": "如果你也有同感，评论区说说你的故事"
        }
    
    def _generate_funny_content(self, topic: str, platform: str) -> Dict:
        """生成搞笑内容"""
        return {
            "setup": f"说到{topic}，我真的忍不住了...",
            "solution": f"你们有没有遇到过这种情况？{topic}的时候...",
            "showcase": f"当时我就震惊了，这{topic}也太...",
            "summary": f"最后提醒大家，{topic}一定要...",
            "cta": "你们遇到过更离谱的吗？评论区见"
        }
    
    def _generate_planting_content(self, topic: str, platform: str) -> Dict:
        """生成种草内容"""
        return {
            "identity": "作为一个资深{topic}爱好者",
            "painpoint": "之前一直在找好的{topic}，踩过不少坑",
            "solution": f"直到遇到这款{topic}，真的惊艳到我了",
            "effect": f"用了{topic}之后，效果真的太明显了",
            "summary": f"真心推荐给想入手{topic}的你们",
            "cta": "链接在评论区，喜欢的记得入手哦"
        }
    
    def _generate_storyboard(
        self,
        script: Dict,
        duration: str
    ) -> List[Dict]:
        """生成分镜描述"""
        steps = script.get("steps", [])
        storyboard = []
        
        duration_seconds = int(duration.replace("s", ""))
        
        for i, step in enumerate(steps):
            # 计算每个镜头的时长
            if i < len(steps) - 1:
                step_duration = duration_seconds // len(steps)
            else:
                step_duration = duration_seconds - sum(
                    [duration_seconds // len(steps)] * (len(steps) - 1)
                )
            
            storyboard.append({
                "scene": i + 1,
                "time": step.get("time", ""),
                "duration": f"{step_duration}s",
                "content": step.get("content", ""),
                "action": self._generate_action(step.get("name", "")),
                "camera": self._get_camera_shot(step.get("name", ""))
            })
        
        return storyboard
    
    def _generate_action(self, step_name: str) -> str:
        """生成动作描述"""
        actions = {
            "钩子": "特写面部表情，制造紧张感",
            "悬念": "近景+远景切换",
            "铺垫": "中景，环境交代",
            "科普": "配合图文讲解",
            "案例": "展示具体操作或效果",
            "故事": "分饰两角或情景演绎",
            "转折": "镜头快速切换",
            "反转": "突然定格或慢动作",
            "高潮": "情绪饱满，表情夸张",
            "总结": "镜头拉远，全景收尾",
            "结尾": "手势引导互动",
            "呼吁": "双手比心或点赞手势",
            "互动": "指向评论区",
            "开场": "真实场景出镜",
            "引入": "生活化场景带入",
            "问题": "皱眉思考表情",
            "方案": "展示具体方法",
            "效果": "前后对比展示"
        }
        return actions.get(step_name, "自然出镜，语速适中")
    
    def _get_camera_shot(self, step_name: str) -> str:
        """获取镜头建议"""
        shots = {
            "钩子": "特写/近景",
            "悬念": "近景",
            "铺垫": "中景",
            "科普": "中景+特写切换",
            "案例": "中景",
            "故事": "双人镜头",
            "转折": "快切",
            "反转": "特写+慢动作",
            "高潮": "近景",
            "总结": "中景",
            "结尾": "近景",
            "呼吁": "近景",
            "互动": "近景"
        }
        return shots.get(step_name, "中景")
    
    def _fill_title_template(self, template: str, topic: str) -> str:
        """填充标题模板"""
        replacements = {
            "{主题}": topic,
            "{数字}": str(random.randint(3, 9)),
            "{效果}": random.choice(["效率翻倍", "效果惊人", "太实用了", "太牛了"]),
            "{时间}": random.choice(["一个月", "一周", "三天", "一周内"]),
            "{技能}": topic,
            "{变化}": random.choice(["蜕变", "逆袭", "成长", "突破"]),
            "{避坑指南}": f"避开{topic}的坑",
            "{能力提升}": f"提升{topic}能力",
            "{道理}": f"关于{topic}的真相",
            "{名人}": random.choice(["明星", "网红", "大佬", "博主"]),
            "{方法}": topic,
            "{行为}": random.choice(["做了", "用了", "买了", "试了"]),
            "{热点事件}": random.choice(["最近很火", "刷屏了", "上热搜", "爆了"]),
            "{金钱}": f"{random.randint(1, 9)}百",
            "{倍数}": str(random.randint(2, 10)),
            "{起点}": random.choice(["小白", "新手", "普通人"]),
            "{终点}": random.choice(["大神", "专家", "达人"]),
        }
        result = template
        for key, value in replacements.items():
            result = result.replace(key, value)
        return result
    
    def _fill_hook_template(self, template: str, topic: str) -> str:
        """填充钩子模板"""
        replacements = {
            "{主题}": topic,
            "{数字}": str(random.randint(3, 9)),
            "{痛点}": f"为{topic}发愁",
            "{痛点行为}": random.choice([f"被{topic}困扰", f"做不好{topic}", f"找不到好的{topic}"]),
            "{失败行为}": random.choice([f"做{topic}", f"选{topic}", f"用{topic}"]),
            "{身份}": random.choice(["过来人", "从业者", "资深玩家", "踩坑达人"]),
            "{行为}": random.choice(["买", "做", "用", "试"]),
            "{场景}": random.choice(["这种情况", "这种问题", "这件事"]),
            "{场景行为}": random.choice([f"遇到{topic}问题", f"需要选择{topic}", f"做{topic}的时候"]),
            "{trigger行为}": random.choice([f"做{topic}", f"选{topic}", f"用{topic}"]),
        }
        result = template
        for key, value in replacements.items():
            result = result.replace(key, value)
        return result
    
    def _generate_topic_tags(self, topic: str) -> List[str]:
        """根据主题生成标签"""
        base_tags = [
            f"#{topic}", f"#关于{topic}", f"#{topic}技巧",
            f"#干货分享", f"#涨知识", f"#必看",
            f"#建议收藏", f"#种草", f"#好物推荐"
        ]
        return base_tags
    
    def _adapt_content(
        self,
        original_script: str,
        source_config: Dict,
        target_config: Dict
    ) -> str:
        """适配内容到目标平台"""
        # 根据目标平台调整语气和风格
        if target_config.get("name") == "小红书":
            return f"【真实分享】\n{original_script}\n\n姐妹们，这个真的太好用了！"
        elif target_config.get("name") == "快手":
            return f"老铁们好！\n{original_script}\n\n觉得有用的话，双击支持一下！"
        else:
            return original_script
    
    def _extract_topic(self, script: str) -> str:
        """从脚本中提取主题"""
        # 简单实现，实际可以从脚本中提取关键词
        return "视频主题"


# 导出主类
__all__ = ["ScriptGenerator"]
