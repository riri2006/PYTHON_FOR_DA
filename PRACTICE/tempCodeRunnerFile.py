def mood():
   print("meri jaanu ka mood kaisa hai jaano ")
def happy():
   print("meri kehsu ka mood ekdm ok hai ")   
def romantic():   
   print("aaj hum khana khaynge ❤️❤️❤️")

commands = {
   "hello":mood(),
   "mwaah":romantic(),
   "puuchi":happy()
}

commands["hello"]
commands["mwaah"]
commands["puuchi"]