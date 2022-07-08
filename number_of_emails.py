"""
Problem Statement:
------------------
Every email consists of a local name and a domain name, separated by the @ sign.
abc@xyz.com
For example, in alice@abc.com, alice is the local name, and abc.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.
ab.c@xyz.com => abc@xyz.com
If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@abc.com" and "alicez@abc.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

ab.c+de@xyz.com => abc@xya.com
If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails?

Example 1:
Input: ["test.email+alex@abc.com",
    "test.e.mail+bob.cathy@abc.com","testemail+david@ab.c.com"]
Output: 2
Explanation: "testemail@abc.com" and "testemail@ab.c.com" actually receive mails


Note:
1 <= emails[i].length <= 100
1 <= emails.length <= 100
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
"""


def solve(emails):
    # initializing an empty set to store correct email addresses as set only contains unique elements.
    answer = {''}
    
    for email in emails:
        # splitting the email into account name and domain name.
        account, domain = email.split("@")

        # removing the '.' before all the '+' symbol
        account = account.split("+")[0].replace(".", "")

        # adding the correct email address into the answer set.
        answer.add(account + "@" + domain)

    return len(answer)-1


if __name__ == '__main__':
    emails = ["test.email+alex@abc.com",
              "test.e.mail+bob.cathy@abc.com", "testemail+david@ab.c.com"]
    answer = solve(emails)

    print(answer)
