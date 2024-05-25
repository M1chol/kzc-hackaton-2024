<template>
    <div id="wrapper1">
        <div id="wrapper2">
            <nav>
                <div id="upperbar">
                    <div id="search"></div>
                    <div id="logo"></div>
                    <div id="menu">
                    <MenuButton @toggleMenu="handleToggleMenu"></MenuButton>
                    </div>
                </div>
                <div id="lowerbar">
                    <div id="markers">
                        <Marker></Marker>
                    </div>
                </div>
            </nav>
        </div>
    </div>
</template>

<script setup>
    const handleToggleMenu = () => {
        console.log("test")
    }
</script>

<script>
import MenuButton from './MenuButton.vue'
import Marker from './Favourites.vue'

export default {
    name: 'Dropdown',
    components: {
        MenuButton,
        Marker
    }
}


</script>

<style scoped>


nav {
    display: flex;
    border-radius: 20px;
    flex-direction: column;
    overflow: hidden;
    background-color: #DDDDDD;
    flex-basis: 700px;
    box-shadow: 0 3px 30px gray;
    margin: 10px;
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

#wrapper1 {
    position: absolute;
    width: 100%;
    z-index: 1;
}

#wrapper2 {
    display: flex;
    justify-content: right;
}
</style>