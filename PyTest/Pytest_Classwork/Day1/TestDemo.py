"""
def register():
    print("Regestering...")
def test_register():
    print("Regestering...")
def test_login():
    print("Logging in...")
def test_logout():
    print("Logging out...")

#This wont work 
class demo:
    def test_register():
        print("Regestering...")

    def test_login():
        print("Logging in...")

    def test_logout():
        print("Logging out...")
"""
class Test_demo:
    def test_register(self):
        print("Regestering...")

    def test_login(self):
        print("Logging in...")

    def test_logout(self):
        print("Logging out...")
