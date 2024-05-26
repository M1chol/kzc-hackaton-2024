<template>
    <div id="menu">
        <div id="profile">
            <img src="../assets/pp_placeholder.jpg" id="pp">
            <p>Witaj, Admin</p>
        </div>
        <div id="schedule" class="option">Plan Lekcji</div>
        <div id="calculator" class="option">Kalkulator Sredniej</div>
        <div id="miniwiki" class="option">Poradnik</div>
        <div id="logout" class="option">Wyloguj -></div>
    </div>
</template>

<script setup>
</script>

<style>

#logout {
    background-color: #627254;
    color: #EEEEEE;
    margin-top: 50px;
}

#profile p {
    font-size: 20px;
    text-align: center;
    font-weight: bold;
}

#pp {
    border:#627254 3px solid;
    height: 150px;
    width: 150px;
    border-radius: 75px;
}
#profile {
    height: 150px;
    width: 150px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 70px;
}

.option:hover {
    cursor: pointer;
}
#menu {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap:20px;
    padding: 20px;
    overflow-y: scroll;
    overflow-x: hidden;
    touch-action: pan-y;
}
.option {
    text-transform: uppercase;
    padding: 0;
    text-align: center;
    line-height: 70px;
    margin-left: auto;
    margin-right: auto;
    width: 320px;
    height: 70px;
    background-color: #EEEEEE;
    border-radius: 20px;
}
</style>