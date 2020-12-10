# FAQ Decition tree Excel to Json 

## Overview
This Code process and excel file with a decition tree extructure to create a json that the QnA Chat bot can import.

There are some requirements for the excel:

 * The Excel file should be in the same folder that main.py (you can change the code to point to other location if needed)

 * NUMBER OF COLUMNS MATTER, DELETE ON THE EXCEL THE UNNECESARY RIGHT COLUMNS.

 * FIRST COLUMN SHOULD BE STARTING POINT OF THE GUIDED CONVERSATION. SAME VALUE FOR ALL THE EXCEL ROWS

 * THE 3 LAST COLUMNS SHOULD BE THE INDIVIDUAL QUESTIONS. ALWAYS NEEDED TO BE FILLED. EACH QUESTION WITH UNIQUE ID.

 * NO VALUE ON THE EXCEL SHOULD BE THE SAME OR THE TRAINING COULD BE PROBLEMATIC, IF THERE IS 2 BRANCH OF THE TREE WITH
    SIMILAR QUESTIONS, CHANGE FOR EXAMPLE THE CELL VALUE WITH SOME PREFIX BASED ON THE BRANCH

## RUN

The code runs in Python3. To install dependencies run:

    > pip3 install -r requirements.txt

If you have python3 linked to pip and not pip3 you will have to run:

    > pip3 install -r requirements.txt