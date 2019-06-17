FROM azuresdk/azure-cli-python
RUN apk add --no-cache expect
RUN mkdir -p /home/minerhero
ADD . /home/minerhero
WORKDIR /home/minerhero
RUN pip install -r requirements.txt
CMD ["bash","loop10.sh"]
