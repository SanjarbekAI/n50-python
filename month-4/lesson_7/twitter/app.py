import math

#
# def read_txt_file(file_name):
#     with open(file_name, "r") as f:
#         return f.read()

#
# page = 1
# page_size = 2
#
# posts = read_txt_file("posts.txt").split("\n")
#
# while True:
#     print(posts[(page - 1) * page_size: (page - 1) * page_size + page_size])
#     print(f"""1 <- {page}/{math.ceil(len(posts) / page_size)} -> 2""")
#     choice = input("Enter: ")
#     if choice == "1":
#         if page == 1:
#             print("There is no page before that")
#             continue
#         page -= 1
#     elif choice == "2":
#         if page == 2:
#             print("There is no page after that")
#             continue
#         page += 1
#     else:
#         print("Invalid choice")
