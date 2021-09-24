mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = ‘#DAD873’
backgroundColor = ‘#454D66’
secondaryBackgroundColor = ‘#31333F’
textColor= ‘#309975’
font = ‘sans serif’
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
