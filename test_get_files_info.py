from functions.get_files_info import get_files_info


def main():
    print("Result for current directory:")
    print(get_files_info("calculator", "."))
    
    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))
    
    print("Result for '/bin' directory:")
    try:
        print(get_files_info("calculator", "/bin"))
    except Exception as e:
        print(e)
    
    print("Result for '../' directory:")
    try:
        print(get_files_info("calculator", "../"))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
