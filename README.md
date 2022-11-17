## Procedure on how to play Mental Poker 
1. Alice shuffles and encrypts a deck of cards, then sends it to Bob E<sub>Alice</sub>(M). 
2. Bob picks five of the ciphertexts (Bob picks a number from 1-52).  and identifies these as Amy’s hand and sends them back to Amy. Amy then decrypts them, and she has her hand. 
3. Bob now picks five cards and encrypts them with his own key E<sub>Bob</sub>(E<sub>Alice</sub>(M))= E<sub>Alice</sub>(E<sub>Bob</sub>(M))
4.  He sends them back to Amy. Amy then decrypts the ciphertexts and sends to Bob. E<sub>Bob</sub>(M). Amy cannot find out what bob has as it is encrypted with Bob key. 
5. Bob then decrypts with his decryption key and he now has his hand.
6. Both Amy and Bob cross out the number picked by Bob from the list of possible numbers to be picked

## How to use this github

### Installing 

Using Git/BASH run the following commands:

```
git -b final --single-branch clone https://github.com/S-Samiksha/MentalPoker

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

```

### Bob's server
Under the bob-server.py, edit the HOST and PORT to your own host and port. <br>
Run the command: `python bob-server.py` <br>

### Alice's client 
Under the alice-client.py, edit the HOST and PORT to Bob's ip address and port. 
Run the command: `python alice-client.py` <br>



## Adapted From: <br>
> https://people.csail.mit.edu/rivest/ShamirRivestAdleman-MentalPoker.pdf
> https://rextar4444.medium.com/how-to-play-mental-poker-a-tutorial-by-the-author-of-cypher-poker-loosely-edited-by-twoc-j-smithy-8c1c6f7a8259 









