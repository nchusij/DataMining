import func
import random, string

# randomText = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(512 * 1024 * 1024 + 7))
randomText = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(4))
# Generate [0-9, a-z, A-Z] ten words

func.WriteFile('D:/PlainText.txt', randomText)
