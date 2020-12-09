:: prereqs to run with python
:: pip3 install -r requirements.txt
:: chmod +x crypt.py

:: cmd part
:: grab encrypted key from email
:: in my case, I ran: 
:: ./crypt -i saitama.txt -o onepunch.man -m CTR -l 256

:: decrypt file 
crypt.py -d -i onepunch.man -o capedbaldy.txt -m CTR -l 256