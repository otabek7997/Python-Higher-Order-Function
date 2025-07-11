emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

domains= list(filter(lambda email: email.endswith("@gmail.com"), emails))

print(domains)
