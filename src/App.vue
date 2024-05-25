<template>
  <GMapMap
      :center="{lat: 51.093048, lng: 6.842120}"
      :zoom="7"
      map-type-id="terrain"
      style="width: 100%; height: 100%"
  >
  </GMapMap>
</template>

<script >
export default {
  name: 'App',
  data() {
    return {
      center: {lat: 51.093048, lng: 6.842120},
    }
  }
}
</script>

