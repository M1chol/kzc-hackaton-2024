<script setup>
import { CustomMarker, GoogleMap, InfoWindow } from 'vue3-google-map'
import { pins } from '../main.js'
import Popup from './Popup.vue'
const center = { lat: 52.254205, lng: 20.903159 }
let activePopups = []
let popupId = 0
const handlePinClick = (pin) => {
  console.log("Marker clicked", pin)
  activePopups.push({ ID: popupId++, x: pin.x, y: pin.y, text: pin.name })
  console.log(activePopups)
}
const lookupIcon = [
  "/Ikonka_autobus.png",
  "/Ikonka_jedzenie.png",
  "/Ikonka_sport.png",
  "/Ikonka_szpital.png",
  "/Ikonka_tramwaj.png",
  "/Ikonka_uczelnia.png",
  "/Ikonka_wip.png"
]
</script>

<template>
  <GoogleMap
  api-key="AIzaSyBuA4DzGdYl_hOXUgB3W5ejpnxhu0f6rPg"
  style="width: 100%;
   height: 100%;
    position: absolute;
    top: 0px;
   "
  :center="center"
  :zoom="15"
  >
    <span v-for="pin in pins" :key="pin.ID">
      <CustomMarker 
        :options="{ position: { lat: pin.x, lng: pin.y } }"
        @click="() => handlePinClick(pin)"
      >
        <img v-bind:src="lookupIcon[pin.iconID]" style="width:25px;height:25px;" />
      </CustomMarker>
    </span>
    <span v-for="popup in activePopups" :key="popup.ID">
        <InfoWindow :options="{ position: { lat: popup.x, lng: popup.y } }"> <Popup :title="popup.text"/> </InfoWindow>
    </span>
  </GoogleMap>
</template>

<style scoped>
* {
  width: 100%;
  height: 100%;
}
</style>