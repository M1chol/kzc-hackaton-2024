<template>
    <div id="wrapper1">
        <div id="wrapper2">
            <nav>
                <div id="upperBar">
                    <div id="searchbar">
                        <input id="search" name="text" placeholder="Search..." type="search">
                    </div>
                    <div id="logo"><b>WAT CONNECT</b></div>
                    <div id="menubutton">
                        <MenuButton @toggleMenu="(state) => handleToggleMenu(state)"></MenuButton>
                    </div>
                </div>
                <div id="middlebar">
                    <Menu></Menu>
                </div>
                <div id="lowerbar">
                    <Favourite></Favourite>
                </div>
            </nav>
        </div>
    </div>

</template>

<script setup>
function addPost() {
        
    }

    const handleToggleMenu = (state) => {
        if(state){
            document.getElementById("middlebar").style.display ="flex";
            document.getElementById("lowerbar").style.display ="none";
            document.getElementById("addpost").style.display = "none";
        } else {
            document.getElementById("middlebar").style.display = "none";
            document.getElementById("lowerbar").style.display ="flex";
            document.getElementById("addpost").style.display ="block";

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

#logo {
    line-height: 60px;
    margin-left: 10px;
    font-size: 20px;
    overflow: hidden;
}



    #search {
        margin-top: 10px;
        margin-left: 10px;
        max-width: 150px;
        background-color: #f5f5f5;
        color: #627254;
        padding: .15rem .5rem;
        min-height: 40px;
        border-radius: 15px;
        outline: none;
        border: none;
        line-height: 1.15;
        box-shadow: 0px 10px 20px -18px;
      }
      
      #search:focus {
        border-bottom: 2px solid #627254;
        border-radius: 15px;
      }
      
      #search:hover {
        outline: 1px solid lightgrey;
      }



#middlebar {
    display: none;
    height: calc(100vh - 80px);
    width: 100%;
    flex-direction: column;
    flex-wrap: wrap;
    justify-content: space-between;
    align-content: center;
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

#searchbar {
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
    flex-basis: 50px;
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