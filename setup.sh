mkdir -p ~/.streamlit/

echo "
[theme]
primaryColor=’#020202’
backgroundColor=’#c4c3c3’
secondaryBackgroundColor=’#ebd316’
font = ‘sans serif’
\[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
