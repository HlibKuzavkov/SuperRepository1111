from revision import utils


print(utils.is_safe('qWertyu5')) # всі умови задовільнені
print(utils.is_safe('qW5')) # <8
print(utils.is_safe('QWERTYU5')) #без lowercase
print(utils.is_safe('qwertyu5')) # без Uppercase
print(utils.is_safe('qWertyuh')) # не має числа


print(utils.has_duplicate([1,2,1]))
print(utils.has_duplicate([1,2,3]))

print(utils.is_warm(750))
print(utils.is_warm(-100))