#cd 333/homework/final/333-Final-Project


# Command line to run DOCKER_BUILDKIT=0 docker build .

FROM python:3


ADD main.py .
ADD poke_center.py .
ADD pokemon_owner.py .
ADD pokemon_trainer.py .
ADD pokemon.py .
ADD pokemon_list.txt .
ADD research_lab.py .
ADD battle_stadium.py .


#ADD 333/homework/final/333-Final-Project .



#RUN pip install requests beautifulsoup4

CMD ["python", "./main.py"]



# /app accesses all files in current directory
#WORKDIR /usr/src/app


#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

#RUN pip update
#RUN pip install --no-cache-dir -r
# Copies all files from current directory
#COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]