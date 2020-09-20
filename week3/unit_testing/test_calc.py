#another team, integration testing team
#team, dev team

from calc import calc_add

if calc_add(7,8) == 15: #fixed inputs, expected outcome
    print("Good")
else:
    print("bad")

# Fail faster
assert calc_add(7,8) == 15
assert calc_add(3,10) == 13
assert calc_add(7.0,1.0) == 8.0
assert calc_add("7","8") == 16
assert calc_add("7","8.5") == 15.5
# make dev code crash/fail

# grouping things, reports, enable/disable, run only subset


print(calc_add(7,8))
print(calc_add(0.3,0.7))
print(calc_add(-3, 8))

#inputs can vary, string inputs
print(calc_add("4888","6999")) #3rd month of delivery.

#
print(calc_add("4.8","7.2")) #3rd month of delivery.