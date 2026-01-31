# import unittest
# from functions.get_files_info import get_files_info


# class TestGetFilesInfo(unittest.TestCase):

#     def test_get_files_info_current_directory(self):
#         """Test listing files in current directory"""
#         result = get_files_info("calculator", ".")
#         print("Result for current directory:")
#         indented_result = "\n".join("  " + line for line in result.split("\n"))
#         print(indented_result)

#     def test_get_files_info_subdirectory(self):
#         """Test listing files in subdirectory"""
#         result = get_files_info("calculator", "pkg")
#         print("Result for 'pkg' directory:")
#         indented_result = "\n".join("  " + line for line in result.split("\n"))
#         print(indented_result)

#     def test_get_files_info_outside_directory(self):
#         """Test that accessing /bin directory returns an error"""
#         result = get_files_info("calculator", "/bin")
#         print("Result for '/bin' directory:")
#         indented_result = "\n".join("    " + line for line in result.split("\n"))
#         print(indented_result)

#     def test_get_files_info_parent_directory(self):
#         """Test that accessing parent directory returns an error"""
#         result = get_files_info("calculator", "../")
#         print("Result for '../' directory:")
#         indented_result = "\n".join("    " + line for line in result.split("\n"))
#         print(indented_result)


# if __name__ == "__main__":
#     unittest.main()

from functions.get_files_info import get_files_info


def test():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    indented_result = "\n".join("  " + line for line in result.split("\n"))
    print(indented_result)

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    indented_result = "\n".join("  " + line for line in result.split("\n"))
    print(indented_result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    indented_result = "\n".join("  " + line for line in result.split("\n"))
    print(indented_result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    indented_result = "\n".join("  " + line for line in result.split("\n"))
    print(indented_result)


if __name__ == "__main__":
    test()