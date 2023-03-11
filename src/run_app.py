import os
import webbrowser

def main():

    port = 8000
    enable_cors = False
    enable_xsrf_protection = False
    headless = True

    cmd = f"streamlit run --server.port={port} --server.enableCORS={enable_cors} --server.enableXsrfProtection={enable_xsrf_protection} --server.headless={headless} src/Home.py"
    os.system(cmd)

    url = f"http://localhost:{port}"
    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    main()
