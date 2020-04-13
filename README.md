# Bowflex website bot

This project is designed to automatically checkout any product on the bowflex webpage

# Dependencies 
 
selenium 

chromedriver, navigate to the config.json and modify the directory to your computers chromedriver directory. You can download the version for your computer here https://chromedriver.chromium.org/ .

```
pip install selenium
```

pyautogui

```
pip install pyautogui
```


# How to run

First navigate to both the shipping.json file then the billing.json and replace the text with your respective billing and shipping details. 


```
python bot.py
```

When the script is launched the console will prompt you for a product link. After the link is inputted, a web browser window will open. After that, the script should do the rest of the work.


