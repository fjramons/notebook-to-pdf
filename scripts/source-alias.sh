
# Alias for conversion of notebooks to PDF
alias nb2pdf='docker run -it \
--rm \
-v "${PWD}":/workdir \
fjramons/notebook2pdf'
