#-*- coding: utf-8 -*-

import collections


"""
-----
Ethernet DEVICE ----> PacketReceiver ---->  | RxQueue | ----> PacketProcessor
       |                                                             |
       |                                                             |
       |                                                             |
       +<---------  PacketTransmitter  <--- | TxQueue | <---- ProtocolHandler
"""

class TxQueue(collections.Queue):
    """Transmit queue
    """
    pass


class RxQueue(collections.Queue):
    """Receive queue
    """
    pass


class PacketTransmitter(object):
    """packet transmitter
    """
    pass


class PacketReceiver(object):
    """packet Receiver
    """
    pass


class PacketProcesser(object):
    pass


