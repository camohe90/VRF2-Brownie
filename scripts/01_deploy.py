from brownie import VRFConsumerV2, network, config, Wei 
from scripts.funciones_utiles import get_account


LINKTOKEN = "0x01BE23585060835E02B77ef475b0Cc51aA1e0709"

def deploy_vrf_consumer():
    account = get_account()
    print(f"On network {network.show_active()}")
    subscription_id = config["networks"][network.show_active()]["subscription_id"]
    keyhash = config["networks"][network.show_active()]["keyhash"]  # Also known as keyhash
    vrf_coordinator = "0x6168499c0cFfCaCD319c818142124B7A15E857ab"
    link_token = "0x01be23585060835e02b77ef475b0cc51aa1e0709"

    vrf_consumer = VRFConsumerV2.deploy(
        subscription_id,
        vrf_coordinator,
        link_token,
        keyhash,  # Also known as keyhash
        {"from": account,'value': Wei('0.1 ether')},
    )
    if config["networks"][network.show_active()].get("verify", False):
        vrf_consumer.tx.wait(BLOCK_CONFIRMATIONS_FOR_VERIFICATION)
        VRFConsumerV2.publish_source(vrf_consumer)
    else:
        vrf_consumer.tx.wait(1)
    return vrf_consumer


def main():
    deploy_vrf_consumer()

    