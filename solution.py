from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
   mailserver='localhost'
   port=25

   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.bind ((mailserver, port))
   clientSocket.connect((mailserver, port))
   #clientSocket.listen(1)
   #connectionSocket.addr = clientSocket.accept()


   recv = clientSocket.recv(1024).decode()

   if recv[:3] != '220':


   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()


   if recv[:3] != '250':


   # Send MAIL FROM command and print server response.
   mailFrom = "MAIL FROM: <jason.a.rivera@gmail.com> \r\n"
   clientSocket.send(mailFrom.encode())
   recv = clientSocket.recv(1024)

   if recv[:3] != '220':

   # Send RCPT TO command and print server response.
   rcpTo= "RCPT TO: <jar10045@nyu.edu> \r\n"
   clientSocket.send(rcptTo.encode())
   recv3 = clientSocket.recv(1024)

   if recv[:3] != '220':

# Send DATA command and print server response.
   data = "DATA\r\n"
   clientSocket.send(data.encode())
   recv4 = clientSocket.recv(1024)

   if recv[:3] != '220':

   # Send message data.
   subject = "Subject: SMTP mail client testing \r\n\r\n"
   clientSocket.send(subject.encode())
   message = raw_input("Enter your message: \r\n")
   clientSocket.send(message.encode())
   clientSocket.send(endmsg.encode())
   recv_msg = clientSocket.recv(1024)

   if recv[:3] != '220':

   # Message ends with a single period.
   # Fill in start
   # Fill in end

   # Send QUIT command and get server response.
   clientSocket.send("QUIT\r\n".encode())
   message = clientSocket.recv(1024)

   clientSocket.close()



if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')
