# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file not exists just return 0
def occurances_of_letter_a(file_name):
    try:
        f = open(file_name)
        file_content = f.read()
        f.close()
        result = 0
        for i in file_content:
            if i.lower() == 'a':
                result += 1
        return result
    except:
        return 0
