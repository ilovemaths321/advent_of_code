import re
FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validPassports = 0
with open("input", "r") as file:
    passports = file.read().split('\n\n')
    for passport in passports:

        # part a
        # presentFields = all(passport.count(field) == 1 for field in FIELDS)
        # if presentFields:
        #     validPassports += 1

        # part b

        ## Regex
        byrRx, iyrRx, eyrRx = r"byr:(\d*)", r"iyr:(\d*)", r"eyr:(\d*)"
        hgtRx = r"hgt:(\d*cm|\d*in)"
        hclRx = r"hcl:#([0-9a-f]*)"
        eclRx = r"ecl:(amb|blu|brn|gry|grn|hzl|oth)"
        pidRx = r"pid:(\d*)"
        fieldsRxlist = [byrRx, iyrRx, eyrRx, hgtRx, hclRx, eclRx, pidRx]
        fullRx = r"".join(rf"(?=.*{field})?" for field in fieldsRxlist)
        fullRx = r"(?sm)" + fullRx  # to look in all lines

        ## Get Fields
        m = re.match(fullRx, passport)
        byr, iyr, eyr, hgt, hcl, ecl, pid = m.groups()
        if hgt != None:
                hgtNum, hgtUnit = int(hgt[:-2]), hgt[-2:]
        else:
                hgtNum, hgtUnit = 0 ,"cm"

        ## Validation
        byrVal = (1920 <= int(byr) <= 2002) if byr != None else False
        iyrVal = (2010 <= int(iyr) <= 2020) if iyr != None else False
        eyrVal = (2020 <= int(eyr) <= 2030) if eyr != None else False
        hgtVal = 150 <= hgtNum <= 193 if hgtUnit == "cm" else 59 <= hgtNum <= 76
        hclVal, eclVal, pidVal = hcl != None, ecl != None, pid != None
        fieldsVallist = [byrVal, iyrVal, eyrVal, hgtVal, hclVal, eclVal, pidVal]

        validFields = all(fieldVal for fieldVal in fieldsVallist)

        if validFields:
            validPassports += 1



print(validPassports)