inport subprocess

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

name = input("Enter the your name: ")
interface = input("Enter the interface name: ")
new_mac = input("Enter the new MAC address: ")


print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("Hello " + name + " :) ")
print("[+] MAC address changed successfully.")
