import smtplib

def main(text):
	# Set up the SMTP server
	smtp_server = "smtp.gmail.com"
	port = 587
	username = <your email address>
	password = <password>

	# Create a message
	message = """
	%s
	"""%(text)

	# Send the message
	with smtplib.SMTP(smtp_server, port) as server:
	    server.starttls()
	    server.login(username, password)
	    server.sendmail(username, "<Receiver's Address>", message)

	print("Email sent successfully!")

if __name__ == '__main__':
	main('This is a Test Email')

