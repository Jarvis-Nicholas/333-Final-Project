#cd 333/homework/final/333-Final-Project

FROM python:3

# /app accesses all files in current directory
WORKDIR /usr/src/app


#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

#RUN pip update
RUN pip install --no-cache-dir -r
# Copies all files from current directory
COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]