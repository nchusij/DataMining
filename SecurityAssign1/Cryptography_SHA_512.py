from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

import time
import func

# 讀取出檔案內容
PlainText = func.GetPlainText().encode("utf-8")

# 設定加密方式
digest = hashes.Hash(hashes.SHA512(), backend=default_backend())

# 加密並計算時間
start = time.time()
digest.update(PlainText)
CipherText = digest.finalize()
end = time.time()
print("SHA512    Time taken: ", end - start, "seconds.")
