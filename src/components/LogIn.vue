<template>
    <div class="main">
        <h1>Wat Connect</h1>
        <h3>Wpisz tutaj swoje dane:</h3>
        <form id="loginForm" @submit="dupsko(e)" action="GET">
            <label for="first">
                  Nazwa:
              </label>
            <input type="text" 
                   id="username"
                   name="username" 
                   placeholder="Wpisz nazwę" required>

            <label for="password">
                  Hasło:
              </label>
            <input type="password"
                   id="password" 
                   name="password" 
                   placeholder="Wpisz hasło" required>

            <div class="wrap">
                <button type="submit"
                        onclick="solve()">
                    Prześlij
                </button>
            </div>
        </form>
        <p>Nie zarejestrowany?
              <a href="#" 
               style="text-decoration: none;">
                Stwórz konto
            </a>
        </p>
    </div>
</template>
<script setup>
    const tokenUrl = 'http://127.0.0.1:8000/token';

    async function getToken(formData) {
        const response = await fetch(tokenUrl, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        return data.access_token;
    }

    async function dupsko (event){
        event.preventDefault();

        const formData = new FormData(this);
        const token = await getToken(formData);

        // Wyświetlamy token w konsoli
        console.log(token);
    }
</script>
<style scoped>
.main {
    background-color: #fff;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
    padding: 10px 20px;
    transition: transform 0.2s;
    width: 500px;
    text-align: center;
}

h1 {
    color: #4CAF50;
}

label {
    display: block;
    width: 100%;
    margin-top: 10px;
    margin-bottom: 5px;
    text-align: left;
    color: #555;
    font-weight: bold;
}


input {
    display: block;
    width: 100%;
    margin-bottom: 15px;
    padding: 10px;
    box-sizing: border-box;
    border: 1px solid #ddd;
    border-radius: 5px;
}

button {
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
    margin-bottom: 15px;
    border: none;
    color: white;
    cursor: pointer;
    background-color: #4CAF50;
    width: 100%;
    font-size: 16px;
}

.wrap {
    display: flex;
    justify-content: center;
    align-items: center;
}

</style>