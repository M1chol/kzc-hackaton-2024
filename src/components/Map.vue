<script setup>
import { CustomMarker, GoogleMap, InfoWindow } from 'vue3-google-map'
import { pins } from '../main.js'
import Popup from './Popup.vue'
import { ip_static } from './ipstatic.js';
const center = { lat: 52.254205, lng: 20.903159 }
let activePopups = []
let pinPosts = []
let popupContent = ""

const handlePinClick = (pin) => {
  activePopups[0]=pin
  console.log("Marker clicked", pin)
  fetch(`http://${ip_static}:8000/pin/${pin.ID}`).then(res => res.text()).then(res => popupContent = res)
  fetch(`http://${ip_static}:8000/posts/${pin.ID}`).then(res => res.json()).then(res => pinPosts = res)
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
function dupa() {
  activePopups = []
}
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
        @click="handlePinClick(pin)"
      >
        <img v-bind:src="lookupIcon[pin.iconID]" style="width:27px;height:27px;" />
      </CustomMarker>
    </span>
    <span v-for="popup in activePopups" :key="popup.ID">
        <InfoWindow @closeclick="dupa" :options="{ position: { lat: popup.x, lng: popup.y } }"> <Popup :title="popup.name" :content="popupContent" :posts="pinPosts" :pinId2="popup.ID"/> </InfoWindow>
    </span>
  </GoogleMap>
</template>

<style scoped>
* {
  width: 100%;
  height: 100%;
}
</style>