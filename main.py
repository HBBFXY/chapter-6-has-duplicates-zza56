def has_duplicates(lst):
    """判断列表中是否存在重复元素，存在则返回True，否则返回False"""
    return len(lst) != len(set(lst))


# 测试程序
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],       
        [1, 2, 3, 2, 5],       
        [],                     
        [10],                   
        ["a", "b", "a"],        
        [1.5, 2.5, 1.5, 3.5],  
        [True, False, True]     
    ]
    
    print("重复元素判定测试结果：")
    for i, case in enumerate(test_cases, 1):
        result = has_duplicates(case)
        print(f"测试用例 {i}: {case} → {'存在重复元素' if result else '无重复元素'}")
