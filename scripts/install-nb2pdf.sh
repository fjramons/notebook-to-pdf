#!/bin/bash

echo >> ~/.bashrc
echo "# Alias for conversion of notebooks to PDF" >> ~/.bashrc
echo "alias nb2pdf='docker run -it \
--rm \
-v \"\${PWD}\":/workdir \
fjramons/notebook2pdf'" >> ~/.bashrc
