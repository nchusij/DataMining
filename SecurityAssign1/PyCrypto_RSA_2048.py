from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto import Random
import func
import time

random_generator = Random.new().read
rsa = RSA.generate(2048, random_generator)

# 產生私KEY
private_pem = rsa.exportKey()
# 產生公KEY
public_pem = rsa.publickey().exportKey()

# 讀取出檔案內容
PlainText = func.GetPlainText().encode('utf-8')
# 設定加密方式
rsakey = RSA.importKey(public_pem)
cipher = Cipher_pkcs1_v1_5.new(rsakey)

# 如果檔案內容長度超過245bytes，就分段加密
l = len(str(PlainText))
i = 0
total = 0
CipherText = b''
sCipherText = b''
endlen = 0
# 分段加密
while l - 245 * i > 0:
    if l > 245 + i * 245: endlen = 245 + i * 245
    if l < 245 + i * 245: endlen = l

    # 加密並計算時間
    start = time.time()
    sCipherText = cipher.encrypt(PlainText[i * 245: endlen])
    end = time.time()
    CipherText += sCipherText
    i += 1
    total += end - start

# 總共花費的時間
print("RSA2048   Time taken: ", total, "seconds.")

checkPlainText = ''
# 如果檔案內容長度沒有超過245bytes，就解密
if len(func.GetPlainText()) < 245:
    rsakey = RSA.importKey(private_pem)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    checkPlainText = cipher.decrypt(CipherText, random_generator)

# 加密過的資料存檔
func.WriteFile('D:/RSA2048_CipherText.txt', str(CipherText))

# 如果檔案內容長度沒有超過245bytes，就存檔
#if len(func.GetPlainText()) < 245:
    # 加密後再解密的資料存檔
    #func.WriteFile('D:/RSA2048_checkPlainText.txt', checkPlainText.decode('utf-8'))
