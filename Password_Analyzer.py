class PasswordChecker:

    def __init__(self):


    def take_input:
        #Take full user name, year of birth. Ask user what option (generate, check, or exit).

        user_firstname = kai#input('Enter your first name:')
        user_secondname = wolff#input('Enter your first name:')
        user_birthyear = "1992"#input('Enter your year of birth:')
        user_password = ""

        # user_input = input("")
        # if user_input == "end":
        #     break
        # if again == no:
        #     break

    def generate_password:
            #check policy, generate random characters that satisfy policy

    def check_password(self,password):
        #check password against password policy, their name, DOB, and common passwords.
        report = []
        policy_compliant = self.check_policy(password)

        # if policy_compliant:
        #     report.append("Complies with password policy")
        # else:
        #     report.append("Does not comply with password policy")

        # not_common = self.check_list(password)

        # if not_common:
        #     report.append("Not in list of common passwords")
        # else:
        #     report.append("Found in list of common passwords")

        user_detail_free = self.check_user_details(password)
        if user_detail_free:
            report.append("No user details in password")
        else:
            report.append("User Details Found in Password")

        if policy_compliant and not_common and user_detail_free:
            report.append("This means that the password is STRONG.")
        else:
            report.append("This means that the password is weak")

    def check_list(self,password):
        #checks if the given password is part of the common password list.
        password_file = open('common_passwords.txt', 'r')

        while True:
            #iterates through whole file
            line = password_file.readline()
            if password in line:
                return False
            elif line == False:
                #line will be empty if nothing left in file
                break
        return True


def check_policy(self,password):
        # open policy file, output True or False depending whether password complies
def check_user_details(self, password, user_firstname, user_lastname, user_birthyear):
    #checks if the password contains the user name or year of birth. Outputs T
    if user_firstname in password:
        return False
    elif user_lastname in password:
        return False
    elif user_birthyear in password:
        return False
    else:
        return True


    def generate_report(self,report):
        #formats output in human-readable way. Checks if user wants this put into a file.
        for line in report:
            print(line)
        #ask user if they want to
        wants_file = input(Would you like this written to a file (y/n) ? )
        if wants_file.lower() == "y":
            write_to_file(report)
            return "Report written to file"
        else:
            return "Report not written to file"

    def write_to_file(self, report):
        #writes report to file.
        file = open(password_report.txt, 'w')
        for line in report: