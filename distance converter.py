distance = float(input("Distance: "))
distance = float(distance)
unit = input("Is this in Miles(M) or Kilometers(KM)?: ")
if unit.upper() == "M":
    converted = float(distance) * 1.6
    print(str(converted) + "KM")
else:
    converted = float(distance) / 1.6
    print(str(converted) + "M")