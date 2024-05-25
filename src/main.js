import { createApp } from 'vue'
import VueGoogleMaps from '@fawmi/vue-google-maps'

let apikey = ""

try {
    const data = fs.readFileSync('./google-api.txt', 'utf8');
    apikey = data
} catch (err) {
    console.error(err);
}

const app = createApp(App);
app.use(VueGoogleMaps, {
    load: {
        key: apikey,
        // language: 'de',
    },
}).mount('#app')
