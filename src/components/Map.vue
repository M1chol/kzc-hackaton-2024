<script setup>
import { CustomMarker, GoogleMap, InfoWindow } from 'vue3-google-map'
import { pins } from '../main.js'
import Popup from './Popup.vue'
const center = { lat: 52.254205, lng: 20.903159 }
let activePopups = []
let pinPosts = []
let popupContent = ""
const handlePinClick = (pin) => {
  console.log("Marker clicked", pin)
  activePopups.push(pin)
  fetch(`http://127.0.0.1:8000/pin/${pin.ID}`).then(res => res.text()).then(res => popupContent = res)
  fetch(`http://127.0.0.1:8000/posts/${pin.ID}`).then(res => res.json()).then(res => pinPosts = res) // TODO: Check if work
  console.log(pinPosts)
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
  :fullscreenControl="false"
  :clickableIcons="false"
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
        <InfoWindow :options="{ position: { lat: popup.x, lng: popup.y } }"> <Popup :title="popup.text" :content="popupContent" :posts="pinPosts"/> </InfoWindow>
    </span>
  </GoogleMap>
</template>

<style scoped>
* {
  width: 100%;
  height: 100%;
}
</style>