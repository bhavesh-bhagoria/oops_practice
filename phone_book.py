record_file = "personal_contact.txt"

class contact:

	def add_contact(self):
		name = input("Enter name: ")
		email = input("Enter eamil: ")
		phone = input("Enter phone number: ")
		file = open(record_file, "a")
		file.write(name + "," + email + "," + phone + "\n")
		file.close()
		print("Contact Saved")

	def display(self,contact_info):
		print("----------------------")
		print("Name :", contact_info[0])
		print("Email:", contact_info[1])
		print("Phone:", contact_info[2])
		print("----------------------")

	def search_contact(self):
		name_input = input("Enter name of the contact: ")
		file = open(record_file,"r")
		data = file.readlines()
		file.close()

		for line in data:
			contact_info = line.replace("\n", "").split(",")
			if contact_info[0] == name_input:
				self.display(contact_info)
				return
			else:
				print("Not found")


contact = contact()

while True:
	print("Press 1 to add contact")
	print("Press 2 to search contact")
	print("Press 3 to exit")
	choice = input("Enter the choice: ")
	if choice == "1":
		contact.add_contact()
	elif choice =="2":
		contact.search_contact()
	elif choice == "3":
		break
	else:
		print("Invalid ")



#decorator and iterator