import { createApp, ref } from 'vue'
import App from './App.vue'

export const pins = ref([]); // Initialize as a reactive reference for pins list

async function fetchData() {
    try {
        const res = await fetch(
            `http://127.0.0.1:8000/pins`
        );
        pins.value = await res.json();

        console.log(pins.value)
    } catch (error) {
        console.error('Error fetching pins data:', error);
    }
}

// Initial fetch
fetchData();

// Fetch data at intervals
setInterval(fetchData, 2000); // Fetch data every 5 seconds (adjust as needed)

createApp(App).mount('#app')