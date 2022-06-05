#import logging
import sys

import smpplib.gsm
import smpplib.client
import smpplib.consts


# if you want to know what's happening
#logging.basicConfig(level='DEBUG')

# Two parts, GSM default / UCS2, SMS with UDH
# TODO check this method to format your messages
parts, encoding_flag, msg_type_flag = smpplib.gsm.make_parts(u'Message test agavaza')

client = smpplib.client.Client('10.201.47.17', 5016)

# Print when obtain message_id
client.set_message_sent_handler(
    lambda pdu: sys.stdout.write('sent {} {}\n'.format(pdu.sequence, pdu.message_id)))

# Handle delivery receipts (and any MO SMS)
def handle_deliver_sm(pdu):
        sys.stdout.write('delivered {}\n'.format(pdu.receipted_message_id))
        return 0 # cmd status for deliver_sm_resp

client.set_message_received_handler(lambda pdu: handle_deliver_sm(pdu))

client.connect()
print('conectado')
client.bind_transceiver(system_id='CMC_Portal', password='#C*rw1t')
print('binded ')
for part in parts:
    #pdu = client.send_message(
    client.send_message(
        source_addr_ton=smpplib.consts.SMPP_TON_ALNUM,
        source_addr_npi=smpplib.consts.SMPP_NPI_UNK,
        # Make sure it is a byte string, not unicode:
        source_addr='1727',

        dest_addr_ton=smpplib.consts.SMPP_TON_INTL,
        dest_addr_npi=smpplib.consts.SMPP_NPI_ISDN,
        # Make sure these two params are byte strings, not unicode:
        destination_addr='258847479196',
        short_message=part,

        data_coding=encoding_flag,
        esm_class=msg_type_flag,
        registered_delivery=True,
    )
    #print(pdu.sequence)

client.unbind()
client.disconnect()

# Enters a loop, waiting for incoming PDUs
#client.listen()(lottus) administrator@srv03:/var/www/cac_ussd/pythonsmpplib$
