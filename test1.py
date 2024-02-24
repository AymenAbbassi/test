# from inputs import get_key
 
# while 1:
#     events = get_key()
#     for event in events:
#         print(event.ev_type, event.code, event.state)







import usb.core

devices = usb.core.find(bDeviceClass=0)
for device in devices:
    print(device)

