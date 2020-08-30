import hashlib

md5=hashlib.md5()
md5.update('hellopython'.encode('utf-8'))
# e53024684c9be1dd3f6114ecc8bbdddc
# 5f63dbd7099001adde5056f1908246d8
print(md5.hexdigest())