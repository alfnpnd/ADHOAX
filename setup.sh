mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
"
[theme]
primaryColor = "#E694FF"
backgroundColor = "#00172B"
secondaryBackgroundColor = "#0083B8"
textColor = "#DCDCDC"
font = "sans-serif"> ~/.streamlit/config.toml
