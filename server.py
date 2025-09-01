from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>

</head>
<body>
    <center>TCP/IP Layers and Protocols<center>
    <table border="1" align="center" cellpadding="9" bgcolor="red">
        <tr>
            <th>TCP/IP Layers</th>
            <th>Protocols (Examples)</th>
        </tr>
        <tr>
            <td>Application Layer</td>
            <td>HTTP, RDP, DNS, SMTP, Telnet, SNMP</td>
        </tr>
        <tr>
            <td>Transport Layer</td>
            <td>TCP, UDP</td>
        </tr>
        <tr>
            <td>Internet Layer</td>
            <td>ICMP, IGMP, ARP, IP, IPSec</td>
        </tr>
        <tr>
            <td>Network Access Layer</td>
            <td>Ethernet (IEEE 802.3), Token Ring, PPP, Frame Relay</td>
        </tr>
    </table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()