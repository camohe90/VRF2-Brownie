#!/usr/bin/python3
from brownie import VRFConsumerV2


def main():
    vrf_contract = VRFConsumerV2[-1]
    try:
        print(f"El número aleatorio solicitado a chainlink es {vrf_contract.s_randomWords(0)}")
        print(f"El número secreto para ganar la apuesta es {vrf_contract.secretNumber()}")
    except:
        print("Debes esperar por lo menos un minuto a menos que estes en local chain!")
