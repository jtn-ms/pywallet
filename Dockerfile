FROM python:3.7
# Or any preferred Python version.
RUN git clone https://github.com/jtn-ms/pywallet.git
RUN pip install -r requirements.txt
CMD ["bash"] 
# Or enter the name of your unique directory and parameter set.
