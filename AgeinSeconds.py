def age_in_seconds():
    user_age, user_month = input("Enter your age in years & month: ").split()
    print("Age entered: ", user_age)
    print("Months entered: ", user_month)
    age_seconds = (int(user_age) * 365 * 24 * 60 * 60)
    month_seconds = (int(user_month) * 30 * 24 * 60 * 60)
    total_seconds = age_seconds + month_seconds
    print(age_seconds)
    print(month_seconds)
    print("You have lived for {} seconds.".format(total_seconds))

age_in_seconds()