### PASSWORD ENCRYPTED ###  
import random, hashlib

#Facundo Castro

# cs50 Final project

def main():
    password = input("Enter a password: ")
    hash = encrypt_password(password,input("Enter a type: "))
    password_generator(len(password))
    a = Decrypt_password(hash,input("Enter a type: "),"password.txt")
    print(f"The Password is: {a}")


def password_generator(len):

    '''
    A basic generator of passwords, Generates the number of posible passwords, calculating the number of symbols, 
    characters and numbers, raised to the length of the password, 
    and then writing them to a text file. They are generated with the integrated Python random library using the Sample() method.
    '''

    with open("password.txt","w") as file:
    #74 is the number of characters (characters+ characters(upper) + numbers + symbols)
        if len > 16 or len < 0:
            raise ValueError
        for a in range(74**len):
            characters = "abcdefghijklmnopqrstuvwxyz"
            numbers = "012W3456789"
            symbols = "{}[]()*;/,_\-"
            sequence = characters + characters.upper()  + numbers + symbols
        #use random sample to generate random passwords
            password_union = random.sample(sequence, len)
            password_result = "".join(password_union)
            #write it in the .txt file
            file.write(f"{password_result}\n")
            a+=1
    file.close()
    return "File Created"

def encrypt_password(password, type):

    '''
    A method that receives two input parameters (password, type) where the password 
    is the one that will be encrypted and the type is the type of hash. 
    analyze the different cases with the match function, if so we call the hashlib library function of the corresponding hash type
    '''

    print("\nHASH RESOLVES\n")
    key = str(password).encode('utf-8')
    print(f"Password :  {password}\n Type : {type}\n")
    #use match to systemize the cases
    match type:
        case 'md5':
            md5 = hashlib.md5(key).hexdigest()
            print(f"HASH : {md5}")
            return md5
        case 'sha1':
            sha1 = hashlib.sha1(key).hexdigest()
            print(f"HASH : {sha1}")
            return sha1
        case  's':
            sha224 = hashlib.sha224(key).hexdigest()
            print(f"HASH : {sha224}")
            return sha224
        case  'sha256':
            sha256 = hashlib.sha256(key).hexdigest()
            print(f"HASH : {sha256}")
            return sha256
        case  'sha384':
            sha384 = hashlib.sha384(key).hexdigest()
            print(f"HASH : {sha384}")
            return sha384
        case  'sha512':
            sha512 = hashlib.sha512(key).hexdigest()
            print(f"HASH : {sha512}")
            return sha512
        case _:
            raise ValueError(f'The encryption type {str(type)} is invalid.' )

def Decrypt_password(hash,type,file):
    '''
    It works by opening the text file with the passwords and going through it and performing the conversion with the indicated type, 
    and at the same time looking for equality between the iterable and the hash passed by parameter in case equality is achieved, 
    password decrypted and resolved.
    '''
    try:
        #open the file generated from the Generate password method in reading mode
        with open(file, 'r') as solver:
            #go through the file
            for x in solver.readlines():
                a = x.strip("\n").encode('utf-8')
                match type:
                    case 'md5':
                        a = hashlib.md5(a).hexdigest()      
                    case 'sha1':
                        a = hashlib.sha1(a).hexdigest()
                    case  'sha224':
                        a = hashlib.sha224(a).hexdigest()
                    case  'sha256':
                        a = hashlib.sha256(a).hexdigest()
                    case  'sha384':
                        a = hashlib.sha384(a).hexdigest()
                    case  'sha512':
                        a = hashlib.sha512(a).hexdigest()
                    case _:
                        raise Exception(f'\nThe encryption type {str(type)} is invalid.' )
                if a == str(hash):
                    return str(x.rstrip())
    except Exception as e:
            return f"Error: {e}"

if __name__ == '__main__':
    main()