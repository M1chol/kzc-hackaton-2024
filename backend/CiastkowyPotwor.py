# import requests

# # Tworzenie sesji
# session = requests.Session()

# # Wysłanie żądania GET i automatyczne zapisanie cookies
# response = session.get('https://example.com')
# print(response.cookies)  # Wyświetlenie cookies otrzymanych z serwera

# # Użycie zapisanych cookies w kolejnym żądaniu
# response = session.get('https://example.com/somepage')
# print(response.text)  # Wyświetlenie zawartości odpowiedzi

# def addUser(UID: int) -> None:
#     session.cookies.set('UID', f'{UID}')

# def userRead() -> int:


# # Wysłanie żądania z własnymi cookies
# response = session.get('https://example.com/anotherpage')
# print(response.text)