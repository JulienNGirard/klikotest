FROM radioastro/casa:4.6


RUN apt-get update && \
    apt-get install -y \
        python-astropy \
    && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD main.py /
ADD requirements.txt /
RUN pip install -r /requirements.txt

# klikonise the container
ADD kliko.yml /
ADD kliko /
RUN pip install kliko

