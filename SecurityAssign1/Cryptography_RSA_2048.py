from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

import time
import func

# 產生私KEY
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# 產生公KEY
public_key = private_key.public_key()

# 讀取出檔案內容
PlainText = func.GetPlainText().encode('utf-8')


# 測試用
# PlainText = b'encrypted data'


# 加密function
def Enc(PlainText):
    ciphertext = public_key.encrypt(
        PlainText,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    return ciphertext


# 解密function
def Dec(ciphertext):
    checkPlainText = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    return checkPlainText


# 如果檔案內容長度超過214bytes，就分段加密
l = len(str(PlainText))
i = 0
total = 0
CipherText = b''
sCipherText = b''
endlen = 0

# 分段加密
while l - 214 * i > 0:
    if l > 214 + i * 214: endlen = 214 + i * 214
    if l < 214 + i * 214: endlen = l
    # 加密並計算時間
    start = time.time()

    sCipherText = Enc(PlainText[i * 214: endlen])
    end = time.time()
    CipherText += sCipherText
    i += 1
    total += end - start

# 總共花費的時間
print("RSA2048   Time taken: ", total, "seconds.")

checkPlainText = ''
# 如果檔案內容長度沒有超過214bytes，就解密
if len(func.GetPlainText()) < 214:
    checkPlainText = Dec(CipherText)

# 加密過的資料存檔
func.WriteFile('D:/Cryptography_RSA2048_CipherText.txt', str(CipherText))

# 如果檔案內容長度沒有超過214bytes，就存檔
#if len(func.GetPlainText()) < 214:
    # 加密後再解密的資料存檔
    #func.WriteFile('D:/Cryptography_RSA2048_checkPlainText.txt', checkPlainText.decode('utf-8'))
