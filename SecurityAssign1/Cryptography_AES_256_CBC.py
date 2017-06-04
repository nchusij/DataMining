from cryptography.hazmat.primitives.ciphers import modes

import os, time
import func

# 設定加密方式
iv = os.urandom(16)
cipher = func.GetCrypCipher(modes.CBC(iv))
encryptor = cipher.encryptor()

# 讀取出檔案內容
PlainText = func.GetPlainText()

# 加密並計算時間
start = time.time()
CipherText = encryptor.update(func.Padding(PlainText).encode("utf-8"))  # + encryptor.finalize()
end = time.time()
print("AES256CBC Time taken: ", end - start, "seconds.")

# 解密
decryptor = cipher.decryptor()
checkPlainText = decryptor.update(CipherText)  # + decryptor.finalize()

# 加密過的資料存檔
func.WriteFile('D:/Cryptography_AES256CBC_CipherText.txt', str(CipherText))
# 加密後再解密的資料存檔，用來看檔案是否為原來的檔案內容加上padding
#func.WriteFile('D:/Cryptography_AES256CBC_checkPlainText.txt', checkPlainText.decode("utf-8"))
