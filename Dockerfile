FROM python:3.11.3-bullseye

RUN apt-get update && \
    apt-get install --yes \
        pandoc \
        texlive-fonts-recommended \
        texlive-plain-generic \
        texlive-xetex && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY /src .

WORKDIR /workdir

ENTRYPOINT ["python", "/app/add-metadata.py"]
