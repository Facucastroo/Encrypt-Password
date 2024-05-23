from project import password_generator, encrypt_password,Decrypt_password
import pytest

def test_password_generator():

    with pytest.raises(ValueError):
        assert password_generator(17)
    assert password_generator(3) == "File Created"
    # The generated file will be huge as a test, try with a length of 3 characters
    
def test_encrypt_password():

    assert encrypt_password("Final", "sha256") == "f4ed8fa656b74c5ddf5a54eca0f9aa9629d6c192225a85a5a0abb1a607285523"
    assert encrypt_password("cs50", "md5") == "5d8e29a73f0cc3813911d920c75bc129"
    assert encrypt_password("3/0", "sha512") == "ba8195776b3f78ac112d1e2bd73704a1df0ce74a137e9b9db824b8dccac8b97e34b0b814dc7e57259e27935d38f8a69b90a7028394c74ebefeffb25332284b42"

def test_Decrypt_password():

    assert  Decrypt_password("bbe75aae5757f08d985be18ced8444d1","md5","password.txt") == "WSX"
    assert  Decrypt_password("b3f0e6a3e82d1e42f86c4d3a195cd3347e3f7537512403f5404bf808c73a8d73","sha256","password.txt") == "3Lf"
