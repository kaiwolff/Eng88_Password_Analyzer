common_passwords.txt - This list was taken from https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt

### Manual

### Required Files
#### Password Policy

This file is a config file for the password policy, and allows a user to change the various requirements for a password (such as minimum and maximum length, or the list of allowed characters). These can be edited by a user. It is advised to avoid localised characters (2.g £, or Umlauts) as allowed special characters as this interfered our unit testing.

#### Common Passwords File

A file listing (at the moment) 10 thousand common passwords. This serves to protect a user from a basic dictionary attack

The file can be replaced with any list of passwords, as long as it is named "common_passwords.txt". Passwords should be one per line.
### Required Modules

This code imports `configparser`, `random` and `string`.
### Key Functions

#### check_password

This function will take in a user's first and last names, the year of birth and a password to be checked against the user details. The  functions runs checks against the password policy, checks the password against a list of common passwords (see also "Password Policy" and "Common Passwords File", above), and makes sure that no user details are contained in the password. The function then lists which tests are passed (by their test functions returning `True`), and declares the password strong if all tests were passed (weak otherwise).

The information is presented in a list called report, containing a line on a particular test per entry. This is passed to `generate_report`, where the user is given the option to save this information.

#### generate_report

Unpacks the `report` list and prints it for the user to see. Will then offer the user the option of saving the report in a file, calling write_to_file if this option is selected.

#### write_to file

Asks the user if they want to append or overwrite the file `password_report.txt`. prints tested password and report on tests passed or failed into the file.

## Test Functions

Tests were packed into separate functions as this would allow reuse to check any generated passwords. Three test functions were created: `check_policy`, `check_user_details`, and `check_list`.

`check_policy` calls a function to read in the password policy from the filed `password_policy.txt`, and uses the returned values to make sure that the password is the correct length (between `min_length` and `max_length`) and that the password has at least the required number of numbers, lowercase characters, uppercase characters and special characters. If special characters that are not part of the `allowed_specials` string are used, the password policy is considered failed. The policy can be edited via the password_policy.txt file. Will return `True` if password policy is obeyed, `False` otherwise.

`check_user_details` looks for the user details (First name, second name, year of birth) as part of the password. If any user details are found, it returns `False`.

`check_list` looks at the file `common_passwords`, and returns `True` if the password is not part of the list. Otherwise, will return `False`.






