# Presentation 

#### Cryptography Ideas to consider:
1. Confidentiality: Ensures that the message or data does not fall into the wrong hands 
2. Integrity: Ensuring the data is not changed --> Not susceptible to MiTM attacks
3. Authentiation: Meaning that the receiver can verify that the message was indeed sent by the sender Alice (Sign Using a Hash)
4. Non-Repudiation: Meaning that the seender Alice cannot deny sending the message --> How to do this 

#### Mental Poker General Constriants:
1. Alice and Bob wish to communicate using a secret key cryptosystem.
2. Each player must know which cards are in his hand, but must have no information about which cards are in the other player's hand. `Confidentiality`
3. All possible hands are equally likely for each player --> proper RNG
4. During the game the players may want to draw new cards from the "remaining deck" or to reveal certain cards in their hands to the opposing player. They must be able to do so without compromising the security of the cards remaining in their hand. 
5. At the end of the game, each player must be able to check that the game was played fairly and that the other player has not cheated. If one player claimed that he was dealt four aces, the other player must now be able to confirm this. `Non-Repudiation and Authentication`
6. Mathematically, it is theoretically impossible to deal the cards in a way which simulataneously ensures that the two hands are disjoint.
7. However, with a protocol we can do so. 
8. Mental Poker has to be a symmetric key encryption due to the commutative requirement. 

#### Properties of Mental Poker 
1. E<sub>k</sub>(X) is the encrypted version of a message X under key K
2. D<sub>k</sub>(E<sub>k</sub>(X)) = X for all messages X and keys K
3. E<sub>alice</sub>(E<sub>bob</sub>(X)) = E<sub>bob</sub>(E<sub>alice</sub>(X)) for all messages X and keys J and K, 
4. Given X and E<sub>k</sub>(X) it computationally impossible for a cryptanalyst to derive K, for all X and K, 
5. Given any messages X and Y, it is computationally impossible to find keys J and K such that E<sub>Alice</sub>(X) = E<sub>Bob</sub>(Y)


6. The Encryption and Decryption is similar to the RSA encryption and decryption which uses gcd, PHI(n), mod n. 
7. It is commutative therefore can be used for the SAME value of n. 
8. This is where it starts differing from the original RSA. 
9. n here is public and we share the same PHI(n). In other words, p and q has to be sent across the network without somebody else sniffing it. 
10. Bob and Alice have their own encryption this is NOT public as compared to our regular RSA. 

So what does that mean? <br>

> gcd (A, PHI(n)) = 1 AND gcd(B, PHI(n))=1 AND A !=B AND (A & B) cannot be and should not be deciphered. 

> That means gcd(q, PHI(n))=1 whereby q must have as many values as possible to prevent brute force attacks or even simple plain mathematical attacks. 

> https://rextar4444.medium.com/how-to-play-mental-poker-a-tutorial-by-the-author-of-cypher-poker-loosely-edited-by-twoc-j-smithy-8c1c6f7a8259 

#### Procedure on how to play Mental Poker 
1. Alice shuffles and encrypts a deck of cards, then sends it to Bob E<sub>Alice</sub>(M). 
2. Bob picks five of the ciphertexts (Bob picks a number from 1-52).  and identifies these as Amy’s hand and sends them back to Amy. Amy then decrypts them, and she has her hand. 
3. Bob now picks five cards and encrypts them with his own key E<sub>Bob</sub>(E<sub>Alice</sub>(M))= E<sub>Alice</sub>(E<sub>Bob</sub>(M))
4.  He sends them back to Amy. Amy then decrypts the ciphertexts and sends to Bob. E<sub>Bob</sub>(M). Amy cannot find out what bob has as it is encrypted with Bob key. 
5. Bob then decrypts with his decryption key and he now has his hand.
6. Both Amy and Bob cross out the number picked by Bob from the list of possible numbers to be picked


#### Explaination of the Encryption / Decryption:
1. RSA is a type of asymetric encryption/decryption 
2. So you can publish a "public key" which anybody can use to encrypt messages to you but only you know the appropriate corresponding private decryption key. 
3. For this method to work, there should be no way to compute (in a reasonable time) the decryption key from the encryption key. 
4. Generally for each communication, Alice and Bob will use a different key. If they keep on using the same key, time after time, an eavesdropper has more matieral to use for decryption). 
5. Usually, we would use public key cryptosystem, but does that acheive commutative properties?


#### Things to do:
1. How to send my p and q across without attackers sniffing? Need something form of Hashing and Hash values (one or two days fixing that)
    > Alice send p and Bob send q
2. How to ensure PHI is large enough to avoid a brute force attack? (one day fixing this)
3. Brute Force Attack --> Key Class 
4. Plain text attack on the cards side. (one or two days) --> Deck Class 
5. RNG can we hardcode it? and then prove something for it like Week 9 Lecture slide 4 --> Deck Class
6. Blinding Attack with actual code, because online provides the one for RSA. here our algorithm is slightly different (One or two days) --> Key Class
7. Initial Card Values can Leak Information --> Figure this out 
> m^(phi(P)/2)mod P --> find out why it works?
8. AES 
9. Deffie Hellman 








