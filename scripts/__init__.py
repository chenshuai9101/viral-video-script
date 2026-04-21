"""
短视频爆款文案生成器
v1.0

为自媒体创作者提供爆款短视频脚本生成服务
支持平台：抖音、小红书、快手
"""

from .generator import ScriptGenerator
from .formulas import (
    get_title_templates, get_hook_templates, 
    get_structure_template, fill_template
)
from .platforms import get_platform_config, get_platform_features

__version__ = "1.0"
__author__ = "viral-video-script"

__all__ = [
    "ScriptGenerator",
    "get_title_templates",
    "get_hook_templates",
    "get_structure_template",
    "fill_template",
    "get_platform_config",
    "get_platform_features",
]
