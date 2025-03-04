import win32com.client as s

speak = s.Dispatch("SAPI.SpVoice")

names=["atul","anmol","harry","anushka","shantanu","avnish","rishi"]
for n in names:
    g=f"Congratualtions {n}"            
    speak.Speak(g)
