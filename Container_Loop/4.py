input_id = input("아이디를 입력해주세요.\n")
# real_egoing = "egoing"
# real_k8805 = "k8805"
members = ['egoing','k8805']
for member in members:
    if member == input_id:
        print('Hello!, ' + member)
        import sys
        sys.exit()
print ('Who are you?')
