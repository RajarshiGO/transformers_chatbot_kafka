FROM ubuntu
RUN apt update && apt install -y python3 python3-pip nginx
RUN mkdir /app
WORKDIR /app
ADD ./static ./static
ADD ./templates ./templates
ADD ./download_model.py ./
ADD ./tokenizer.pt ./
COPY ./app.py ./
COPY ./model.py ./
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./nginx.conf /etc/nginx/nginx.conf
COPY ./script.sh ./
RUN chmod a+x script.sh
RUN python3 download_model.py
EXPOSE 80
CMD ["./script.sh"] 