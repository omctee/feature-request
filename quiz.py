
from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcpvJU0c3TLNHpUotODhbnZqrbbJFpFfjNpTZI-xYQ9EtDi8A3TK5yybRoYrFlQy7bUXsKOjM7n8n_sx46E3Imi8htjkYfMSbTRPe4zUfu2n0avqOlxNxAsaVyE47RpS3cqhT75tFSaPl9dTsAQSFR-jo5paVXxDgBjbzW5YXLTKmoVvYf9vBQbLGgqS4UX59kG4fu'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()

"""
quiz part 2
https://engineering-application.britecore.com/e/t5e119s3t/testImplementationEngineer


quiz part 1
s = ""
c = [104, 116, 116, 112, 115, 58, 47, 47, 101, 110, 103, 105, 110, 101, 101, 114, 105, 110, 103, 45, 97, 112, 112, 108, 105, 99, 97, 116, 105, 111, 110, 46, 98, 114, 105, 116, 101, 99, 111, 114, 101, 46, 99, 111, 109, 47, 113, 117, 105, 122, 47, 115, 100, 102, 103, 119, 114, 52, 52, 104, 114, 102, 104, 102, 104, 45, 119, 115]
for i in c:
  s = s + chr(i)
print(s)
#https://engineering-application.britecore.com/quiz/sdfgwr44hrfhfh-ws
"""