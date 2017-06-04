from Crypto.Hash import SHA512
import time
import func

# 讀取出檔案內容
PlainText = func.GetPlainText().encode('utf-8')

# 加密並計算時間
start = time.time()
h = SHA512.new(PlainText).hexdigest()
end = time.time()
print("SHA512    Time taken: ", end - start, "seconds.")
# print (h)

"""
#兩種寫法  結果相同的測試
start = time.time()
h = SHA512.new()
h.update(b'zzz')
h.hexdigest()
end = time.time()
print ("SHA512    Time taken: ", end - start, "seconds.")
print(h.hexdigest())

start = time.time()
h=SHA512.new(b'zzz').hexdigest()
end = time.time()
print ("SHA512    Time taken: ", end - start, "seconds.")
print(h)
"""
