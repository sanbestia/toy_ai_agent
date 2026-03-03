from functions.run_python_file import run_python_file


def main():
    print("Result for calculator usage instructions:")
    print(run_python_file("calculator", "main.py"))
    
    print("Result for calculator usage with args:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    
    print("Result for calculator testing:")
    print(run_python_file("calculator", "tests.py"))
    
    print("Result for file outside scope")
    try:
        print(run_python_file("calculator", "../main.py"))
    except Exception as e:
        print(e)
    
    print("Result for non existent file:")
    try:
        print(run_python_file("calculator", "nonexistent.py"))
    except Exception as e:
        print(e)
    
    print("Result for non python file")
    try:
        print(run_python_file("calculator", "lorem.txt"))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
