n = input()
a = [int(i) for i in input().split()]


a.insert(0,a.pop())

ans = ""
for i in a:
    ans+=str(i)
    ans+=" "

print(ans[:-1])