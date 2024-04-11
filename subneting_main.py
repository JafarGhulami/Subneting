#11 April 2024
#!/usr/bin/env python
import random
#import sys

def subnet_calc():
    try:
#check ip validaty
        while True:

            ip_address = input("Please Enter your IP Address: ")

            #checking otceds
            octed = ip_address.split(".")
            #rules for validation
            if (len(octed) == 4 ) and (1<= int(octed[0])) and (int(octed[0]) <= 223) and (int(octed[0]) != 127) and (int(octed[0]) != 169 or int(octed[1]) !=254) and ((0 <= int(octed[1]) <= 255) and (0 <= int(octed[2]) <= 255) and (0 <= int(octed[3]) <= 255)):
                #print("\n")
                break
            else:
                print("\n The IP address is INVALID please enter it again!")
                continue

        while True:
            # subnet mask validation checking
            masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
            #print("\n")
            subnet_mask = input("Please Enter your Subnet mask: ")
            mask = subnet_mask.split(".")
            if (len(mask) == 4) and (int(mask[0]) == 255) and (int(mask[1]) in masks) and (int(mask[2]) in masks) and (
                    int(mask[3]) in masks) and (int(mask[0]) >= int(mask[1])) and (int(mask[1]) >= int(mask[2])) and (
                    int(mask[2]) >= int(mask[3])):
                break
            else:
                print("invalid subnet mask Please try again")
                continue
        # converting decimal subnet mask to binary one
        mask_octed_add = []
        mask_octed_decimal = subnet_mask.split(".")

        for octed_index in range(0, len(mask_octed_decimal)):

            binary_octed = bin(int(mask_octed_decimal[octed_index])).split("b")[1]

            if len(binary_octed) == 8:
                mask_octed_add.append(binary_octed)
            elif len(binary_octed) < 8:
                mask_octed_add.append(binary_octed.zfill(8))
        decimal_mask = ".".join(mask_octed_add)

        # find num of hosts by binary mask
        no_of_zero = decimal_mask.count("0")
        no_of_one = 32 - no_of_zero
        no_of_hosts = (2 ** no_of_zero) - 2
        # no_of_ip_in_net = (2** no_of_zero)

        # find the wildcard mask by ip octeds and then join them as a wildcard mask
        wildcard_octed = []

        for w_octed in mask_octed_decimal:
            val = 255 - int(w_octed)
            wildcard_octed.append(str(val))

        wildcard_mask = ".".join(wildcard_octed)
        print("wildcard mask: ", wildcard_mask)


        #converting IP to binary
        ip_binary_add = []
        ip_octeds = ip_address.split(".")

        for octed_index in range(0, len(ip_octeds)):

            binary_octed = bin(int(ip_octeds[octed_index])).split("b")[1]

            if len(binary_octed) == 8:
                ip_binary_add.append(binary_octed)
            elif len(binary_octed) < 8:
                ip_binary_add.append(binary_octed.zfill(8))
        ip_binary_add = "".join(ip_binary_add)
        #print("Binary of ip number: ",ip_binary_add)
        #find network add from 11111000000010000010001001000000 ------> keep the 1 or 0 then other maybe 1 or 0

        network_add_binary = ip_binary_add[:no_of_one]+"0"*no_of_zero
        broadcast_add_binary = ip_binary_add[:no_of_one]+"1"*no_of_zero
        #print("broadcast address:%s\nnetwork address: %s"%(broadcast_add_binary,network_add_binary))

        my_broadcast_add = []
        my_network_add = []
        # for example to seperate the 11111000000010000010001001000000 to -----> [11111000, 0000100 ,00010001 ,001000000] ---> [248,4,17,32]

        for index in range(0,len(broadcast_add_binary),8):

            octs = int(broadcast_add_binary[index:index+8],2) # the second arg of int show the base of string base 2
            my_broadcast_add.append(octs)


        for index in range(0, len(network_add_binary), 8):
            octs = int(network_add_binary[index:index + 8],2) # the second arg of int show the base of string base 2
            my_network_add.append(octs)

        print("Network ID: %s\nBroadcast ID: %s"%(my_network_add,my_broadcast_add))


        #give as a randome ip address
        i = 1
        while True:
            generate = input("Generate a randome IP from subnet? (y/n)")


            # obtain ip between net add and broadcast add
            if generate =="y":

                generate_ip = []
                for indexb, oct_bst in enumerate(my_broadcast_add):
                    for indexn , oct_net in enumerate(my_network_add):
                        if indexb == indexn:
                            if oct_bst == oct_net:
                            ## add I dentical octets to the gerated ip list
                                generate_ip.append(oct_bst)
                            else:
                                generate_ip.append(str(random.randint(int(oct_net),int(oct_bst))))
                                # ip generated
                ip_values = []
                for iii in generate_ip:
                    ip_values.append(str(iii))

                ip_generated = ".".join(ip_values)

                print("#%d ip address is :%s "%(i,ip_generated))
                i += 1

               # print("\n")
                continue


            else:
                print("okay bye!")
                break


    except KeyboardInterrupt:
        print("There is some problem about your keyboard strock!")


subnet_calc()