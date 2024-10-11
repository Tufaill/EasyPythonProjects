#i worked on this small task to explore how functions work in python
#how to use potential and keyword argument

#this calculator works in this way lol
''' it checks how many times the letter from the word "True love" appears in both
#    names (like mine: Tufail Hussain).  it counts the occurrence of(true love) in first name(tufail)
#    then it checks in second name(hussain) so in this case it appers 3 and 6 times so 36%'''

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    name_lower_case = combined_names.lower()

#now we are checking how many times "T,r,u,e" is in both name
    t = name_lower_case.count("t")
    r = name_lower_case.count("r")
    u = name_lower_case.count("u")
    e = name_lower_case.count("e")
    first_digit = t + r + u + e

#now we are checking how many times "f,a,l,s,e" is in both name
    l = name_lower_case.count("l")
    o = name_lower_case.count("o")
    v = name_lower_case.count("v")
    e = name_lower_case.count("e")
    second_digit = l + o + v + e

#now we will combine both calculated output
    love_score = str(first_digit)+ str(second_digit)
    print(f"Your total love score is {love_score}%")

calculate_love_score(name1="Tufail", name2="hussain")

