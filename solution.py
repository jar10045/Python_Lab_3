from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"


   #Create socket called clientSocket and establish a TCP connection with mailserver and port
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((mailserver, port))
   recv = clientSocket.recv(1024).decode()
   if recv[:3] != '220':
      pass

   #Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   if recv1[:3] != '250':
      pass


   #Send MAIL FROM command and print server response.
   mailfrom = "MAIL FROM: <jar10045@nyu.edu> \r\n"
   clientSocket.send(mailfrom.encode())
   recv2 = clientSocket.recv(1024).decode()
   if recv2[:3] != '250':
      pass


   #Send RCPT TO command and print server response.
   RCPTTO = "RCPT TO: <jar10045@nyu.edu> \r\n"
   clientSocket.send(RCPTTO.encode())
   recv3 = clientSocket.recv(1024).decode()
   if recv3[:3] != '250':
      pass

   #Send DATA command and print server response.
   DATA = "DATA\r\n"
   clientSocket.send(DATA.encode())
   recv4 = clientSocket.recv(1024).decode()
   if recv4[:3] != '250':
      pass

   #Send message data.
   SUBJECT = "Subject: SMTP mail client testing \r\n\r\n"
   clientSocket.send(SUBJECT.encode())
   clientSocket.send(msg.encode())
   recv5 = clientSocket.recv(1024).decode()
   if recv5[:3] != '250':
      pass

   #Message ends with a single period.
   full_message = msg + endmsg
   clientSocket.send(full_message.encode())
   recv6 = clientSocket.recv(1024).decode()
   if recv6[:3] !='250':
      pass

   #Send QUIT command and get server response.
   QUIT = "QUIT\r\n"
   clientSocket.send(QUIT.encode())
   msg = clientSocket.recv(1024).decode()
   clientSocket.close()


if __name__ == '__main__':
   smtp_client(1025,'127.0.0.1')
