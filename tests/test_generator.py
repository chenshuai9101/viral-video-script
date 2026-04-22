#!/usr/bin/env python3
"""
Viral-Video-Script 测试用例
验证脚本生成、标题生成、标签推荐功能
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scripts.generator import ScriptGenerator
from scripts.formulas import TITLE_TEMPLATES, HOOK_TEMPLATES, STRUCTURE_TEMPLATES
from scripts.platforms import PLATFORM_CONFIG

def test_generator_init():
    """测试生成器初始化"""
    print("=== 测试: 生成器初始化 ===")
    gen = ScriptGenerator()
    assert gen is not None
    assert "douyin" in gen.platform_config
    print("✅ 生成器初始化成功")
    return True

def test_generate_script():
    """测试完整脚本生成"""
    print("\n=== 测试: 完整脚本生成 ===")
    gen = ScriptGenerator()
    
    result = gen.generate_script(
        topic="职场沟通技巧",
        platform="douyin",
        style="干货",
        duration="30s"
    )
    
    assert "titles" in result
    assert "main_script" in result
    assert "tags" in result
    
    print(f"✅ 脚本生成成功")
    print(f"   标题数: {len(result['titles'])}")
    print(f"   标签数: {len(result['tags'])}")
    
    return True

def test_generate_titles():
    """测试标题生成"""
    print("\n=== 测试: 标题生成 ===")
    gen = ScriptGenerator()
    
    titles = gen.generate_titles("Python编程", "douyin", count=3)
    assert len(titles) == 3
    print(f"  标题: {titles}")
    
    print("✅ 标题生成功能正常")
    return True

def test_formulas():
    """测试爆款公式库"""
    print("\n=== 测试: 爆款公式库 ===")
    
    for style, templates in TITLE_TEMPLATES.items():
        assert len(templates) > 0
        print(f"  {style}类标题: {len(templates)}个模板")
    
    print("✅ 爆款公式库完整")
    return True

def test_platform_configs():
    """测试平台配置"""
    print("\n=== 测试: 平台配置 ===")
    
    for platform, config in PLATFORM_CONFIG.items():
        assert "name" in config
        print(f"  [{platform}] {config['name']}")
    
    print("✅ 平台配置完整")
    return True

def run_all_tests():
    """运行所有测试"""
    print("=" * 50)
    print("Viral-Video-Script 测试套件")
    print("=" * 50)
    
    tests = [
        test_generator_init,
        test_generate_script,
        test_generate_titles,
        test_formulas,
        test_platform_configs,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ 测试失败: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"测试结果: {passed} 通过, {failed} 失败")
    print("=" * 50)
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
