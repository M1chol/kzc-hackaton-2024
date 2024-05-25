<template>
    <div id="wrapper1">
        <div id="wrapper2">
            <nav>
                <div id="upperBar">
                    <div id="search"></div>
                    <div id="logo"></div>
                    <div id="menubutton">
                        <MenuButton @toggleMenu="(state) => handleToggleMenu(state)"></MenuButton>
                    </div>
                </div>
                <div id="middlebar">
                    <Menu></Menu>
                </div>
                <div id="lowerbar">
                    <div id="favourites">
                        <Favourite></Favourite>
                    </div>
                </div>
            </nav>
        </div>
    </div>
</template>

<script setup>
    const handleToggleMenu = (state) => {
        if(state){
            document.getElementById("middlebar").style.display ="block";
            document.getElementById("lowerbar").style.display ="none";
        } else {
            document.getElementById("middlebar").style.display = "none";
            document.getElementById("lowerbar").style.display ="block";
        }
    }
</script>

<script>
import MenuButton from './MenuButton.vue'
import Menu from './Menu.vue'
import Favourite from './Favourites.vue'

export default {
    name: 'Dropdown',
    components: {
        MenuButton,
        Favourite
    }
}
</script>

<style scoped>

#middlebar {
    display: none;
    height: calc(100vh - 80px);
    width: 100%;
}

nav {
    pointer-events: all;
    display: flex;
    border-radius: 20px;
    flex-direction: column;
    overflow: hidden;
    background-color: #DDDDDD;
    flex-basis: 700px;
    box-shadow: 0 3px 30px gray;
    margin: 10px;
}

#upperBar {
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
#menubutton {
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
    pointer-events: none;
}

#wrapper2 {
    display: flex;
    justify-content: right;
}
</style>