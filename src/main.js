import { createApp, ref } from 'vue'
import App from './App.vue'
import { ip_const } from './components/hostip';

export const pins = ref([]); // Initialize as a reactive reference for pins list
export const favs = ref([]);

async function fetchData() {
    try {
        const res1 = await fetch(
            `http://${ip_const}:8000/pins`
        );
        pins.value = await res1.json();

        console.log(pins.value)
    } catch (error) {
        console.error('Error fetching pins or favs data:', error);
    }
}
async function dupa() {
    try {
        const res2 = await fetch(
            `http://${ip_const}:8000/fav/1`
        );
        favs.value = await res2.json().then(console.log(favs));
    } catch (error) {
        console.error('Error fetching pins or favs data:', error);
    }
}
// Initial fetch
fetchData();
dupa();


// Fetch data at intervals
setInterval(fetchData, 2000); // Fetch data every 5 seconds (adjust as needed)

createApp(App).mount('#app')