# MCserver-alert
A discord webhook to alert if player joins/leaves your minecraft server by sending a message to your discord channel

## Usage
1. Install [python](https://www.python.org/)
2. Rename `.env.example` file to `.env`
3. Store the following values:
```
WEBHOOK="Enter your webhook url here"
LOGPATH="Enter your latest.log file path here"
```
4. Install dependencies:
   * ```pip install -r requirements.txt```
   
	* For manual installation:
        
        * `pip install discord-webhook` 
        * `pip install python-dotenv`
        
 

5. Run the `alert.py`

     > **NOTE**: This was tested in `Python 3.9`.
     
