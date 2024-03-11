from queue import LifoQueue
import time as t

fordward_history = LifoQueue()
backward_history = LifoQueue()
current_page = None

#visit the function
number_of_visits = int(input("Eenter the number of url histort: "))
print("\n Enter URL to visit: ")

for i in range(number_of_visits):
    url = input("URL: ")
    print(f"Visisting {url}")
    t.sleep(1)
    backward_history.put(current_page)
    current_page =  url
    print (f"Current Page: {current_page}\n")


#Go back
while input("Do you want to go back? (yes or no): ").lower() == "yes":
    if not backward_history.empty():
        fordward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}\n")
        t.sleep(1)
    else:
        print ("No previous page available\n")

while input("Do you want to go forward? (yes or no): ").lower() == "yes":
    if not fordward_history.empty():
        backward_history.put(current_page)
        current_page = fordward_history.get()
        print (f"Going forward to {current_page}\n")
        t.sleep(1)
    else:
        print("No forward page available\n")























    
