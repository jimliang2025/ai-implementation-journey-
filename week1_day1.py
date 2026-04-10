# Week 1 Day 1：数据读取基础
# 目标：用Python生成模拟数据并保存为Excel

import pandas as pd
from datetime import datetime, timedelta
import random

# 生成模拟销售数据（中文场景）
def generate_mock_data():
    customers = ['张三', '李四', '王五', '赵六', '陈七']
    products = ['笔记本电脑', '鼠标', '键盘', '显示器', '耳机']
    
    data = []
    for i in range(20):  # 生成20条记录
        record = {
            '客户姓名': random.choice(customers),
            '产品名称': random.choice(products),
            '销售金额': random.randint(100, 15000),
            '购买日期': datetime.now() - timedelta(days=random.randint(1, 30)),
            '是否付款': random.choice([True, False])
        }
        data.append(record)
    
    return pd.DataFrame(data)

# 主程序
if __name__ == "__main__":
    try:
        # 生成数据
        df = generate_mock_data()
        
        # 显示前5行
        print("=== 模拟销售数据 ===")
        print(df.head())
        print(f"\n共生成 {len(df)} 条记录")
        
        # 简单统计
        print(f"\n总销售额: {df['销售金额'].sum()} 元")
        print(f"平均客单价: {df['销售金额'].mean():.2f} 元")
        
        # 保存到Excel（带时间戳）
        filename = f"销售数据_{datetime.now().strftime('%m%d_%H%M')}.xlsx"
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"\n✅ 数据已保存至: {filename}")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        print("提示：如果提示缺少库，请运行: pip install pandas openpyxl")