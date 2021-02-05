This python program web scrapes prices for specified cryptocurrencies, and sends desktop notifications when a price moves above or below a threshold.

Python dependencies:

requests
bs4
numpy
win10toast

The `Crypto Notify` folder also contains a batch file `Crypto_Price.bat` which can be run through windows scheduler to run the python file on a regular interval.
To use the batch file, replace `C:\your\python\directory\python.exe` with your python directory.
