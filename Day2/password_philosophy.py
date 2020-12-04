import re


class PasswordChecker:

    def __init__(self, txt: str):
        arr = txt.split(" ")
        self.min = int(arr[0].split("-")[0])
        self.max = int(arr[0].split("-")[1])
        self.char = arr[1].replace(":", "")
        self.password = arr[2]

    def check_policy_old(self) -> bool:
        if self.min <= self.password.count(self.char) <= self.max:
            return True
        else:
            print(self.min, self.max, self.char, self.password, self.password.count(self.char))
            return False

    def check_policy_new(self) -> bool:
        if self.password[self.min - 1] == self.char and self.password[self.max - 1] != self.char:
            return True
        elif self.password[self.min - 1] != self.char and self.password[self.max - 1] == self.char:
            return True
        else:
            print(self.min, self.max, self.char, self.password, self.password.count(self.char))
            return False


with open("input.txt") as f:
    x = f.readlines()

x = [x.strip() for x in x]

valid_passwords = 0

for i in x:
    if PasswordChecker(txt=i).check_policy_new():
        valid_passwords += 1

print(valid_passwords)
