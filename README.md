# UIU-LMS-info-extractor
This application uses a variety of technologies, including Web Scraping and web Automation, to obtain participant information for a course that is only accessible to UIU students.

## Technologies Used
- Python : Used programming language
- BeautifulSoup : For scraping webpages to get info
- Playwright : For web automation 
- Excel : Storing all obtained participant information
- Tkinter : Simple GUI
- Pillow / PIL : used for image processing
- Requests : The requests module allows us to send HTTP requests
- Multiprocessing : It utilizes multiple CPU cores to make the program work faster

## Tutorial
1. Turn off Windows Security if the .exe file gets detected as a threat
1. Launch the browser of your choice.
2. Open the LMS site and log in.
3. Navigate to the Participants page of the course from which 
    you need to retrieve participant data.
4. Copy the link in the address bar.
5. The URL should have this format: 

    `https://lms.uiu.ac.bd/user/index.php?id=****`
6. Now, open the Application (.exe file).
7. Put your username & password. (Don't worry. Your credentials aren't being stored anywhere) 
8. Paste the link you copied and hit the "Proceed" button
9. Now, you're all good. The program will do its job and after some time (usually takes 20-30 seconds depending on internet speed or number of participants) it will generate an Excel file
10. The Excel file will look like this:

    | Name         | ID                  | Email            |
    | ------------ | ------------------- |------------------|
    |name 1  | ID of name 1           |Email of name 1
    |name 2  | ID of name 2           |Email of name 2
    |name 3  | ID of name 3           |Email of name 3

#### How to run this program
----
If your windows pc has Google Chrome or Microsoft Edge, then download the [LMS info extractor.exe](https://github.com/skupperr/UIU-LMS-info-extractor/blob/main/LMS%20info%20extractor.exe)

If you don't have either of those, then download [LMS info extractor (All Browser).exe](https://github.com/skupperr/UIU-LMS-info-extractor/blob/main/LMS%20info%20extractor%20(All%20Browser).exe) (It's a huge file because there is a browser built into this)


## Project Dependencies
- Playwright
    ```bash
        pip install pytest-playwright
- Install playwright browser
    ```bash
        playwright install
- BeautifulSoup
    ```bash
        pip install beautifulsoup4
- Tkinter
    ```bash
        pip install tkinter
- Pillow / PIL
    ```bash
        pip install pillow

- Rest of the libraries are Python built-in libraries 

### Workflow of this Application 
Firstly, it logs into the official side of LMS using the user's credentials and heads over to the link given by the user. Secondly, it scrapes all the profile links of the perticipants and put them in a list. Then it goes through all of the profiles, scrapes informations and put them in an Excel file
