

# * pip install selenium
# Selenium is a tool that helps computers do things on websites automatically.
# Imagine you want to do some tasks on a website, like filling out forms, clicking buttons, or checking information. Instead of doing all of these tasks manually, Selenium allows you to write a computer program in languages like Python or Java to do these tasks automatically.
# It's like having a robot that can use a web browser and follow your instructions to interact with websites without you having to click or type things yourself. Selenium is commonly used for things like testing websites and automating repetitive web tasks.

from time import sleep # Inbuilt
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.options import Options # pip install selenium
from selenium.webdriver.common.by import By # pip install selenium
import warnings # Inbuilt
from selenium.webdriver.chrome.service import Service

# Configuring the webdriver to automate the program for utilizing ChatGPT as a backend model.


# to ignore all the unwanted warnings in terminal by selenium
warnings.simplefilter("ignore")

try:
    Link = "https://gpt4login.com/use-chatgpt-online-free/"
    chrome_driver_path = 'Brain\\chromedriver.exe'
    chrome_options = Options()
    chrome_options.headless = True #! TRY TO CHANGE THIS
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--log-level=3')
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(Link)

except Exception as e:
    print("To resolve this error, you should set up the ChromeDriver properly.")
    print("*For the successful execution of this program, it is essential to configure and set up the ChromeDriver.")
    print(e)

# Storing the previous conversation ID for reference.

def FileReader():
        
    try:
        File = open("Brain\\Chatnumber.txt","r")
        Data = File.read()
        File.close()
        return Data

    except Exception as e:
        print(e)

# Reading the previous conversation ID for reference.

def FileWriter(Data):

    try:
        File = open("Brain\\Chatnumber.txt","w")
        File.write(Data)
        File.close()

    except Exception as e:
        print(e)

# Initiating the primary execution phase while utilizing ChatGPT as the backend model.

def ChatGPTBrain(Query):
    Query = str(Query)

    try:
        # type the query
        # XML path  inspect->select desired element->in code->right click->copy xpath
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/div/textarea").send_keys(Query)
        sleep(1)

    except:
        print("*The Input button or Input Section does not appear to be readily accessible or available within the current context or environment.*")
        print("*Consider modifying the path for the 'Input' element, which is available on the website.*")

    try:
        # click the send btn
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/button/span").click()

    except:
        print("*The Send.Keys() function or button does not appear to be readily accessible or available within the current context or environment.*")
        print("*Consider modifying the path for the 'Send' button, which is available on the website.*")

    try:
        # for continious chat then the answer displayed will be lower and lower ..so used this 
        Data = str(FileReader())

    except:
        print("*Could Not Be able to access the file Where Chatnumber is saved for reference.")

    # getting the answer
    while True:

        sleep(0.5)
        
        try:

            try:
                AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
                Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).is_displayed()
                if str(Answer)=="True":
                    break

            except:
                # print("*The response text element cannot be located. Please ensure that you update its selector or locator.")
                pass

        except:
            pass
    
    try:
        AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
        Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).text

    except:
        print("*The response text element cannot be located. Please ensure that you update its selector or locator.")

    NewData = int(Data) + 2 # because 1 div=query(Hi! How can I help you) , 2div=ansToQuery
    FileWriter(Data=str(NewData))
    return Answer

# Commencing the main execution phase.

def MainExecutionChatGPT():

    print("")
    print("Initiating the GPT-4 model.")
    FileWriter(Data='3') #mean third div(Hi! How can I help you?) as 1div=AI(Hi! How can I help you?) ,.2div=query, 3div=ansOfQuery

    while True:
            
        try:
            # Query = input("Enter Your Query : ")
            # print(ChatGPTBrain(Query=Query))

            File= open("Body\\SpeechRecognition.txt", "r")
            Data=File.read()
            File.close()

            FileHistory= open("Brain\\HistoryChat.txt", "r")
            DataHistory= FileHistory.read()
            FileHistory.close()


            if str(Data)==str(DataHistory):
                sleep(0.5)
                pass
            else:
                Result= ChatGPTBrain(Data)
                print(Result,"\n\n")

                FileHistory= open("Brain\\HistoryChat.txt", "w")
                FileHistory.write(Data)
                FileHistory.close()
        
        except Exception as e:
            print(e)
        


MainExecutionChatGPT()