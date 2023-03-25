import wmi

print(" __       __   ______    ______          ______   __                                               ")
print("/  \     /  | /      \  /      \        /      \ /  |                                              ")
print("$$  \   /$$ |/$$$$$$  |/$$$$$$  |      /$$$$$$  |$$ |____    ______   _______    ______    ______  ")
print("$$$  \ /$$$ |$$ |__$$ |$$ |  $$/       $$ |  $$/ $$      \  /      \ /       \  /      \  /      \ ")
print("$$$$  /$$$$ |$$    $$ |$$ |            $$ |      $$$$$$$  | $$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |")
print("$$ $$ $$/$$ |$$$$$$$$ |$$ |   __       $$ |   __ $$ |  $$ | /    $$ |$$ |  $$ |$$ |  $$ |$$    $$ |")
print("$$ |$$$/ $$ |$$ |  $$ |$$ \__/  |      $$ \__/  |$$ |  $$ |/$$$$$$$ |$$ |  $$ |$$ \__$$ |$$$$$$$$/ ")
print("$$ | $/  $$ |$$ |  $$ |$$    $$/       $$    $$/ $$ |  $$ |$$    $$ |$$ |  $$ |$$    $$ |$$       |")
print("$$/      $$/ $$/   $$/  $$$$$$/         $$$$$$/  $$/   $$/  $$$$$$$/ $$/   $$/  $$$$$$$ | $$$$$$$/ ")
print("                                                                               /  \__$$ |          ")
print("                                                                               $$    $$/           ")
print("                                                                                $$$$$$/            ")

print("                                                                               By SAVINDU DESHAN   ")
print("")

def change_mac_address(interface, new_mac):
    try:
        wmi_obj = wmi.WMI()
        
        adapter = wmi_obj.Win32_NetworkAdapter(InterfaceIndex=interface)[0]
        
        adapter.Disable()
        
        adapter.MACAddress = new_mac
        
        adapter.Enable()
        
        print("[+] MAC address changed successfully.")
    except:
        print("[-] An error occurred while changing the MAC address.")

interface = input("Enter the interface index: ")
new_mac = input("Enter the new MAC address: ")

change_mac_address(interface, new_mac)
