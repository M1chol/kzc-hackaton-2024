import { createApp, ref } from 'vue'
import App from './App.vue'

export const pins = ref([]); // Initialize as a reactive reference for pins list
export const favs = ref([]);

async function fetchData() {
    try {
        const res1 = await fetch(
            `http://127.0.0.1:8000/pins`
        );
        pins.value = await res1.json();
        // const res2 = await fetch(
        //     `http://127.0.0.1:8000/fav/1`
        // );
        // favs.value = await res2.json();
        console.log(pins.value)
        //console.log(favs.value)
    } catch (error) {
        console.error('Error fetching pins or favs data:', error);
    }
}

// Initial fetch
fetchData();

// Fetch data at intervals
setInterval(fetchData, 2000); // Fetch data every 5 seconds (adjust as needed)

createApp(App).mount('#app')