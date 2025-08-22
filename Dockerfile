FROM nikolaik/python-nodejs:python3.10-nodejs20 
 
# Update package lists and install ffmpeg 
RUN apt-get update \ 
    && apt-get install -y --no-install-recommends ffmpeg \ 
    && apt-get clean \ 
    && rm -rf /var/lib/apt/lists/* 
     
 
COPY . /app/ 
WORKDIR /app/ 
RUN pip3 install --no-cache-dir -U -r requirements.txt 
 
CMD bash start
