FROM python

COPY requirments.txt .
RUN pip install -r requirments.txt


COPY . .

CMD ["python","main.py"]    