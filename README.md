# stocks_pred
Aplikacja pozwala na przewidywanie kursu akcji na giełdzie na podstawie cen otwarcia, zamknięcia, najwyższych i najniższych dnia poprzedniego. Poniższy screenshot prezentuje wygląd interfejsu aplikacji używając streamilta:
<img width="433" alt="stocks" src="https://github.com/s23218/SUML/assets/79990066/a7d8e762-261f-4dac-af3f-4a2e097b2e8b">

Do uruchomienia fast api należy wykonać następujące komendy:
- cd src/fastpi
- uvicorn modelapi:app --reload

Do uruchomienia aplikacji streamlit należy wykonać następującą komendę:
- streamlit run app.py

Użyte technologie:
- sqlalchemy: do wysłania danych treningowych do bazy danych postgres
- kedro: podzielenie kodu na pipeliny i nody
- yfinance: uzyskanie danych o akcjach
- streamlit: aplikacja webowa umożliwiająca wykonanie predykcji oraz uruchomienie pipelinów
