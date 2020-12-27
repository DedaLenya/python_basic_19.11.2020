# return masked string
def maskify(cc):
    cc1 = cc[-4:]
    l = len(cc)-4
    return ("#"*l + cc1)

print(maskify("sobaka"))

