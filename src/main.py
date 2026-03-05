import Tests.test_01_abtest as TC01
import Tests.test_02_add_elements as TC02
import Tests.test_03_basic_auth as TC03 
import Tests.test_04_broken_images as TC04

def main():

    TC01.run()

    TC02.run()

    TC03.run()

    TC04.run()

if __name__ == "__main__":
    main()