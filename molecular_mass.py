import re

atomic_num = {"H":1,"He":2,"Li":3,"Be":4,"B":5,"C":6,"N":7,"O":8}
element_names = ("Hydrogen","Helium","Lithium","Berylium","Boron","Carbon","Nitrogen","Oxygen")
atomic_mass = (1.01, 4, 6.94, 9.01, 10.81, 12.01, 14.01,16)

def Element_count(chemFormula):
    chemSplit = re.findall('[A-Z][^A-Z]*', chemFormula)
    elementCount = [0,0,0,0,0,0,0,0]
    for x in chemSplit:
        n=1
        if x[-1].isnumeric():
            num_list = re.findall('\\d+', x)
            n = int(num_list[0])
        elementSyb = re.findall('\\D+', x)[0]
        atomic_number = atomic_num[elementSyb]
        elementCount[atomic_number-1] = elementCount[atomic_number-1] + n
    return elementCount


def Element_Report(elementCount,atomic_num,element_names):
    print("This is the composition of the molecule")
    for i in range(len(atomic_num)):
        if elementCount[i]==0:
            continue
        n = elementCount[i]
        elementName = element_names[i]
        print(f"{elementName} = {n}")

def dot(K, L):
   if len(K) != len(L):
      return 0
   
   return sum(i[0] * i[1] for i in zip(K, L))

def main():
    Chem = input("Enter Chemical formula: ")
    if not Chem.isalnum():
        print("Non-valid input")
        return
    ElemetCount = Element_count(Chem)
    molecularMass = dot(atomic_mass,ElemetCount)
    print(molecularMass)
    Element_Report(ElemetCount,atomic_num,element_names)

main()