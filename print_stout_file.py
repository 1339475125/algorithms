"""
请实现下面代码中的 `stdout_redirect` ，实现将 `print` 打印的字符串打印到文件中。

    ```python
    with open("file.txt", "w") as f:
        with stdout_redirect(f):
            print("hello world")
    ```
"""

def stdout_redirect(f):
    """
    输出打印到文件中
    """
    

    
if __name__ == "__main__":
    with open("file.txt", "w") as f:
        with stdout_redirect(f):
            print("hello world")