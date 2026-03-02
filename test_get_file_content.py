from functions.get_file_content import get_file_content


def main():
    print("Result for 'lorem.txt':")
    print(get_file_content("calculator", "lorem.txt"))
    
    print("Result for 'main.py':")
    print(get_file_content("calculator", "main.py"))
    
    print("Result for 'pkg/calculator.py':")
    print(get_file_content("calculator", "pkg/calculator.py"))
    
    print("Result for file outside scope:")
    try:
        print(get_file_content("calculator", "/bin/cat"))
    except Exception as e:
        print(e)
    
    print("Result for non existent file:")
    try:
        print(get_file_content("calculator", "pkg/does_not_exist.py"))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
