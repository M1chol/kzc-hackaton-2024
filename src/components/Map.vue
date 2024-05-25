<script setup>
import { GoogleMap, Marker } from 'vue3-google-map'
import { pins }  from '../main.js'
const center = { lat: 52.254205, lng: 20.903159 }
</script>

<template>
  <GoogleMap
  api-key="AIzaSyBuA4DzGdYl_hOXUgB3W5ejpnxhu0f6rPg"
  style="width: 100%;
   height: 100%;
    position: absolute;
   "
  :center="center"
  :zoom="15"
  >
    <span v-for="pin in pins" :key="pin.ID">
      <Marker :options="{ position: {lat: pin.lat, lng: pin.lng} }" />
    </span>
  </GoogleMap>
</template>

<style scoped>
* {
  width: 100%;
  height: 100%;
}
</style>