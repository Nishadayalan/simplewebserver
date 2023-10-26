from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
	<title> INAMGE MAP </title>
	<body>
		<table border="8" cellspacing="20" cell padding="60">
			<caption> TOP FIVE REVENUE GENERATING SOFTWARE COMPANIES </caption>
			<tr>
				<th>S.NO</th>
				<th>Company</th>
				<th>Revenue</th>
			</tr>
			<tr>
				<td>1</td>
				<td>microsoft</td>
				<td>65 billion</td>
			</tr>
			<tr>
				<td>2</td>				
				<td>Oracle</td>
				<td>29.6 billion</td>
			</tr>
			<tr>
				<td>3</td>				
				<td>IBM</td>
				<td>29.1 billion</td>
			</tr>
 			<tr>
				<td>4</td>
				<td>SAP</td>
				<td>6.4 billion</td>
			</tr>
			<tr>
				<td>5</td>
				<td>Symantic</td>
				<td>5.6 billion</td>
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