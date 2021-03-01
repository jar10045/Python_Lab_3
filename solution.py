from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
 msg = "\r\n My message"
 endmsg = "\r\n.\r\n"


# Create socket called clientSocket and establish a TCP connection with mailserver and port
 clientSocket = socket(AF_INET, SOCK_STREAM)
 clientSocket.connect((mailserver, port))
 clientSocket.listen(1)
 recv = clientSocket.recv(1024).decode()
 if recv[:3] != '220':
    pass 

 # Send HELO command and print server response.
 HELOCommand = 'HELO Alice\r\n'
 clientSocket.send(HELOCommand.encode())
 clientSocket.listen(1)
 recv = clientSocket.recv(1024).decode()
 if recv[:3] != '250':
    pass


 # Send MAIL FROM command and print server response.
 MAIL = "MAIL FROM: <jar10045@nyu.edu> \r\n"
 clientSocket.send(MAIL.encode())
 clientSocket.listen(1)
 recv = clientSocket.recv(1024).decode()
 if recv[:3] != '250':
    pass


 # Send RCPT TO command and print server response.
 RCPT = "RCPT TO: <jar10045@nyu.edu> \r\n"
 clientSocket.send(RCPT.encode())
 clientSocket.listen(1)
 recv = clientSocket.recv(1024).decode()
 if recv[:3] != '250':
    pass

 # Send DATA command and print server response.
 DATA = "DATA\r\n"
 clientSocket.send(DATA.encode())
 clientSocket.listen(1)
 recv = clientSocket.recv(1024).decode()
 if recv[:3] != '250':
    pass

 # Send message data.
 SUBJECT = "Subject: SMTP mail client testing \r\n\r\n"
 clientSocket.send(SUBJECT.encode())
 clientSocket.send(msg.encode())
 clientSocket.send(endmsg.encode())
 clientSocket.listen(1)
 recv = clientSocket.recv(1024).decode()
 if recv[:3] != '250':
    pass

 # Message ends with a single period.
 ENDMSG = "\r\n.\r\n"
 clientSocket.send(ENDMSG.encode())
 recv= clientSocket.recv(1024).decode()
 if recv[:3] !='250':
    pass

 # Send QUIT command and get server response.
 clientSocket.send("QUIT\r\n".encode())
 msg = clientSocket.recv(1024).decode()
 clientSocket.close()



 if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
