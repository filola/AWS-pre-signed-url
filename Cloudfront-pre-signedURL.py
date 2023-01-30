
# #!/usr/bin/python3

# import datetime
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.primitives.asymmetric import padding
# from botocore.signers import CloudFrontSigner

# ACCESSKEY_ID = 'ABCDEFG'

# def rsa_signer(message):
#     #### .pem is the private keyfile downloaded from CloudFront keypair
#     key_path = '/Users/qu_chs/Downloads/pk-APKAT24SLC2FLI2IZSMV.cer'  # Private key 파일 위치
#     with open(key_path, 'rb') as key_file:
#         private_key = serialization.load_pem_private_key(
#             key_file.read(),
#             password=None,
#             backend=default_backend()
#         )
#     signer = private_key.sign(padding.PKCS1v15(), hashes.SHA1())
#     signer.update(message)
#     return signer.finalize()

# url = 'url 주소'  # CloudFront 상 객체 주소
# current_time = datetime.datetime.utcnow()
# expire_date = current_time + datetime.timedelta(minutes=2)  # 만료시간을 정함
# cloudfront_signer = CloudFrontSigner("KeyId", rsa_signer)
# # Create a signed url that will be valid until the specfic expiry date
# # provided using a canned policy.
# signed_url = cloudfront_signer.generate_presigned_url(url, date_less_than=expire_date)
# print(signed_url)

import datetime

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from botocore.signers import CloudFrontSigner


def rsa_signer(message):
    with open('키 경로', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())

key_id = '엑세스 키 ID'
url = '접근할 cloudfront url'
expire_date = datetime.datetime(2023, 1, 1)

cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)

# Create a signed url that will be valid until the specific expiry date
# provided using a canned policy.
signed_url = cloudfront_signer.generate_presigned_url(
    url, date_less_than=expire_date)
print(signed_url)
