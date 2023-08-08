FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# install ffmpeg
RUN apt update && \
  apt install -y --no-install-recommends ffmpeg libavcodec-extra && \
  rm -rf /var/lib/apt/lists/*

VOLUME /usr/src/app

CMD [ "python", "./run.py" ]
