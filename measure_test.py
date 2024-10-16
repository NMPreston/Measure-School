# Noah Preston . CSC-231-001

from measure import FootMeasure 

def run_examples():
    print("FootMeasure output: ")
    measure1 = FootMeasure()
    measure2 = FootMeasure(feet = 4)
    measure3 = FootMeasure(feet = 4, inches = 8)
    measure4 = FootMeasure(inches = 56)

    print(measure1)
    print(measure2)
    print(measure3)
    print(measure4)

    print("\nFootMeasure addition: ")
    measure5 = measure2 + measure3 
    print(measure5)

    measure6 = measure3 + measure4
    print(measure6)

    print("\nFootMeasure relational operators:")
    print(measure3 == measure4)  # True
    print(measure2 != measure3)  # True
    print(measure2 < measure3)   # True
    print(measure3 > measure2)   # True
    print(measure2 <= measure3)  # True
    print(measure3 >= measure4)  # True

    print("\nTesting boundary conditions:")
    measure7 = FootMeasure(feet =0 , inches = 0)
    print(measure7)  

if __name__ == "__main__":
    run_examples()