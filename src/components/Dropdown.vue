<template>
    <nav>
      <div id="upperbar">
        <div id="search"></div>
        <div id="logo"></div>
        <div id="menu">
          <MenuButton></MenuButton>
        </div>
      </div>
      <div id="lowerbar">
        <div id="markers">
          <div class="marker">
            <span>20</span>
          </div>
        </div>
      </div>
    </nav>
</template>

<script>
import MenuButton from 'MenuButton.vue'

export default {
    name: 'Dropdown',
    components: {
        MenuButton
    }
}
</script>

<style scoped>
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

body {
    margin: 0;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap-reverse;
    justify-content: center;
    background-image: url("../src/assets/testbackground.jpg");
}

nav {
    height: 110px;
    display: flex;
    border-radius: 20px;
    flex-direction: column;
    overflow: hidden;
    background-color: #DDDDDD;
    margin: 10px;
    max-width: 700px;
    box-shadow: 0 3px 30px gray;
}

#upperbar {
    background-color: #EEEEEE;
    flex-direction: row;
    display: flex;
    height: 60px;
    border-radius: 20px;
}

#search {
    flex-grow: 0;
    flex-shrink: 0;
    flex-basis: 100px;
}
#logo {
    flex-basis: 100%;    
}
#menu {
    display: flex;
    justify-content: right;
    flex-grow: 0;
    flex-shrink: 0;
    flex-basis: 100px;
    padding-right: 10px;
    padding-top: 5px;
}

#lowerbar {
    padding: 5px;
    height: 50px;
    flex-direction: row;
    display: flex;
    gap: 5px;
}

.marker {
    height: 40px;
    background-color: #EEEEEE;
    gap: 5px;
}

#app {
    flex-grow: 5;
    background-color: #627254;
}
</style>