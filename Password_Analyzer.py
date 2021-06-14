class PasswordChecker:

    def take_input(self):
        pass
        #Take full user name, year of birth. Ask user what option (generate, check, or exit). # For now, just test variables, shoudl be written up by Munira

    def generate_password(self): # will be written by Afshana
            #check policy, generate random characters that satisfy policy - Afshana working on this.
        pass

    def check_password(self,password, first_name, second_name, birth_year):
        print("opened check_password")
        #check password against password policy, their name, DOB, and common passwords.
        report = []

        policy_compliant = self.check_policy(password)
        # print(f"checked policy compliance {policy_compliant}")

        if policy_compliant:
            report.append("Complies with password policy")
            # print("Complies with password policy")
        else:
            report.append("Does not comply with password policy")
            # print("Does not comply with password policy")

        not_common = self.check_list(password)
        # print("common passwords checked")

        if not_common:
            report.append("Not in list of common passwords")
            # print("Not in list of common passwords")
        else:
            report.append("Found in list of common passwords")
            # print("Found in list of common passwords")

        user_detail_free = self.check_user_details(password, first_name, second_name, birth_year)
        if user_detail_free:
            report.append("No user details in password")
        else:
            report.append("User Details Found in Password")

        if policy_compliant and not_common and user_detail_free:
            report.append("This means that the password is STRONG.")
        else:
            report.append("This means that the password is weak")

        return report

    def check_list(self,password):
        #checks password against passwords in common_passwords.txt. Returns True if password is not in file, False if found
        with open('common_passwords.txt', 'r') as password_file:
            #iterates through whole file
            for line in password_file:
                if password in line:
                    password_file.close()
                    return False
                elif line == False:
                    #line will be empty if nothing left in file
                    print("end of file reached")
                    password_file.close()
                    break
        return True


    def check_policy(self,password):
            # reads password policy, checks if password complies with requirements. Returns True if yes, False if not.
            policy_list = self.read_password_policy()
            #now hav ea list defining password policy
            num_specials = policy_list[0]
            num_lowercase = policy_list[1]
            num_uppercase = policy_list[2]
            num_numbers = policy_list[3]
            min_length = policy_list[4]
            max_length = policy_list[5]
            allowed_specials = policy_list[6]

            count_specials = 0
            count_lower = 0
            count_upper = 0
            count_numbers = 0

            if len(password) < min_length or len(password) > max_length:
                #not compliant if too short or too long
                return False

            for letter in password:
                #check each letter to see if special, lower, upper, or number. Count each of these
                if letter.isdigit():
                    count_numbers += 1
                elif letter.isupper():
                    count_upper += 1
                elif letter.islower():
                    count_lower += 1
                elif letter in allowed_specials:
                    count_specials += 1
                else:
                    #return false if part of password is not in any allowed category
                    print("illegal character")
                    return False

            #now have a count of all the lower, upper, special characters and numbers
            if count_upper >= num_uppercase and count_lower >= num_lowercase and count_specials >= num_specials and count_numbers >= num_numbers:
                return True
            else:
                return False

    def check_user_details(self, password, user_firstname, user_lastname, user_birthyear):
        #checks if the password contains the user name or year of birth. Outputs True if no user details in the password
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
        #ask user if they want to write to file
        wants_file = input("Would you like this written to a file (y/n) ? ")
        if wants_file.lower() == "y":
            write_to_file(report)
        else:
            return "Report not written to file"

    def write_to_file(self, report):
        #writes report to file.
        file = open(password_report.txt, 'w')
        for line in report:
            write.file(f"{line}\n")
        return "Report written to password_report.txt"

    def read_password_policy(self):
        #reads in password policy, returns variables as a list
        # password_policy = open('password_policy.txt', 'r')
        num_specials = 1
        num_lowercase = 3
        num_uppercase = 3
        num_numbers = 4
        min_length = 8
        max_length = 16
        allowed_specials = "~!\"£$%^&*()_-+="

        return [int(num_specials), int(num_lowercase), int(num_uppercase), int(num_numbers), int(min_length), int(max_length), allowed_specials]



    #########################TESTBED

# password_tester = PasswordChecker()
# print("password_tester generated")
# test_list = password_tester.check_password("Test_1929KIl","Kai", "Wolff", "1992")
# print(test_list)

