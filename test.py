import funpy

@funpy.forEachArg
def user_info(x, n):
    return x*2

print(user_info(2, 4, 6))