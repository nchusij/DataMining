from cryptography.hazmat.primitives.ciphers import modes

import time
import func

# 設定加密方式
cipher = func.GetCrypCipher(modes.ECB())
encryptor = cipher.encryptor()

# 讀取出檔案內容
PlainText = func.GetPlainText()

# 加密並計算時間
start = time.time()
CipherText = encryptor.update(func.Padding(PlainText).encode("utf-8"))  # + encryptor.finalize()
end = time.time()
print("AES256EBC Time taken: ", end - start, "seconds.")

# 解密
decryptor = cipher.decryptor()
checkPlainText = decryptor.update(CipherText)  # + decryptor.finalize()

# 加密過的資料存檔
func.WriteFile('D:/Cryptography_AES256ECB_CipherText.txt', str(CipherText))
# 加密後再解密的資料存檔，用來看檔案是否為原來的檔案內容加上padding
#func.WriteFile('D:/Cryptography_AES256ECB_checkPlainText.txt', checkPlainText.decode("utf-8"))
