<script setup>
import { CustomMarker, GoogleMap, Marker } from 'vue3-google-map'
import { pins }  from '../main.js'
const center = { lat: 52.254205, lng: 20.903159 }
const handlePinClick = (pin) => {
  console.log("Marker clicked", pin)
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
  >
    <span v-for="pin in pins" :key="pin.ID">
      <CustomMarker 
        :options="{ position: { lat: pin.x, lng: pin.y } }"
        @click="() => handlePinClick(pin)"
      >
        <img src="/Ikonka_autobus.png" style="width:55px;height:55px;" />
      </CustomMarker>
    </span>
  </GoogleMap>
</template>

<style scoped>
* {
  width: 100%;
  height: 100%;
}
</style>