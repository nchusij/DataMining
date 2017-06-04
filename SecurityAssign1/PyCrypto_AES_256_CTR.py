from Crypto.Cipher import AES

import time
import func

# 設定加密方式
cipher = func.GetCipher(AES.MODE_CTR)

# 讀取出檔案內容
PlainText = func.GetPlainText()

# 加密並計算時間
start = time.time()
CipherText = cipher.encrypt(func.Padding(PlainText))
end = time.time()
print("AES256CTR Time taken: ", end - start, "seconds.")

# 加密後再解密
checkPlainText = cipher.decrypt(CipherText)

# 加密過的資料存檔
func.WriteFile('D:/AES256CTR_CipherText.txt', str(CipherText))
# 加密後再解密的資料存檔，用來看檔案是否為原來的檔案內容加上padding
#func.WriteFile('D:/AES256CTR_checkPlainText.txt', checkPlainText.decode("utf-8"))
