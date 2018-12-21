# i="aa"
# count = 0
# while(i):
#     if count <3:
#         i=input()   
#         print(i)
#     else :
#         break
#     count +=1


for i in range(2):
    try:
        k = input()
        print(k)
    except EOFError:
        break

    