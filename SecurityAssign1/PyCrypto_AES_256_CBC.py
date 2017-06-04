from Crypto.Cipher import AES
from Crypto import Random

import time
import func

# 設定加密方式
iv = Random.new().read(AES.block_size)
cipher = func.GetCipher(AES.MODE_CBC, iv=iv)

# 讀取出檔案內容
PlainText = func.GetPlainText()

# 加密並計算時間
start = time.time()
CipherText = iv + cipher.encrypt(func.Padding(PlainText))
end = time.time()
print("AES256CBC Time taken: ", end - start, "seconds.")

# 加密後再解密
# It is ignored for MODE_ECB and MODE_CTR.
iv = CipherText[:AES.block_size]
cipher = func.GetCipher(AES.MODE_CBC, iv)
checkPlainText = cipher.decrypt(CipherText[AES.block_size:])

# 加密過的資料存檔
func.WriteFile('D:/AES256CBC_CipherText.txt', str(CipherText))
# 加密後再解密的資料存檔，用來看檔案是否為原來的檔案內容加上padding
#func.WriteFile('D:/AES256CBC_checkPlainText.txt', checkPlainText.decode("utf-8"))
