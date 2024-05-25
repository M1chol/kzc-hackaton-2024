<template>
  <Dropdown></Dropdown>
  <Map></Map>
</template>

<script>
import Map from './components/Map.vue'
import Dropdown from './components/Dropdown.vue'

export default {
  name: 'App',
  components: {
    Map,
    Dropdown
  }
}
</script>

<style>
.darkgreen {
    background-color: #627254;
}

.lightgreen {
    background-color: #76885B;
}

.gray {
    background-color: #DDDDDD;
}

.lightgray {
    background-color: #EEEEEE;
}

* {
  margin: 0;
}
#app {
  height: 100vh;
}

</style>
