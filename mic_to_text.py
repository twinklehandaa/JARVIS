import speech_recognition as sr

# index = 5 #or 9
# for name in sr.Microphone.list_microphone_names():
#     print(index," ",name)
#     # print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
#     index=index+1

recognizer = sr.Recognizer() #object created of inbuilt class Recognizer

def mic1():
    with sr.Microphone(device_index=0) as source:
        print("Say something: ")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source) #Audio
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said: ", text)
        return text
    
if __name__ == "__main__":
    mic1()
