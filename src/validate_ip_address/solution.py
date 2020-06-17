class Solution:
    NEITHER = "Neither"
    IPV4 = "IPv4"
    IPV6 = "IPv6"
    
    def validIPAddress(self, IP: str) -> str:
        if not IP:
            return self.NEITHER

        if '.' in IP:
            octets = IP.split('.')
            if len(octets) != 4:
                return self.NEITHER
            for octet in octets:
                if not octet:
                    return self.NEITHER
                if not octet.isdigit():
                    return self.NEITHER
                if len(octet) > 1 and octet.startswith('0'):
                    return self.NEITHER
                int_value = int(octet)
                if int_value < 0 or int_value > 255:
                    return self.NEITHER
            return self.IPV4

        if ':' in IP:
            octets = IP.split(':')
            if len(octets) != 8:
                return self.NEITHER
            for octet in octets:
                if not octet:
                    return self.NEITHER
                if not octet.isalnum():
                    return self.NEITHER
                if len(octet) > 4:
                    return self.NEITHER
                try:
                    int_value = int(octet, 16)
                    if int_value < 0 or int_value > 65535:
                        return self.NEITHER
                except ValueError:
                    return self.NEITHER
            
            return self.IPV6
        
        return self.NEITHER
        