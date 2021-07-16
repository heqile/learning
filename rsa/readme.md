# RSA
## Description
RSA is one of the asymetric encryption method. It have a pair of keys: private key and public key. As the name so-called, the private key is a key that should keep in secret, no one can touch it. And the public key can be wildly distributed, everyone can see and use it.

## Usage
A message can be encrypted with one key (private key or public key), then the encrypted text only can be decrypted with the other key. 
- Secure message: Alice wants to send a secret message to Bob. What Alice can do? Alice encrypts the message with the Bob's public key, then only Bob, who has the private key, can read the message.
- Signing: Alice wants Bob to prove its identity. What can Bob do? Bob can encrypt the well known message with his private key and send that to Alice. As Alice have the Bob's prublic key, she can decrypt the message and verify if it is correct. 

## Math
### Notation
1. p, q: two prime numbers
2. n: n = p * q. n is used as modulus for both private and public key, and it also represents the key length
3. lambda(n): Carmichael's totient function on n. Normally it is the number of coprimes to n.
4. e: 1 < e < lambda(n), and e and lambda(n) are coprimes. the most commonly chosen value for e is 65,537
5. d: d * e ≡ 1 (mod λ(n))
### Keys
1. public key: n, e
2. private key: n, d
### Equations:
1. encryption: ![encryption](doc/encrypt_equation.svg)
2. signing: ![signing](doc/signing_equation.svg)

## Example
1. Generate key for p =17, q = 11, n = 187, e= 7 & d = 23.
   1. create a file with asn1 type
    ```text
    # file: asn1
    asn1=SEQUENCE:rsa_key

    [rsa_key]
    version=INTEGER:0
    modulus=INTEGER:187
    pubExp=INTEGER:7
    privExp=INTEGER:23
    p=INTEGER:17
    q=INTEGER:11
    e1=INTEGER:7
    e2=INTEGER:3
    coeff=INTEGER:14
    ```
   2. use openssl command to create the key files
    ```bash
    # private key
    openssl asn1parse -genconf <path to above file> -out newkey.der
    # check private key
    openssl rsa -in newkey.der -inform der -text -check
    # public key
    openssl rsa -in newkey.der -inform der -pubout > public.key
    openssl rsa -in smalld.pem -pubin -text
    ```
2. Encrypt the message file
   1. encrypt with public key: `openssl rsautl -encrypt -pubin -inkey public_long.key -in message.txt`
   2. decrypt with private key: `openssl rsautl -decrypt -inkey private_long.key -in encrypted_message.txt`
3. Encrypt/decrypt with python:
   ```python
    # message: hello world
    # the message should convert to hex then to int
    message = "hello world"
    import binascii
    m = int(binascii.hexlify(message), 16) # 126207244316550804821666916
    # for the given key pair (private_long.key/public_long.key)
    n = 6542015063994515248476730532100329105363108552572836810853371344715686413541869574742532199613525678825344869087943182615610691038663329702677380730930271
    e = 65537
    d = 1328726711885362352144189696092092721996556722817599688561716678662595203482821432888460954148701099137516232958011436071851729184290089386753025541773473
    # to encrypt
    c = pow(m, e, n) # 1680696943663121224060923538102641144854240637727931795550093592903700287049656958939397072341118425986760523193410262816033084228544459889930830384609313
    # to decrypt
    dm = pow(c, d, n) # 126207244316550804821666916
   ```

## Possible attacks
[reference](https://www.sjoerdlangkemper.nl/2019/06/19/attacking-rsa/)
1. Modulus too small
    - modulus: 8464481006489090994506453371545747140045883416875197642486592854169 (`possible_attacks/modulus_too_small/smallkey.pem`)
    - using `http://factordb.com/index.php?query=8464481006489090994506453371545747140045883416875197642486592854169` (or other tools) to find the p, q easily
2. Low private exponent
    - inspect the public key, we can find the `e` is extreamly great which is a sign of using `wiener` or `Boneh and Durfee` to crack it. n=146586037202965387069634066969876083326251628520351225215717274507283204108452066438865866202922396922761298570847843003044895731969747304642676580139354698435068642668022869039577672704378038093336446321775683503036016532581053061337333809170145805527545224809935978727653773522811954484028147223471197153661
    e=39931334096757883591750420309773442362369179459075378633140843909930331209369084171392694467173740964163519891505430971652782334490522304164197440293467143392875696416420560487128761020036187269685969620865898338255304144689856535870698697635019941724787590476120246934236608125253706342455216317508579270327
    - the example can be cracked with `wiener` algorithm. [wiener is well explained in this video](https://www.youtube.com/watch?v=OpPrrndyYNU)
3. p and q close together
    - using Fermat’s factorization method.
    - `Fermat’s algorithm searches for an a and b such that N = a2 - b2. In that case, N is factorable as (a + b)(a - b). If p and q are close together, a is close to √N and b is small, making them easy to find.`
4. e = 1
5. Prime N
6. shared p or q
    - if two keys shares exact the same p or q, we can use calculate the gcd to find the common prime
    - if two keys shares some close prime, we can try to use the `Wiener` methode to break it.  
      - For example:
       ```python
       from typing import Tuple, Iterator, Iterable, Optional
       n1=848618245986946113856861516017057946811048278213696064801189677795363283325440826098691152307268337594919769636945823789565170289533004601037743584706310322948174445580605970474321048724844100292089086919267113592449794772197707045175566457659320376007535766717374330501563932305560229136165673234960976147749464573610793
       n2=1638570822193767360035771630083255816253900246406668474185142832300121157408287883795068894850124293996692348231016134472283974982309183413894865545379783902246447389668147665757291582452405957728558699589758761201669341785192037109205105106607476814750862046924434988200262499102808098985673205422714882639790078086842187
       def rational_to_contfrac(x: int, y: int) -> Iterator[int]:
           """
           ref: https://en.wikipedia.org/wiki/Euclidean_algorithm#Continued_fractions

           >>> list(rational_to_contfrac(4, 11))
           [0, 2, 1, 3]
           """
           while y:
               a = x // y
               yield a
               x, y = y, x - a * y

       def contfrac_to_rational_iter(contfrac: Iterable[int]) -> Iterator[Tuple[int, int]]:
           """
           ref: https://www.cits.ruhr-uni-bochum.de/imperia/md/content/may/krypto2ss08/shortsecretexponents.pdf (6)
           """
           n0, d0 = 0, 1
           n1, d1 = 1, 0
           for q in contfrac:
               n = q * n1 + n0
               d = q * d1 + d0
               yield n, d
               n0, d0 = n1, d1
               n1, d1 = n, d

       def convergents_from_contfrac(contfrac: Iterable[int]) -> Iterator[Tuple[int, int]]:
           """
           ref: https://www.cits.ruhr-uni-bochum.de/imperia/md/content/may/krypto2ss08/shortsecretexponents.pdf Section.3
           """
           n_, d_ = 1, 0
           for i, (n, d) in enumerate(contfrac_to_rational_iter(contfrac)):
               if i % 2 == 0:
                   yield n + n_, d + d_
               else:
                   yield n, d
               n_, d_ = n, d

       f_ = rational_to_contfrac(n1, n2)
       convergents_from_contfrac(f_)
       for a,b in convergent:
           if a!=1 and b!=1 and n1%a==0 and n2%b==0:
               print(f"p1={a}, q1={n1//a}, p2={b}, q2={n2//b}")
               break

       # p1 = 857712323239775057524082694907933273426907057259473041420510822066423446966733400899365691
       # q1 = 989397287404617739595246457389170004592866030381488020297920368401835221027360490635044846273885035195008650404478629627225081645106200551624187341122937248871212771784190881292957094295575712475747196046331194571455359122339058923
       # p2 = 1656130295740004048847006964224492019888442056651007891201894308473616198666793024352465301
       # q2 = 989397287404617739595246457389170004592866030381488020297920368401835221027360490635044846273885035195008650404478629627225081645106200551624187341122937248871212771784190881292957094295575712475747196046331194571455359122339061087
       ```
